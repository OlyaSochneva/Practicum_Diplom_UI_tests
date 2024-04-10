import allure

from pages.base_page import BasePage

from locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePage):
    @allure.step("Проверяем, что открыта страница с лентой заказов")
    def check_feed_page_is_displayed(self):
        return self.check_element_visible(FeedPageLocators.FEED_HEADER)

    @allure.step("Клик на заказ")
    def click_on_order(self, order):
        self.scroll_to_element(order)
        self.click_and_wait_for(order, FeedPageLocators.ORDER_POPUP_WINDOW)
        self.anti_overlay_click()    # для Firefox

    @allure.step("Проверяем, что открылось поп-ап окно заказа")
    def check_order_popup_is_displayed(self):
        return self.check_element_visible(FeedPageLocators.ORDER_POPUP_WINDOW)

    @allure.step("Собираем уникальный локатор заказа")
    def create_order_locator(self, order_number):
        return self.create_locator(FeedPageLocators.FEED_ORDER_LOCATOR_TEMPLATE, order_number)

    @allure.step("Проверяем, что заказ отображается")
    def check_order_is_displayed(self, order_locator):
        return self.check_element_visible(order_locator)

    @allure.step("Собираем локатор раздела «в работе» с номером заказа, возвращаем текст")
    def wait_my_order_and_return_progress_section(self, order_number):
        progress_section = self.create_locator(FeedPageLocators.PROGRESS_SECTION_TEMPLATE, order_number)
        return self.get_text(progress_section)

    @allure.step("Возвращаем текущее значение счётчика (int)")
    def return_counter_value(self, counter_locator):
        value = self.get_text(counter_locator)
        return int(value)
