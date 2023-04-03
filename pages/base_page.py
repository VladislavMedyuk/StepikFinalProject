from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from resourses.env import Resources
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from locators.locators import BasePageLocators


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

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(BasePageLocators.LOGIN_LINK), "Login link is not present"

    def element_is_disappeared(self, locator: tuple):
        try:
            WebDriverWait(self.browser, Resources.TIMEOUT, 1, TimeoutException). \
                until_not(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, locator: tuple) -> bool:
        try:
            WebDriverWait(self.browser, Resources.TIMEOUT).until(
                EC.visibility_of_element_located(locator)
            )
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, locator: tuple) -> bool:
        try:
            WebDriverWait(self.browser, Resources.TIMEOUT).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            return True
        return False

    def open(self):
        self.browser.get(self.url)

    def search_element(self, locator: tuple) -> WebElement:
        try:
            WebDriverWait(self.browser, Resources.TIMEOUT).until(
                EC.visibility_of_element_located(locator)
            )
        finally:
            return self.browser.find_element(*locator)
