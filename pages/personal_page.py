from pages.base_page import BasePage

from locators.personal_page_locators import PersonalPageLocators
from locators.login_page_locators import LoginPageLocators


class PersonalPage(BasePage):
    def click_on_logout_button(self):
        self.click_and_wait_for(PersonalPageLocators.LOGOUT_BUTTON, LoginPageLocators.LOGIN_BUTTON)

    def click_on_order_history(self):
        self.click_and_wait_for_invisibility(
            PersonalPageLocators.ORDER_HISTORY, PersonalPageLocators.PASSWORD_FIELD)

    def return_order_number_from_history(self):
        number = self.get_text(PersonalPageLocators.TEST_ORDER_NUMBER)
        return number[2:]


