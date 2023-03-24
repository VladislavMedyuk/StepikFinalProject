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

    def is_element_present(self, method, selector):
        try:
            WebDriverWait(self.browser, Resources.timeout).until(
                EC.presence_of_element_located((method, selector))
            )
        except NoSuchElementException:
            return False
        return True

    # def solve_quiz_and_get_code(self):
