import pytest
import requests

from selenium import webdriver

from data import URL

from assistant_methods import new_user
from assistant_methods import build_random_order
from assistant_methods import return_order_number


@pytest.fixture(scope="function")
def test_user():
    user = {}
    email_pass = {}
    payload = new_user()
    requests.post(URL.REGISTRATION, data=payload, timeout=10)
    email_pass['email'] = payload['email']
    email_pass['password'] = payload['password']
    response = requests.post(URL.LOGIN, data=email_pass, timeout=10)
    token = response.json()['accessToken']
    user['token'] = token
    user['email_pass'] = email_pass
    yield user  # email_pass и токен
    requests.delete(URL.USER, headers={'Authorization': token})


@pytest.fixture(scope="function")
def order_payload():
    payload = {"ingredients": build_random_order()}
    return payload


@pytest.fixture(scope="function")
def create_order_and_return_number(test_user, order_payload):
    response = requests.post(URL.ORDERS, headers={'Authorization': test_user['token']},
                             data=order_payload, timeout=10)
    number = return_order_number(response)
    return number


@pytest.fixture(scope="function")
def chrome():
    my_options = webdriver.ChromeOptions()
    my_options.add_argument("--window-size=1920,1080")
    my_options.add_argument("--disable-web-security")
    my_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=my_options)
    driver.get(URL.MAIN_PAGE)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def firefox():
    my_options = webdriver.FirefoxOptions()
    my_options.add_argument("--width=1920")
    my_options.add_argument("--height=1080")
    my_options.set_preference('dom.webnotifications.enabled', False)
    driver = webdriver.Firefox(options=my_options)
    driver.get(URL.MAIN_PAGE)
    yield driver
    driver.quit()
