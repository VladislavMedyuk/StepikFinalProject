import enum


class Resources:
    PRODUCT_PAGE_LINK = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    MAIN_LINK = "http://selenium1py.pythonanywhere.com/"
    TIMEOUT = 30


class Browsers(enum.Enum):
    CHROME_BROWSER = "chrome"
    FIREFOX_BROWSER = "firefox"
