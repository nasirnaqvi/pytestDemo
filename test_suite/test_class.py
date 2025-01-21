import pytest
from time import sleep

from selenium.webdriver.common.by import By




@pytest.mark.usefixtures("login")
class TestOrangeHRM:

    @pytest.fixture(autouse=True)
    def setup_method(self, login):
        self.driver, self.configs = login

    def teardown_method(self, method):
        pass

    def test_items(self):
        self.driver.find_element(By.XPATH, "//a[span[text() = 'PIM']]").click()

        sleep(5)