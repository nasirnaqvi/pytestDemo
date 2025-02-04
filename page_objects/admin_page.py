from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from page_objects.base_page import BasePage


class AdminPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
