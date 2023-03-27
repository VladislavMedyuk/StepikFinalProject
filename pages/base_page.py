from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from resourses.env import Resources
from selenium.webdriver.support import expected_conditions as EC
import math


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

    def is_element_present(self, locator: tuple) -> bool:
        try:
            WebDriverWait(self.browser, Resources.TIMEOUT).until(
                EC.visibility_of_element_located(locator)
            )
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
