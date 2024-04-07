import pytest
import allure

from selenium.webdriver.support import expected_conditions

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.common_header import CommonHeader
from pages.personal_page import PersonalPage

from locators.login_page_locators import LoginPageLocators
from locators.personal_page_locators import PersonalPageLocators


class TestPersonalPage:
    @allure.title('Проверка: переход по клику на «Личный кабинет»')
    @pytest.mark.parametrize("driver", ['chrome', 'firefox'])
    def test_move_to_personal_account_by_click_on_button(self, request, driver, test_user):
        driver = request.getfixturevalue(driver)                                # setup
        common_header, login_page = CommonHeader(driver), LoginPage(driver)     # setup
        common_header.click_on_personal_account_button()
        login_page.login(test_user['email_pass'])
        common_header.click_on_personal_account_button()
        assert expected_conditions.visibility_of_element_located(PersonalPageLocators.ORDER_HISTORY)

    @allure.title('Проверка: переход в раздел «История заказов»')
    @pytest.mark.parametrize("driver", ['chrome', 'firefox'])
    def test_move_to_order_history_section(self, request, driver, test_user):
        driver = request.getfixturevalue(driver)                             # setup
        common_header, login_page, personal_page = (                         # setup
            CommonHeader(driver), LoginPage(driver), PersonalPage(driver))   # setup
        common_header.click_on_personal_account_button()
        login_page.login(test_user['email_pass'])
        common_header.click_on_personal_account_button()
        personal_page.click_on_order_history()
        history_header = personal_page.return_element(PersonalPageLocators.ORDER_HISTORY)
        assert '_active_' in history_header.get_attribute('class')

    @allure.title('Проверка: выход из аккаунта')
    @pytest.mark.parametrize("driver", ['chrome', 'firefox'])
    def test_logout_from_personal_account(self, request, driver, test_user):
        driver = request.getfixturevalue(driver)                             # setup
        common_header, login_page, personal_page = (                         # setup
            CommonHeader(driver), LoginPage(driver), PersonalPage(driver))   # setup
        common_header.click_on_personal_account_button()
        login_page.login(test_user['email_pass'])
        common_header.click_on_personal_account_button()
        personal_page.click_on_logout_button()
        assert expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
