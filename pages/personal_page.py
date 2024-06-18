import allure

from pages.base_page import BasePage

from locators.personal_page_locators import PersonalPageLocators
from locators.login_page_locators import LoginPageLocators


class PersonalPage(BasePage):
    @allure.step("Проверяем, что открыт личный кабинет")
    def check_personal_page_is_displayed(self):
        return self.check_element_visible(PersonalPageLocators.ORDER_HISTORY)

    @allure.step("Клик на раздел «история заказов»")
    def click_on_order_history(self):
        self.click_and_wait_for_invisibility(
            PersonalPageLocators.ORDER_HISTORY, PersonalPageLocators.PASSWORD_FIELD)

    @allure.step("Возвращаем заголовок «история заказов»")
    def return_history_header(self):
        return self.return_element(PersonalPageLocators.ORDER_HISTORY)

    @allure.step("Возвращаем номер заказа из раздела «история заказов»")
    def return_order_number_from_history(self):
        number = self.get_text(PersonalPageLocators.TEST_ORDER_NUMBER)
        return number[2:]

    @allure.step("Клик на кнопку «Выйти»")
    def click_on_logout_button(self):
        self.click_and_wait_for(PersonalPageLocators.LOGOUT_BUTTON, LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Проверяем, что страница личного кабинета закрылась")
    def check_personal_page_is_closed(self):
        return self.check_element_invisible(PersonalPageLocators.ORDER_HISTORY)


