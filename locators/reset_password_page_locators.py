from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    # поле ввода почты:
    EMAIL_INPUT = By.XPATH, '//input[@name="name"]'

    # кнопка «Восстановить»:
    RESET_BUTTON = By.XPATH, '//button[text()="Восстановить"]'

    # поле ввода нового пароля (сам input):
    NEW_PASSWORD_INPUT = By.XPATH, '//input[@name="Введите новый пароль"]'

    # поле ввода нового пароля (весь объект):
    NEW_PASSWORD_INPUT_FIELD = By.XPATH, '//input[@name="Введите новый пароль"]/parent::div'

    # кнопка видимости пароля:
    PASSWORD_VISIBILITY_BUTTON = By.XPATH, '//div[contains(@class, "icon")]'

