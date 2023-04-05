from pages.base_page import BasePage
from locators.locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_should_be_empty(self) -> None:
        self.shouldnt_be_any_product_in_basket()
        self.should_be_message_of_empty_basket_on_basket_page()

    def shouldnt_be_any_product_in_basket(self) -> None:
        assert self.search_element(BasketPageLocators.MESSAGE_EMPTY).text in self.search_element(
            BasketPageLocators.BASKET_IS_EMPTY).text, "No message of empty basket!"

    def should_be_message_of_empty_basket_on_basket_page(self) -> None:
        assert self.is_not_element_present(
            BasketPageLocators.BASKET_IS_NOT_EMPTY), "Basket is not empty, but it should be!"

    def should_be_no_message_of_empty_basket_on_basket_page(self) -> None:
        assert self.is_element_present(BasketPageLocators.BASKET_IS_NOT_EMPTY), "Basket is empty, but is should not be"
