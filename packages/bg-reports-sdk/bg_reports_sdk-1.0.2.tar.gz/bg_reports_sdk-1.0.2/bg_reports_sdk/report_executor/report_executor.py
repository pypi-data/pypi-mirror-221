import json
from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from time import sleep

import pytz
import requests
from bg_reports_sdk.data_provider.data_provider import DataProvider
from bg_reports_sdk.scheduler_manager.scheduler_manager import SchedulerManager

from bg_reports_sdk.config import *


class ReportSDKError(Exception):
    pass


class ReportExecutionError(Exception):
    pass


class ReportExecutor(ABC):
    report_type = None

    data_provider = None

    schedule_manager_class = None

    success_processed_reports_count = 0

    _SCHEDULER_UPDATE_INTERVAL = 10 * 60

    _BACKEND_URL = f"{BACKEND_HOST}/api"

    def __init__(self, master_token):
        self._master_token = master_token
        self._request_headers = {"x-token": self._master_token}
        self.data_provider = DataProvider(x_app_key=self.report_type)

        if self.schedule_manager_class is not None and issubclass(
            self.schedule_manager_class, SchedulerManager
        ):
            self.schedule_manager = self.schedule_manager_class(
                master_token=master_token
            )

            if self.report_type != self.schedule_manager.report_type:
                raise ReportSDKError("Incompatible report and scheduler report types")
        else:
            self.schedule_manager = None

    def _get_reports(self):
        """
        Получение отчетов
        """

        # Отчеты, которые находятся в очереди
        in_queue_reports = requests.get(
            f"{self._BACKEND_URL}/background-reports/?report_type={self.report_type}&status=in_queue",
            headers=self._request_headers,
        )

        current_report_type = self._get_report_type_by_name(name=self.report_type)

        other_reports_query_params = [
            f"report_type={self.report_type}",
            f"status=in_progress,failure",
            f"attempts_lt={current_report_type['max_attempts']}",
            f"delayed_to_lt={datetime.now(pytz.timezone('UTC')).strftime('%Y-%m-%dT%H:%M:%SZ')}",
        ]

        # Получение других отчетов по квери параметрам выше
        other_reports = requests.get(
            f"{self._BACKEND_URL}/background-reports/?{'&'.join(other_reports_query_params)}",
            headers=self._request_headers,
        )

        if in_queue_reports.ok and other_reports.ok:
            return in_queue_reports.json() + other_reports.json()

        raise ReportSDKError(f"An error accrued while getting reports.")

    def _get_report_type_by_name(self, name):
        """
        Получение типа отчета по его имени

        Args:
            name (str): Имя отчета

        Returns:
            dict: Объект типа отчета
        """
        response = requests.get(
            f"{self._BACKEND_URL}/background-report-types/?name={name}",
            headers=self._request_headers,
        )

        if response.ok:
            result = response.json()
            if len(result) > 0:
                return result[0]

        raise ReportSDKError(
            f"An error accrued while getting report type with name {name}. {response.text}"
        )

    def _get_report_by_id(self, report_id):
        """
        ПОлучение отчета по id

        Args:
            report_id (int): ID отчета

        Returns:
            dict: Объект отчета
        """
        response = requests.get(
            f"{self._BACKEND_URL}/background-reports/{report_id}",
            headers=self._request_headers,
        )

        if response.ok:
            return response.json()

        raise ReportSDKError(
            f"An error accrued while getting report with id {report_id}. {response.text}"
        )

    def _start_report_processing(self, report_id, ignore_checks=False):
        """
        Запуск отчета

        Args:
            report_id (int): ID отчета
            ignore_checks (int): Если был передан этот флаг, то ручка запуска отчета будет игнорировать проверки

        Returns:
            dict: {report: Report, token: str}
        """

        query_params = []

        if ignore_checks:
            query_params.append(f"force={ignore_checks}")

        response = requests.patch(
            f"{self._BACKEND_URL}/start-background-report-processing/{report_id}/?{'&'.join(query_params)}",
            headers=self._request_headers,
        )

        if response.ok:
            return response.json()

        raise ReportSDKError(
            f"An error accrued while start report processing with id {report_id}. {response.text}"
        )

    def _set_report_result(self, report_id, report_result):
        """
        Запись результата отчета

        Args:
            report_id (int): ID отчета
            report_result (dict): {result: any, status: str, log: str}

        Returns:
            dict: Report
        """

        response = requests.patch(
            f"{self._BACKEND_URL}/set-background-report-result/{report_id}/",
            headers={
                **self._request_headers,
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            data=json.dumps(report_result),
        )

        if response.ok:
            self.success_processed_reports_count += 1
            return

        raise ReportSDKError(
            f"An error accrued while setting report result with id {report_id}. {response.text}"
        )

    @abstractmethod
    def _process_report(self, report, token):
        """
        Для корректной работы класса - необходимо переопределить этот метод.

        Args:
            report (Report): данные отчета
            token (str): токен (НЕ МАСТЕР)

        Returns:
            dict: {result: any; status: str; log: str}
        """
        raise ReportExecutionError("You should implement _process_report method")

    def _run_with_report_id(self, report_id):
        report = self._get_report_by_id(report_id=report_id)
        report_processing_result = self._start_report_processing(
            report_id=report["id"], ignore_checks=True
        )

        try:
            result = self._process_report(
                report=report_processing_result["report"],
                token=report_processing_result["token"],
            )
            print(f"Report with id {report_id} processed!")
        except Exception as e:
            raise ReportExecutionError(e.__traceback__)

        self._set_report_result(report_id=report["id"], report_result=result)

    def _run_cycle(self):
        reports = self._get_reports()

        if len(reports) == 0:
            print("No available reports. Sleep 30 sec...")
            sleep(30)

        for report in reports:
            report_processing_result = self._start_report_processing(
                report_id=report["id"]
            )
            try:
                result = self._process_report(
                    report=report_processing_result["report"],
                    token=report_processing_result["token"],
                )
            except Exception as e:
                raise ReportExecutionError(e.__traceback__)
            self._set_report_result(report_id=report["id"], report_result=result)

    def _run_scheduler_if_needed(self, last_scheduler_run):
        if (
            self.schedule_manager is not None
            and (datetime.now() - last_scheduler_run).total_seconds()
            <= self._SCHEDULER_UPDATE_INTERVAL
        ):
            try:
                self.schedule_manager.run()
                last_scheduler_run = datetime.now()
            except ReportSDKError as e:
                print(e)
            except ReportExecutionError as e:
                print(e)

        return last_scheduler_run

    def run(self, report_id=None):
        """
        Запуск обработки отчетов

        Args:
            report_id (number, optional): Если передан ID отчета то обработка будет проходить только по одному отчету
            с игнорированием проверок. Defaults to None.
        """
        last_scheduler_run = datetime.now() - timedelta(
            seconds=self._SCHEDULER_UPDATE_INTERVAL
        )
        if report_id is None:
            while True:
                last_scheduler_run = self._run_scheduler_if_needed(last_scheduler_run)
                try:
                    self._run_cycle()
                except ReportSDKError as e:
                    print(e)
                except ReportExecutionError as e:
                    print(e)

                sleep(5)
        else:
            last_scheduler_run = self._run_scheduler_if_needed(last_scheduler_run)
            try:
                self._run_with_report_id(report_id=report_id)
            except ReportSDKError as e:
                raise e
            except ReportExecutionError as e:
                raise e
