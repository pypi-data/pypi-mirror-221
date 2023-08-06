from setuptools import setup, find_packages

setup(
    name="bg_reports_sdk",
    version="1.0.2",
    packages=find_packages(),
    install_requires=["requests", "python-dotenv", "pytz"],
    author="Nikita Surov",
    author_email="n.surov@focus.bi",
    description="Software development kit for creating reports and their schedulers.",
    # url="https://github.com/your_username/app",
)
