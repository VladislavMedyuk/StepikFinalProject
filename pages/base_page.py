from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from resourses.env import Resources
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self, browser: webdriver, url: str):
        self.__browser = browser
        self.__url = url

    @property
    def browser(self) -> webdriver:
        return self.__browser

    @browser.setter
    def browser(self, browser: webdriver):
        self.__browser = browser

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    def open(self):
        self.browser.get(self.url)

    def search_element(self, locator: tuple) -> WebElement:
        try:
            WebDriverWait(self.browser, Resources.TIMEOUT).until(
                EC.visibility_of_element_located(locator)
            )
        finally:
            return self.browser.find_element(*locator)

    def is_element_present(self, locator: tuple) -> bool:
        try:
            WebDriverWait(self.browser, Resources.TIMEOUT).until(
                EC.visibility_of_element_located(locator)
            )
        except NoSuchElementException:
            return False
        return True
