import pytest
import os
import allure
import subprocess

from dotenv import load_dotenv

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from page_objects.login_page import LoginPage

# Helper methods
def get_git_root():
    try:
        git_root = subprocess.check_output(["git", "rev-parse", "--show-toplevel"]).strip().decode('utf-8')
        return git_root
    except subprocess.CalledProcessError:
        raise Exception("Not inside a Git repository.")


# Pytest Fixtures
@pytest.fixture(scope="session", autouse=True)
def load_env(request):
    """Used to load env variables"""
    env_path = r"../.env"
    if not os.path.exists(env_path):
        raise FileNotFoundError(f"Environment file {env_path} not found.")

    load_dotenv(dotenv_path=env_path)

@pytest.fixture(scope="class")
def webdriver_handler() -> webdriver.Chrome:
    """Sets up a webdriver instance"""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.implicitly_wait(5)

    yield driver

    driver.quit()

@pytest.fixture(scope="class")
def login(webdriver_handler: webdriver.Chrome):
    """Used to login to an account"""
    username = os.environ["USERNAME"]
    password = os.environ["PASSWORD"]
    url = os.environ["URL"]

    webdriver_handler.get(url)
    login_page = LoginPage(webdriver_handler)
    login_page.login(username, password)

    yield webdriver_handler


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Used to take screenshot of where the test is failing for diagnostic purposes."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        try:
            driver = item.funcargs["webdriver_handler"]
            if driver:
                screenshot_dir = os.path.join(get_git_root(), "screenshots")

                if not os.path.exists(screenshot_dir):
                    os.makedirs(screenshot_dir)

                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                error_name = type(report.longrepr).__name__
                test_name = (
                    item.nodeid.replace("::", "_").replace("/", "_").replace("\\", "_")
                )

                screenshot_file = f"{timestamp}__{test_name}__{error_name}.png"
                screenshot_path = os.path.join(screenshot_dir, screenshot_file)

                driver.get_screenshot_as_file(screenshot_path)
                print(f"\n Screenshot saved to: {screenshot_path}")

                with open(screenshot_path, "rb") as f:
                    allure.attach(
                        f.read(),
                        name=screenshot_file,
                        attachment_type=allure.attachment_type.PNG,
                    )
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="screenshot",
                    attachment_type=allure.attachment_type.PNG,
                )
        except Exception as e:
            print(f"Failed to take screenshot: {e}")