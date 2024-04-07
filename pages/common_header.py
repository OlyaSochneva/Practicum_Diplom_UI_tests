from pages.base_page import BasePage

from locators.common_header_locators import CommonHeaderLocators
from locators.main_page_locators import MainPageLocators
from locators.feed_page_locators import FeedPageLocators


class CommonHeader(BasePage):
    def click_on_personal_account_button(self):
        self.anti_overlay_click()   # для Firefox
        self.click_and_wait_for_invisibility(
            CommonHeaderLocators.PERSONAL_ACCOUNT_BUTTON, MainPageLocators.MENU_HEADER)
        self.anti_overlay_click()   # для Firefox

    def click_on_constructor(self):
        self.click_and_wait_for(CommonHeaderLocators.CONSTRUCTOR_BUTTON, MainPageLocators.MENU_HEADER)

    def click_on_order_feed(self):
        self.anti_overlay_click()   # для Firefox
        self.click_and_wait_for(CommonHeaderLocators.FEED_BUTTON, FeedPageLocators.FEED_HEADER)


