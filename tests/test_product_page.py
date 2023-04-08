from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from resourses.env import Resources
from pages.product_page import ProductPage
import pytest


@pytest.mark.login
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, Resources.LOGIN_PAGE_LINK)
        page.open()
        email, password = page.make_email_and_password()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_item_to_basket(self, browser):
        page = ProductPage(browser, Resources.PRODUCT_PAGE_REVIEW)
        page.open()
        book_name = page.find_book_name()
        book_price = page.find_book_price()
        page.add_item_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_right_name_and_right_price(book_name, book_price)

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, Resources.PRODUCT_PAGE_LINK)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_can_add_item_to_basket(browser):
    page = ProductPage(browser, Resources.PRODUCT_PAGE_REVIEW)
    page.open()
    book_name = page.find_book_name()
    book_price = page.find_book_price()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_right_name_and_right_price(book_name, book_price)


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, Resources.PRODUCT_PAGE_LINK)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, Resources.PRODUCT_PAGE_LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, Resources.PRODUCT_PAGE_LINK)
    page.open()
    page.add_item_to_basket()
    page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, Resources.PRODUCT_PAGE_LINK)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty()
