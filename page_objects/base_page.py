from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def select_tab(self, tab_name):
        """Select a tab by its name."""
        return (By.XPATH, f"//a[span[text() = '{tab_name}']]")

    def select_admin_tab(self):
        """Select the 'Admin' tab."""
        admin_tab = self.select_tab("Admin")
        return self.driver.find_element(*admin_tab).click()

    def select_pim_tab(self):
        """Select the 'PIM' tab."""
        pim_tab = self.select_tab("PIM")
        return self.driver.find_element(*pim_tab).click()

    def select_leave_tab(self):
        """Select the 'Leave' tab."""
        leave_tab = self.select_tab("Leave")
        return self.driver.find_element(*leave_tab).click()

    def select_time_tab(self):
        """Select the 'Time' tab."""
        time_tab = self.select_tab("Time")
        return self.driver.find_element(*time_tab).click()

    def select_recruitment_tab(self):
        """Select the 'Recruitment' tab."""
        recruitment_tab = self.select_tab("Recruitment")
        return self.driver.find_element(*recruitment_tab).click()

    def select_my_info_tab(self):
        """Select the 'My Info' tab."""
        my_info_tab = self.select_tab("My Info")
        return self.driver.find_element(*my_info_tab).click()

    def select_performance_tab(self):
        """Select the 'Performance' tab."""
        performance_tab = self.select_tab("Performance")
        return self.driver.find_element(*performance_tab).click()

    def select_dashboard_tab(self):
        """Select the 'Dashboard' tab."""
        dashboard_tab = self.select_tab("Dashboard")
        return self.driver.find_element(*dashboard_tab).click()

    def select_directory_tab(self):
        """Select the 'Directory' tab."""
        directory_tab = self.select_tab("Directory")
        return self.driver.find_element(*directory_tab).click()

    def select_maintenance_tab(self):
        """Select the 'Maintenance' tab."""
        maintenance_tab = self.select_tab("Maintenance")
        return self.driver.find_element(*maintenance_tab).click()

    def select_claim_tab(self):
        """Select the 'Claim' tab."""
        claim_tab = self.select_tab("Claim")
        return self.driver.find_element(*claim_tab).click()

    def select_buzz_tab(self):
        """Select the 'Buzz' tab."""
        buzz_tab = self.select_tab("Buzz")
        return self.driver.find_element(*buzz_tab).click()
