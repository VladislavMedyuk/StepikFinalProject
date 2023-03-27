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

    def should_be_right_name_and_right_price(self, bookToCompare, priceToCompare):
        self.should_be_right_name(bookToCompare)
        self.should_be_right_price(priceToCompare)

    def should_be_right_name(self, bookToCompare):
        assert self.browser.find_element(*ProductPageLocators.BOOK_NAME).text == bookToCompare, "There isn't book in basket!"

    def should_be_right_price(self, priceToCompare):
        assert self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text == priceToCompare, "Wrong price for the book!"
