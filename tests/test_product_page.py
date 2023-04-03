from pages.login_page import LoginPage
from resourses.env import Resources
from pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('link', Resources.LINKS)
def test_guest_can_add_item_to_basket(browser, link):
    page = ProductPage(browser, link)
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


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, Resources.PRODUCT_PAGE_LINK)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, Resources.PRODUCT_PAGE_LINK)
    page.open()
    page.add_item_to_basket()
    page.should_be_disappeared()
