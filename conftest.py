import pytest
import requests

from selenium import webdriver

from assistant_methods import new_user
from assistant_methods import build_random_order
from assistant_methods import return_order_number


@pytest.fixture(scope="function")
def test_user():
    user = {}
    email_pass = {}
    payload = new_user()
    requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=payload, timeout=10)
    email_pass['email'] = payload['email']
    email_pass['password'] = payload['password']
    response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/login',
                             data=email_pass, timeout=10)
    token = response.json()['accessToken']
    user['token'] = token
    user['email_pass'] = email_pass
    yield user  # email_pass и токен
    requests.delete('https://stellarburgers.nomoreparties.site/api/auth/user', headers={'Authorization': token})


@pytest.fixture(scope="function")
def order_payload():
    payload = {"ingredients": build_random_order()}
    return payload


@pytest.fixture(scope="function")
def create_order_and_return_number(test_user, order_payload):
    response = requests.post('https://stellarburgers.nomoreparties.site/api/orders',
                             headers={'Authorization': test_user['token']}, data=order_payload, timeout=10)
    number = return_order_number(response)
    return number


@pytest.fixture(scope="function")
def chrome():
    my_options = webdriver.ChromeOptions()
    service = webdriver.ChromeService(executable_path="./chromedriver")
    my_options.add_argument("--window-size=1920,1080")
    my_options.add_argument("--disable-web-security")
    my_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=my_options, service=service)
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def firefox():
    my_options = webdriver.FirefoxOptions()
    service = webdriver.FirefoxService(executable_path="./firefoxdriver")
    my_options.add_argument("--width=1920")
    my_options.add_argument("--height=1080")
    my_options.set_preference('dom.webnotifications.enabled', False)
    driver = webdriver.Firefox(options=my_options, service=service)
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()
