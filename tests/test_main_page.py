from pages.login_page import LoginPage
from pages.main_page import MainPage
from resourses.env import Links


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, Links.MAIN_LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
