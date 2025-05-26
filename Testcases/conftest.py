import pytest
import undetected_chromedriver as uc
from selenium import webdriver


# CLI argument support
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome or firefox"
    )


# Fetch browser name from CLI
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser").lower()


# Setup driver with undetected Chrome
@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        options = uc.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = uc.Chrome(options=options)

    elif browser == "firefox":
        driver = webdriver.Firefox()  # Regular Firefox (not undetected)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    return driver

######## Html report generation############


def pytest_configure(config):
    # Optional: Set HTML path here if not passed from command line
    config.option.htmlpath = 'Reports/report.html'

def pytest_html_report_title(report):
    report.title = "NopCommerce Automation Test Report"

def pytest_metadata(metadata):
    metadata['Project Name'] = 'Nop Commerce'
    metadata['Module Name'] = 'Login'
    metadata['Tester'] = 'shanthi T'

