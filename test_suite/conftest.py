import pytest
from selenium import webdriver
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from page_objects.login_page import LoginPage

@pytest.fixture(scope="session", autouse=True)
def load_env(request):
    env_path = r"../.env"
    if not os.path.exists(env_path):
        raise FileNotFoundError(f"Environment file {env_path} not found.")

    load_dotenv(dotenv_path=env_path)

@pytest.fixture(scope="class")
def webdriver_handler() -> webdriver.Chrome:
    # Set up Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.implicitly_wait(5)

    yield driver

    driver.quit()

@pytest.fixture(scope="class")
def login(webdriver_handler: webdriver.Chrome):
    username = os.environ["USERNAME"]
    password = os.environ["PASSWORD"]
    url = os.environ["URL"]

    webdriver_handler.get(url)
    login_page = LoginPage(webdriver_handler)
    login_page.login(username, password)

    yield webdriver_handler
