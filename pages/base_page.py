from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from resourses.env import Resources
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from locators.locators import BasePageLocators


class BasePage:
    def __init__(self, browser: webdriver, url: str) -> None:
        self.__browser = browser
        self.__url = url

    @property
    def browser(self) -> webdriver:
        return self.__browser

    @browser.setter
    def browser(self, browser: webdriver) -> None:
        self.__browser = browser

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str) -> None:
        self.__url = url

    def open(self) -> None:
        self.browser.get(self.url)

    def search_element(self, locator: tuple) -> WebElement:
        return WebDriverWait(self.browser, Resources.TIMEOUT).until(EC.visibility_of_element_located(locator))

    def should_be_login_link(self) -> None:
        assert self.is_element_present(BasePageLocators.LOGIN_LINK), "Login link is not present"

    def go_to_login_page(self) -> None:
        login_link = self.search_element(BasePageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_basket_page(self) -> None:
        basket_button = self.search_element(BasePageLocators.BASKET_BUTTON)
        basket_button.click()

    def is_not_element_present(self, locator: tuple) -> bool:
        try:
            WebDriverWait(self.browser, Resources.TIMEOUT).until(
                EC.invisibility_of_element_located(locator)
            )
        except TimeoutException:
            return False
        return True

    def is_element_present(self, locator: tuple) -> bool:
        try:
            return WebDriverWait(self.browser, Resources.TIMEOUT).until(
                EC.visibility_of_element_located(locator)
            ).is_displayed()
        except NoSuchElementException:
            return False

    def should_be_authorized_user(self):
        assert self.is_element_present(BasePageLocators.ICON_USER), "User icon is not presented," \
                                                                    " probably unauthorised user"
