from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    username_element = (By.XPATH, "//input[@name='username']")
    password_element = (By.XPATH, "//input[@name='password']")
    submit_element = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(*self.username_element).send_keys(username)
        self.driver.find_element(*self.password_element).send_keys(password)
        self.driver.find_element(*self.submit_element).click()

