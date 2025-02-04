# Pytest OrangeHRM Demo
This repository was a demonstration of a testing framework. It contains a Selenium automation framework for testing web applications using Python. The framework provides reusable methods for interacting with a web application and includes several page object models (POMs) for interacting with specific parts of the application.


## Prerequisites
Before you can run the tests, you need to set up the following:

1. Python (3.10 or later)


## Installation

Follow the steps below to set up the project on your local machine:

1. Clone the Repository \
Start by cloning the repository to your local machine:

  ```
  git clone git@github.com:nasirnaqvi/pytestDemo.git
  cd pytest-orangehrm-demo
  ```
2. Set Up a Virtual Environment (Optional but Recommended) 

  To ensure the project dependencies are isolated from other Python projects on your system, it's best to use a virtual environment:
  ```
  python -m venv venv
  source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```
3. Install Dependencies \
   Once the virtual environment is activated, install the required dependencies by running:
  ```
  pip install -r requirements.txt
   ```
   This will install:

  - Selenium: For automating the browser interactions.
  - pytest: For running the tests and managing test execution.
  - webdriver-manager: To automatically handle browser driver installations.
  - pytest-html: Optional (for generating HTML reports of the test execution).


## Running Tests
You can run the tests using pytest, which will automatically discover and execute all the test files in the tests/ directory. To run the tests, simply execute:

```
cd test_suite
pytest --html=report.html
```
Explanation of Options:
- `--html=report.html`: This will create a report.html file in the current directory containing a detailed test execution report.
- Other options for project are listed in the `pytest.ini` file

## Introduction
When developing tests for web applications using Pytest, it's essential to follow best practices to ensure tests are maintainable, clear, and effective. This section introduces key principles for selecting XPath locators, organizing page objects, and writing high-quality test cases.

### Selecting XPath Locators
XPath locators are crucial for interacting with web elements in your tests. Follow these guidelines for effective XPath selection:

- Keep it simple and robust: Use unique attributes like id or data-testid when available to minimize brittleness. For example: `//button[@id='submit']`.
- Avoid hardcoding positions: Avoid expressions like `//div[3]` as changes to the DOM structure can break your tests.
- Use relative paths: Prefer shorter, context-specific paths over absolute paths to make locators easier to read and less fragile. For example: `//form[@id='login']//input[@name='username']`.

### Why Keep Page Objects Separated
The Page Object Model (POM) is a design pattern that improves test maintainability and readability by separating page-related logic from test logic.

- Reusability: Page objects encapsulate locators and methods, allowing you to reuse them across multiple test cases.
- Readability: Keeping page-specific methods in one place makes your tests easier to understand.
- Maintainability: When a UI change occurs, you only need to update the relevant page object instead of all affected tests.

```python
from selenium.webdriver.common.by import By
class LoginPage:
   username_element = (By.XPATH, "//input[@name='username']")
   password_element = (By.XPATH, "//input[@name='password']")
   submit_element = (By.XPATH, "//button[@type='submit']")
  
   def __init__(self, driver):
       self.driver = driver

   def enter_username(self, username):
       self.driver.find_element(*LoginPage.username_element).send_keys(username)

   def click_login(self):
       self.driver.find_element(*LoginPage.submit_element).click()
```

### Creating Good Test Cases
Effective test cases ensure your tests are robust and easy to debug. Consider the following principles:

1. Keep tests atomic: Each test should focus on one functionality to simplify debugging and ensure clarity.
2. Use descriptive names: Test names should clearly indicate the feature being tested. For example: test_login_with_valid_credentials.
3. Add assertions: Verify expected outcomes using meaningful assertions to validate functionality.
4. Leverage fixtures: Use Pytest fixtures to manage setup and teardown processes like initializing the WebDriver, logging in, or loading test data.
5. Parameterize when necessary: Use `@pytest.mark.parametrize` to test multiple inputs or edge cases in a single test function.
6. Use fixture for code used across test cases


Example of when to use parameterization:
```python
import pytest

@pytest.mark.parametrize("username,password", [
   ("valid_user", "valid_pass"),
   ("invalid_user", "invalid_pass"),
])
def test_login(login_page, username, password):
   login_page.enter_username(username)
   login_page.enter_password(password)
   login_page.click_login()
   expected_result = username == "valid_user"
   assert login_page.is_login_successful() == expected_result, (
       f"Login test failed for username: '{username}' and password: '{password}'. "
       f"Expected success: {expected_result}, but got: {login_page.is_login_successful()}."
   )
```

Example of using fixtures:
```python
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
   # Setup: Initialize WebDriver
   driver = webdriver.Chrome()
   driver.get("https://example.com")
   yield driver  # Provide the driver to the test. Everything after the yield runs once the test terminates
  
   # Teardown: Quit WebDriver after the test
   driver.quit()
```

To use this fixture, you can decorate your test set will decorator `pytest.mark.usefixtures("driver")`










