from pathlib import Path
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

PROJECT_ROOT = Path(__file__).resolve().parent.parent
REPORTS_FOLDER = PROJECT_ROOT / "reports"


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    REPORTS_FOLDER.mkdir(parents=True, exist_ok=True)

    run_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_file = REPORTS_FOLDER / f"test_report_{run_time}.html"

    config.option.htmlpath = str(report_file)


@pytest.fixture
def driver(request):
    options = Options()
    options.add_argument("--window-size=1440,900")

    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        },
    )

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(0)

    try:
        yield browser
    finally:
        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
            screenshot_folder = REPORTS_FOLDER / "screenshots"
            screenshot_folder.mkdir(parents=True, exist_ok=True)

            screenshot_file = screenshot_folder / f"{request.node.name}.png"
            browser.save_screenshot(str(screenshot_file))

        browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)