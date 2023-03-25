import enum


class Resources:
    MAIN_LINK = "http://selenium1py.pythonanywhere.com/"
    TIMEOUT = 30


class Browsers(enum.Enum):
    CHROME_BROWSER = "chrome"
    FIREFOX_BROWSER = "firefox"
