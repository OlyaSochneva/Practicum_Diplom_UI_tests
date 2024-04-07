import pytest
import requests
import allure

from selenium.webdriver.support import expected_conditions

from pages.common_header import CommonHeader
from pages.feed_page import FeedPage
from pages.login_page import LoginPage

from locators.feed_page_locators import FeedPageLocators
from pages.personal_page import PersonalPage


class TestFeedPage:
    @allure.title('Проверка: переход по клику на «Лента заказов»')
    @pytest.mark.parametrize("driver", ['chrome', 'firefox'])
    def test_move_to_order_feed_page(self, request, driver):
        driver = request.getfixturevalue(driver)     # setup
        common_header = CommonHeader(driver)         # setup
        common_header.click_on_order_feed()
        assert expected_conditions.visibility_of_element_located(FeedPageLocators.FEED_HEADER)

    @allure.title('Проверка: если кликнуть на заказ, откроется всплывающее окно с деталями')
    @pytest.mark.parametrize("driver", ['chrome', 'firefox'])
    def test_open_order_popup_window_by_click_on_order(
            self, request, driver, create_order_and_return_number):
        driver = request.getfixturevalue(driver)                            # setup
        common_header, feed_page = CommonHeader(driver), FeedPage(driver)   # setup
        order_number = create_order_and_return_number
        order = feed_page.create_order_locator(order_number)
        common_header.click_on_order_feed()
        feed_page.refresh()
        feed_page.click_on_order(order)
        assert expected_conditions.visibility_of_element_located(FeedPageLocators.ORDER_POPUP_WINDOW)

    @allure.title('Проверка: заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    @pytest.mark.parametrize("driver", ['chrome', 'firefox'])
    def test_users_order_from_order_history_displayed_in_feed_page(
            self, request, driver, test_user, create_order_and_return_number):
        driver = request.getfixturevalue(driver)                                              # setup
        common_header, login_page, personal_page, feed_page = (                               # setup
            CommonHeader(driver), LoginPage(driver), PersonalPage(driver), FeedPage(driver))  # setup
        common_header.click_on_personal_account_button()
        login_page.login(test_user['email_pass'])
        common_header.click_on_personal_account_button()
        personal_page.click_on_order_history()
        order_number = personal_page.return_order_number_from_history()
        common_header.click_on_order_feed()
        my_order = feed_page.create_order_locator(order_number)
        assert expected_conditions.visibility_of_element_located(my_order)

    @allure.title('Проверка: при создании нового заказа счётчики Выполнено за всё время '
                  'и Выполнено за сегодня увеличиваются')
    @pytest.mark.parametrize("driver, counter",
                             [('chrome', FeedPageLocators.ALL_COMPLETED_COUNTER_VALUE),
                              ('chrome', FeedPageLocators.TODAY_COMPLETED_COUNTER_VALUE),
                              ('firefox', FeedPageLocators.ALL_COMPLETED_COUNTER_VALUE),
                              ('firefox', FeedPageLocators.TODAY_COMPLETED_COUNTER_VALUE)
                              ])
    def test_completed_counters_increases_with_new_order(
            self, request, driver, counter, test_user, order_payload):
        driver = request.getfixturevalue(driver)                             # setup
        common_header, feed_page = CommonHeader(driver), FeedPage(driver)    # setup
        common_header.click_on_order_feed()
        before = feed_page.return_counter_value(counter)
        requests.post('https://stellarburgers.nomoreparties.site/api/orders',
                      headers={'Authorization': test_user["token"]}, data=order_payload, timeout=10)
        after = feed_page.return_counter_value(counter)
        assert after == (before + 1)

    @allure.title('Проверка: после оформления заказа его номер появляется в разделе В работе')
    @pytest.mark.parametrize("driver", ['chrome', 'firefox'])
    def test_new_order_number_appears_in_progress_section(self, request, driver, create_order_and_return_number):
        driver = request.getfixturevalue(driver)                            # setup
        common_header, feed_page = CommonHeader(driver), FeedPage(driver)   # setup
        order_number = create_order_and_return_number
        common_header.click_on_order_feed()
        progress_section = feed_page.wait_my_order_and_return_progress_section(order_number)
        assert order_number in progress_section
