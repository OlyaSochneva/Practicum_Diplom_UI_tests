from pages.base_page import BasePage

from locators.login_page_locators import LoginPageLocators
from locators.reset_password_page_locators import ResetPasswordPageLocators
from locators.main_page_locators import MainPageLocators


class LoginPage(BasePage):
    def click_on_reset_password(self):
        self.anti_overlay_click()  # для Firefox
        self.click_and_wait_for(
            LoginPageLocators.RESET_PASSWORD_BUTTON, ResetPasswordPageLocators.EMAIL_INPUT)

    def login(self, data):
        self.fill_field(LoginPageLocators.EMAIL_INPUT, data['email'])
        self.fill_field(LoginPageLocators.PASSWORD_INPUT, data['password'])
        self.click_and_wait_for(LoginPageLocators.LOGIN_BUTTON, MainPageLocators.MENU_HEADER)
        self.anti_overlay_click()  # для Firefox
