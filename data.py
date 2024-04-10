from selenium.webdriver.common.by import By


class URL:
    MAIN_PAGE = 'https://stellarburgers.nomoreparties.site'
    REGISTRATION = MAIN_PAGE + '/api/auth/register'  # регистрация
    LOGIN = MAIN_PAGE + '/api/auth/login'  # логин
    USER = MAIN_PAGE + '/api/auth/user'  # получить/изменить/удалить пользователя
    ORDERS = MAIN_PAGE + '/api/orders'  # создать заказ
    INGREDIENTS = MAIN_PAGE + '/api/ingredients'  # список всех ингредиентов


# тест. ингредиент (соус Spicy-X) для тестов всплывающего окна с информацией и теста на счётчик ингредиента
# мне кажется ок сделать его глобальной переменной и оставить тут для тестов, чтобы было легко поменять
TEST_INGREDIENT = By.XPATH, '// a[@href="/ingredient/61c0c5a71d1f82001bdaaa72"]'
