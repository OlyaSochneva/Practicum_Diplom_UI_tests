from selenium.webdriver.common.by import By


class MainPageLocators:
    # кнопка «Войти в аккаунт»
    LOGIN_BUTTON = By.XPATH, '//button[text()="Войти в аккаунт"]'

    # заголовок главной страницы «Соберите бургер»
    MENU_HEADER = By.XPATH, '//h1[text()="Соберите бургер"]'

    # всплывающее окно ингредиента
    INGR_POPUP_WINDOW_HEADER = By.XPATH, '//h2[text()="Детали ингредиента"]'

    # кнопка закрытия всплывающего окна
    POPUP_WINDOW_CLOSE_BUTTON = By.XPATH, '//button[contains(@class, "close")]'

    # шаблон для локатора ингредиента:
    INGREDIENT_LOCATOR_TEMPLATE = By.XPATH, '// a[@href="/ingredient/{}"]'

    # шаблон для локатора счётчика ингредиента
    INGR_COUNTER_LOCATOR_TEMPLATE = By.XPATH, '{}/child::div/child::p[contains(@class, "counter")]'

    # корзина
    BASKET = By.XPATH, '// section[contains(@class, "basket")]'

    # кнопка «Оформить заказ»
    ORDER_BUTTON = By.XPATH, '// button[text()="Оформить заказ"]'

    # всплывающее окно о создании заказа:
    ORDER_CREATION_POPUP_WINDOW = By.XPATH, '// p[text()="идентификатор заказа"]'

