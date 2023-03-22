from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    login_page = LoginPage(browser, url)
    page = MainPage(browser, url)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
    login_page.should_be_login_url()
    login_page.should_be_login_form()
    login_page.should_be_register_form()
