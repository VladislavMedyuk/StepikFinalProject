from pages.base_page import BasePage
from locators.locators import LoginPageLocators
from faker import Faker


class LoginPage(BasePage):
    @staticmethod
    def make_email_and_password() -> tuple:
        faker = Faker()
        return faker.email(), faker.password()

    def should_be_login_page(self) -> None:
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self) -> None:
        assert "login" in self.browser.current_url, "There isn't part 'login' in current url"

    def should_be_login_form(self) -> None:
        assert self.is_element_present(LoginPageLocators.LOGIN_FORM), "Login Form is not present"

    def should_be_register_form(self) -> None:
        assert self.is_element_present(LoginPageLocators.REGISTRATION_FORM), "Register form is not present"

    def register_new_user(self, email, password):
        email_input = self.search_element(LoginPageLocators.REGISTRATION_EMAIL)
        password_input = self.search_element(LoginPageLocators.REGISTRATION_PASSWORD)
        repeat_password = self.search_element(LoginPageLocators.REGISTRATION_REPEAT_PASSWORD)
        submit_button = self.search_element(LoginPageLocators.REGISTRATION_BUTTON)

        email_input.send_keys(email)
        password_input.send_keys(password)
        repeat_password.send_keys(password)

        submit_button.click()
