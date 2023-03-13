import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService


# Define a fixture to initialize the driver based on the provided browser
@pytest.fixture(scope='class')
def driver(request):
    browser = request.config.getoption("--browser")
    # Create the driver based on the selected browser
    print(f"creating {browser} driver")
    if browser == "chrome":
        my_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        my_driver.maximize_window()
    elif browser == "firefox" or browser == "ff":
        my_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        my_driver.maximize_window()
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox', but got {browser}")

    # Return the driver to be used in tests
    yield my_driver

    # Quit the driver after tests are complete
    print(f"closing {browser} driver")
    my_driver.quit()


# Define a command line option to select the browser for running tests
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)"
    )
