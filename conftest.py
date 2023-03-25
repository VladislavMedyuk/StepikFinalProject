import pytest
from selenium import webdriver
from resourses.env import Resources


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default='en', help='Choose language')


@pytest.fixture(scope="function")
def browser(request):
    BROWSER_NAME = request.config.getoption("browser_name").lower()
    LANGUAGE = request.config.getoption("language").lower()
    browser = None
    match BROWSER_NAME:
        case Resources.CHROME_BROWSER:
            print("\nstart chrome browser for test..")
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            options.add_experimental_option('prefs', {'intl.accept_languages': LANGUAGE})
            browser = webdriver.Chrome(options=options)
        case Resources.FIREFOX_BROWSER:
            print("\nstart firefox browser for test..")
            options = webdriver.FirefoxOptions()
            options.set_preference("intl.accept_languages", LANGUAGE)
            browser = webdriver.Firefox(options=options)
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()
