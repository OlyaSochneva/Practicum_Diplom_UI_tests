from selenium.webdriver.common.by import By


class LoginPageLocators:
    # кнопка «Восстановить пароль»:
    RESET_PASSWORD_BUTTON = By.XPATH, '// a[@href="/forgot-password"]'

    # поле ввода почты:
    EMAIL_INPUT = By.NAME, 'name'

    # поле ввода пароля:
    PASSWORD_INPUT = By.NAME, 'Пароль'

    # кнопка «Войти»
    LOGIN_BUTTON = By.XPATH, '//button[text()="Войти"]'
