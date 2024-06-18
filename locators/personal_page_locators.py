from selenium.webdriver.common.by import By


class PersonalPageLocators:
    # кнопка «История заказов»:
    ORDER_HISTORY = By.XPATH, '//a[text()="История заказов"]'

    # номер заказа в разделе «История заказов»:
    TEST_ORDER_NUMBER = By.XPATH, '// div[contains(@class, "textBox")]/child::p[contains(@class, "digits")]'

    # кнопка «Выход»:
    LOGOUT_BUTTON = By.XPATH, '//button[text()="Выход"]'

    # поле редактирования пароля:
    PASSWORD_FIELD = By.XPATH, '//input[@type="password"]'
