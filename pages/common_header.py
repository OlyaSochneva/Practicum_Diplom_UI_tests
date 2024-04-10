import allure

from pages.base_page import BasePage

from locators.common_header_locators import CommonHeaderLocators
from locators.main_page_locators import MainPageLocators
from locators.feed_page_locators import FeedPageLocators


class CommonHeader(BasePage):
    @allure.step("Клик на кнопку «Личный кабинет»")
    def click_on_personal_account_button(self):
        self.anti_overlay_click()   # для Firefox
        self.click_and_wait_for_invisibility(
            CommonHeaderLocators.PERSONAL_ACCOUNT_BUTTON, MainPageLocators.MENU_HEADER)
        self.anti_overlay_click()   # для Firefox

    @allure.step("Клик на раздел «Конструктор»")
    def click_on_constructor(self):
        self.click_and_wait_for(CommonHeaderLocators.CONSTRUCTOR_BUTTON, MainPageLocators.MENU_HEADER)

    @allure.step("Клик на раздел «Лента заказов»")
    def click_on_order_feed(self):
        self.anti_overlay_click()   # для Firefox
        self.click_and_wait_for(CommonHeaderLocators.FEED_BUTTON, FeedPageLocators.FEED_HEADER)


