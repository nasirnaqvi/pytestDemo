# Pytest OrangeHRM Demo
This repository contains a Selenium automation framework for testing web applications using Python. The framework provides reusable methods for interacting with a web application and includes several page object models (POMs) for interacting with specific parts of the application.


## Prerequisites
Before you can run the tests, you need to set up the following:

1. Python (3.10 or later)
2. To install the dependencies listed in requirements.txt, run the following command in your terminal or command prompt:

    `pip install -r requirements.txt`


## Installation

Follow the steps below to set up the project on your local machine:

1. Clone the Repository \
Start by cloning the repository to your local machine:

    ``` 
    git clone [need to insert link]
    cd pytest-orangehrm-demo
   ```
2. Set Up a Virtual Environment (Optional but Recommended) \

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

