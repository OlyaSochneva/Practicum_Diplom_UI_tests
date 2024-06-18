import allure

from pages.base_page import BasePage

from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators

from assistant_methods import build_random_order


class MainPage(BasePage):
    @allure.step("Проверяем, что открыта главная страница")
    def check_main_page_is_displayed(self):
        return self.check_element_visible(MainPageLocators.MENU_HEADER)

    @allure.step("Клик на кнопку «Войти в аккаунт»")
    def click_on_login_button(self):
        self.anti_overlay_click()   # для Firefox
        self.click_and_wait_for(MainPageLocators.LOGIN_BUTTON, LoginPageLocators.RESET_PASSWORD_BUTTON)

    @allure.step("Клик на ингредиент")
    def click_on_ingredient(self, ingredient):
        self.anti_overlay_click()    # для Firefox
        self.scroll_to_element(ingredient)
        self.click_and_wait_for(ingredient, MainPageLocators.INGR_POPUP_WINDOW_HEADER)

    @allure.step("Проверяем, что открылось поп-ап окно ингредиента")
    def check_ingr_popup_is_displayed(self):
        return self.check_element_visible(MainPageLocators.INGR_POPUP_WINDOW_HEADER)

    @allure.step("Закрываем поп-ап окно ингредиента (клик на «крестик»)")
    def close_ingr_popup_window(self):
        self.click_and_wait_for_invisibility(
            MainPageLocators.POPUP_WINDOW_CLOSE_BUTTON, MainPageLocators.INGR_POPUP_WINDOW_HEADER)

    @allure.step("Проверяем, что поп-ап окно ингредиента закрылось")
    def check_ingr_popup_window_closed(self):
        return self.check_element_invisible(MainPageLocators.INGR_POPUP_WINDOW_HEADER)

    @allure.step("Добавляем ингредиент в корзину")
    def add_to_basket(self, ingredient_locator):
        dragged = self.scroll_and_return(ingredient_locator)
        target = self.scroll_and_return(MainPageLocators.BASKET)
        self.drag_and_drop(dragged, target)

    @allure.step("Возвращаем текущее значение счётчика ингредиента")
    def return_ingr_counter_value(self, ingredient_locator):
        method, locator = ingredient_locator
        ingr_counter_locator = self.create_locator(MainPageLocators.INGR_COUNTER_LOCATOR_TEMPLATE, locator)
        return self.get_text(ingr_counter_locator)

    @allure.step("Добавляем в корзину случайный заказ")
    def add_random_order_to_basket(self):
        order = build_random_order()
        for ingredient_id in order:
            ingredient = self.create_locator(
                MainPageLocators.INGREDIENT_LOCATOR_TEMPLATE, ingredient_id)
            self.add_to_basket(ingredient)

    @allure.step("Нажимаем на кнопку «Заказать»")
    def click_on_order_button(self):
        self.click_and_wait_for(MainPageLocators.ORDER_BUTTON, MainPageLocators.ORDER_CREATION_POPUP_WINDOW)

    @allure.step("Проверяем, что открылось поп-ап окно о создании заказа")
    def order_creation_popup_window_is_displayed(self):
        return self.check_element_visible(MainPageLocators.ORDER_CREATION_POPUP_WINDOW)


