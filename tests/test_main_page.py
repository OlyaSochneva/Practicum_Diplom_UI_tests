import pytest
import allure

from pages.common_header import CommonHeader
from pages.main_page import MainPage
from pages.login_page import LoginPage

from data import TEST_INGREDIENT


class TestMainPage:
    @allure.title('Проверка: переход по клику на «Конструктор»')
    @pytest.mark.parametrize("driver", ['chrome', 'firefox'])
    def test_move_to_constructor_section(self, request, driver):
        driver = request.getfixturevalue(driver)  # setup
        common_header, main_page = CommonHeader(driver), MainPage(driver)  # setup
        common_header.click_on_order_feed()
        common_header.click_on_constructor()
        assert main_page.check_main_page_is_displayed()

    @allure.title('Проверка: если кликнуть на ингредиент, появится всплывающее окно с деталями')
    @pytest.mark.parametrize("driver", ['chrome', 'firefox'])
    def test_open_popup_window_by_click_on_ingredient(self, request, driver):
        driver = request.getfixturevalue(driver)  # setup
        main_page = MainPage(driver)  # setup
        main_page.click_on_ingredient(TEST_INGREDIENT)
        assert main_page.check_ingr_popup_is_displayed()

    @allure.title('Проверка: всплывающее окно закрывается кликом по крестику')
    @pytest.mark.parametrize("driver", ['chrome', 'firefox'])
    def test_closing_ingredient_popup_window(self, request, driver):
        driver = request.getfixturevalue(driver)  # setup
        main_page = MainPage(driver)  # setup
        main_page.click_on_ingredient(TEST_INGREDIENT)
        main_page.close_ingr_popup_window()
        assert main_page.check_ingr_popup_window_closed()

    @allure.title('Проверка: при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    @allure.description('(!) Не работает в firefox')
    def test_ingredient_counter_increased_after_adding_in_the_order(self, chrome):
        main_page = MainPage(chrome)  # setup
        main_page.add_to_basket(TEST_INGREDIENT)
        counter = main_page.return_ingr_counter_value(TEST_INGREDIENT)
        assert counter == "1"

    @allure.title('Проверка: залогиненный пользователь может оформить заказ')
    @allure.description('(!) Не работает в firefox')
    def test_authorised_user_can_make_order(self, chrome, test_user):
        main_page, login_page = MainPage(chrome), LoginPage(chrome)  # setup
        main_page.click_on_login_button()
        login_page.login(test_user['email_pass'])
        main_page.add_random_order_to_basket()
        main_page.click_on_order_button()
        assert main_page.order_creation_popup_window_is_displayed()
