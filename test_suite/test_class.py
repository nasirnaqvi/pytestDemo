import pytest
from time import sleep

from selenium.webdriver.common.by import By
from page_objects.admin_page import AdminPage

# Typically we use Camel Case for defining test classes
@pytest.mark.usefixtures("login")
class TestAdminPage:

    @pytest.fixture(autouse=True)
    def setup_method(self, login):
        """This runs prior to each test"""
        self.driver = login
        self.page = AdminPage(self.driver)
        self.page.select_admin_tab()
        sleep(2)

    @pytest.fixture(autouse=True)
    def teardown_method(self):
        """Everything after the yield will run after each test"""
        yield

    # We usually use Snake Case for defining individual test methods
    def test_admin_page_functionality(self):
        """Perform some testing on the admin page"""
        assert True


    def test_add_user(self):
        """Perform some testing on adding a user"""
        assert True