from selenium.common.exceptions import NoSuchElementException


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
            self.browser.find_element(method, selector)
        except NoSuchElementException:
            return False
        return True
