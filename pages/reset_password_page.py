import allure

from assistant_methods import generate_random_email
from assistant_methods import generate_random_string

from pages.base_page import BasePage

from locators.reset_password_page_locators import ResetPasswordPageLocators


class ResetPasswordPage(BasePage):
    @allure.step("Проверяем, что открыта страница восстановления пароля")
    def check_reset_password_page_is_displayed(self):
        return self.check_element_visible(ResetPasswordPageLocators.EMAIL_INPUT)

    @allure.step("Вводим почту и нажимаем «Восстановить»")
    def enter_email_and_press_reset(self):
        self.fill_field(ResetPasswordPageLocators.EMAIL_INPUT, generate_random_email())
        self.click_and_wait_for(ResetPasswordPageLocators.RESET_BUTTON, ResetPasswordPageLocators.NEW_PASSWORD_INPUT)

    @allure.step("Проверяем, что открыта страница ввода нового пароля")
    def check_enter_new_password_page_is_displayed(self):
        return self.check_element_visible(ResetPasswordPageLocators.NEW_PASSWORD_INPUT)

    @allure.step("Вводим новый пароль (случайная строка)")
    def enter_new_password(self):
        self.fill_field(ResetPasswordPageLocators.NEW_PASSWORD_INPUT, generate_random_string(5))

    @allure.step("Вводим почту, нажимаем «восстановить», вводим новый пароль")
    def enter_new_password_flow(self):
        self.enter_email_and_press_reset()
        self.enter_new_password()

    @allure.step("Нажимаем на кнопку видимости и возвращаем поле ввода пароля")
    def click_pass_visibility_button_and_return_pass_input_field(self):
        self.anti_overlay_click()   # для Firefox
        self.click_element(ResetPasswordPageLocators.PASSWORD_VISIBILITY_BUTTON)
        return self.return_element(ResetPasswordPageLocators.NEW_PASSWORD_INPUT_FIELD)
