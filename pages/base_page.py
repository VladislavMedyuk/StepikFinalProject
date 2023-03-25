from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from resourses.env import Resources
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url):
        self.__browser = browser
        self.__url = url

    @property
    def browser(self):
        return self.__browser

    @browser.setter
    def browser(self, browser):
        self.__browser = browser

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        self.__url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, locator: tuple) -> bool:
        try:
            WebDriverWait(self.browser, Resources.TIMEOUT).until(
                EC.visibility_of_element_located(locator)
            )
        except NoSuchElementException:
            return False
        return True

    # def solve_quiz_and_get_code(self):
