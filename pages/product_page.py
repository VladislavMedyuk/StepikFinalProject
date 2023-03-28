import math
from selenium.common import NoAlertPresentException
from pages.base_page import BasePage
from locators.locators import ProductPageLocators


class ProductPage(BasePage):
    def find_book_name(self) -> str:
        return self.browser.find_element(*ProductPageLocators.BOOK_TO_COMPARE).text

    def find_book_price(self) -> str:
        return self.browser.find_element(*ProductPageLocators.PRICE_TO_COMPARE).text

    def add_item_to_basket(self):
        addButton = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        addButton.click()

    def should_be_success_message(self):
        assert self.is_element_present(ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented"

    def should_be_right_name_and_right_price(self, bookToCompare: str, priceToCompare: str):
        self.should_be_right_name(bookToCompare)
        self.should_be_right_price(priceToCompare)

    def should_be_right_name(self, bookToCompare: str):
        assert self.browser.find_element(
            *ProductPageLocators.BOOK_NAME).text == bookToCompare, "There isn't book in basket!"

    def should_be_right_price(self, priceToCompare: str):
        assert self.browser.find_element(
            *ProductPageLocators.BOOK_PRICE).text == priceToCompare, "Wrong price for the book!"

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
