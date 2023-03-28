import pytest
from selenium import webdriver
from resourses.env import Browsers


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default='en', help='Choose language')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name").lower()
    language = request.config.getoption("language").lower()
    match browser_name:
        case Browsers.CHROME_BROWSER.value:
            print("\nstart chrome browser for test..")
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            options.add_experimental_option('prefs', {'intl.accept_languages': language})
            browser = webdriver.Chrome(options=options)
        case Browsers.FIREFOX_BROWSER.value:
            print("\nstart firefox browser for test..")
            options = webdriver.FirefoxOptions()
            options.set_preference("intl.accept_languages", language)
            browser = webdriver.Firefox(options=options)
        case _:
            raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()
