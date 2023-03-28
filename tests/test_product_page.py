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
