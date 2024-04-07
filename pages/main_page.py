from selenium.webdriver import ActionChains

from pages.base_page import BasePage

from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators
from assistant_methods import build_random_order


class MainPage(BasePage):
    def click_on_login_button(self):
        self.anti_overlay_click()   # для Firefox
        self.click_and_wait_for(MainPageLocators.LOGIN_BUTTON, LoginPageLocators.RESET_PASSWORD_BUTTON)

    def click_on_ingredient(self, ingredient):
        self.anti_overlay_click()    # для Firefox
        self.scroll_to_element(ingredient)
        self.click_and_wait_for(ingredient, MainPageLocators.INGR_POPUP_WINDOW_HEADER)

    def close_ingr_popup_window(self):
        self.click_and_wait_for_invisibility(
            MainPageLocators.POPUP_WINDOW_CLOSE_BUTTON, MainPageLocators.INGR_POPUP_WINDOW_HEADER)

    def add_to_basket(self, ingredient_locator):
        dragged = self.scroll_and_return(ingredient_locator)
        target = self.scroll_and_return(MainPageLocators.BASKET)
        action = ActionChains(self.driver)
        action.drag_and_drop(dragged, target).pause(1).perform()

    def return_ingr_counter_value(self, ingredient_locator):
        method, locator = ingredient_locator
        ingr_counter_locator = self.create_locator(MainPageLocators.INGR_COUNTER_LOCATOR_TEMPLATE, locator)
        return self.get_text(ingr_counter_locator)

    def add_random_order_to_basket(self):
        order = build_random_order()
        for ingredient_id in order:
            ingredient = self.create_locator(
                MainPageLocators.INGREDIENT_LOCATOR_TEMPLATE, ingredient_id)
            self.add_to_basket(ingredient)

    def click_on_order_button(self):
        self.click_and_wait_for(MainPageLocators.ORDER_BUTTON, MainPageLocators.ORDER_CREATION_POPUP_WINDOW)

