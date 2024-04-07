import pytest
import allure

from selenium.webdriver.support import expected_conditions

from pages.main_page import MainPage
from pages.login_page import LoginPage

from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.reset_password_page import ResetPasswordPage


class TestResetPasswordPage:
    @allure.title('Проверка: переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @pytest.mark.parametrize("driver", ['chrome', 'firefox'])
    def test_move_to_reset_password_page_by_click_reset_password(self, request, driver):
        driver = request.getfixturevalue(driver)                      # setup
        main_page, login_page = MainPage(driver), LoginPage(driver)   # setup
        main_page.click_on_login_button()
        login_page.click_on_reset_password()
        assert expected_conditions.visibility_of_element_located(ResetPasswordPageLocators.EMAIL_INPUT)

    @allure.title('Проверка: ввод почты и клик по кнопке «Восстановить»')
    @pytest.mark.parametrize("driver", ['chrome', 'firefox'])
    def test_enter_email_and_click_reset_button(self, request, driver):
        driver = request.getfixturevalue(driver)                              # setup
        main_page, login_page, reset_password_page = (                        # setup
            MainPage(driver), LoginPage(driver), ResetPasswordPage(driver))   # setup
        main_page.click_on_login_button()
        login_page.click_on_reset_password()
        reset_password_page.enter_email_and_press_reset()
        assert expected_conditions.visibility_of_element_located(ResetPasswordPageLocators.NEW_PASSWORD_INPUT)

    @allure.title('Проверка: клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    @pytest.mark.parametrize("driver", ['chrome', 'firefox'])
    def test_click_on_visibility_button_make_pass_input_field_active(self, request, driver):
        driver = request.getfixturevalue(driver)                              # setup
        main_page, login_page, reset_password_page = (                        # setup
            MainPage(driver), LoginPage(driver), ResetPasswordPage(driver))   # setup
        main_page.click_on_login_button()
        login_page.click_on_reset_password()
        reset_password_page.enter_new_password_flow()
        field = reset_password_page.click_pass_visibility_button_and_return_pass_input_field()
        assert 'active' in field.get_attribute('class')
