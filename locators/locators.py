from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_USERNAME = (By.NAME, "login-username")
    LOGIN_PASSWORD = (By.NAME, "login-password")
    LOGIN_BUTTON = (By.NAME, "login_submit")

    REGISTRATION_FORM = (By.ID, "register_form")
    REGISTRATION_NAME = (By.NAME, "registration-email")
    PASSWORD = (By.NAME, "registration-password1")
    REPEAT_PASSWORD = (By.NAME, "registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")

