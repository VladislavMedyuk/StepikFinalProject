from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a")
    ICON_USER = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_USERNAME = (By.NAME, "login-username")
    LOGIN_PASSWORD = (By.NAME, "login-password")
    LOGIN_BUTTON = (By.NAME, "login_submit")

    REGISTRATION_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL = (By.NAME, "registration-email")
    REGISTRATION_PASSWORD = (By.NAME, "registration-password1")
    REGISTRATION_REPEAT_PASSWORD = (By.NAME, "registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    BOOK_NAME = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_TO_COMPARE = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_TO_COMPARE = (By.CSS_SELECTOR, ".product_main p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) .alertinner")


class BasketPageLocators:
    BASKET_IS_EMPTY = (By.ID, "content_inner")
    BASKET_IS_NOT_EMPTY = (By.CLASS_NAME, "basket-title")
    MESSAGE_EMPTY = (By.XPATH, "//*[@id='content_inner']/p")
