import pytest
import allure

from selenium.webdriver.support import expected_conditions

from pages.common_header import CommonHeader
from pages.main_page import MainPage
from pages.login_page import LoginPage

from locators.main_page_locators import MainPageLocators


class TestMainPage:
    @allure.title('Проверка: переход по клику на «Конструктор»')
    @pytest.mark.parametrize("driver", ['chrome', 'firefox'])
    def test_move_to_constructor_section(self, request, driver):
        driver = request.getfixturevalue(driver)    # setup
        common_header = CommonHeader(driver)        # setup
        common_header.click_on_order_feed()
        common_header.click_on_constructor()
        assert expected_conditions.visibility_of_element_located(MainPageLocators.MENU_HEADER)

    @allure.title('Проверка: если кликнуть на ингредиент, появится всплывающее окно с деталями')
    @pytest.mark.parametrize("driver", ['chrome', 'firefox'])
    def test_open_popup_window_by_click_on_ingredient(self, request, driver):
        driver = request.getfixturevalue(driver)       # setup
        main_page = MainPage(driver)                   # setup
        main_page.click_on_ingredient(MainPageLocators.TEST_INGREDIENT)
        assert expected_conditions.visibility_of_element_located(
            MainPageLocators.INGR_POPUP_WINDOW_HEADER)

    @allure.title('Проверка: всплывающее окно закрывается кликом по крестику')
    @pytest.mark.parametrize("driver", ['chrome', 'firefox'])
    def test_closing_ingredient_popup_window(self, request, driver):
        driver = request.getfixturevalue(driver)       # setup
        main_page = MainPage(driver)                   # setup
        main_page.click_on_ingredient(MainPageLocators.TEST_INGREDIENT)
        main_page.close_ingr_popup_window()
        assert expected_conditions.invisibility_of_element_located(
            MainPageLocators.INGR_POPUP_WINDOW_HEADER)

    @allure.title('Проверка: при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    @allure.description('(!) Не работает в firefox')
    def test_ingredient_counter_increased_after_adding_in_the_order(self, chrome):
        main_page = MainPage(chrome)      # setup
        main_page.add_to_basket(MainPageLocators.TEST_INGREDIENT)
        counter = main_page.return_ingr_counter_value(MainPageLocators.TEST_INGREDIENT)
        assert counter == "1"

    @allure.title('Проверка: залогиненный пользователь может оформить заказ')
    @allure.description('(!) Не работает в firefox')
    def test_authorised_user_can_make_order(self, chrome, test_user):
        main_page, login_page = MainPage(chrome), LoginPage(chrome)     # setup
        main_page.click_on_login_button()
        login_page.login(test_user['email_pass'])
        main_page.add_random_order_to_basket()
        main_page.click_on_order_button()
        assert expected_conditions.visibility_of_element_located(
            MainPageLocators.ORDER_CREATION_POPUP_WINDOW)
