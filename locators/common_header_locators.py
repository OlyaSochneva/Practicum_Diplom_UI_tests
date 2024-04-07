from selenium.webdriver.common.by import By


class CommonHeaderLocators:
    # кнопка «Лента заказов»:
    FEED_BUTTON = By.XPATH, '// *[@href="/feed"]'

    # кнопка «Конструктор»:
    CONSTRUCTOR_BUTTON = By.XPATH, '//*[contains(text(), "Конструктор")]/parent::a'

    # кнопка «Личный кабинет»:
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, '//*[@href="/account"]'
