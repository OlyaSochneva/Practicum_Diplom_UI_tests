from pages.base_page import BasePage

from locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePage):
    def click_on_order(self, order):
        self.scroll_to_element(order)
        self.click_and_wait_for(order, FeedPageLocators.ORDER_POPUP_WINDOW)

    def create_order_locator(self, order_number):
        return self.create_locator(FeedPageLocators.FEED_ORDER_LOCATOR_TEMPLATE, order_number)

    def wait_my_order_and_return_progress_section(self, order_number):
        progress_section = self.create_locator(FeedPageLocators.PROGRESS_SECTION_TEMPLATE, order_number)
        return self.get_text(progress_section)

    def return_counter_value(self, counter_locator):
        value = self.get_text(counter_locator)
        return int(value)
