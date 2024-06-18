import requests
import string
import random

from data import URL


def build_random_order():
    buns_list = []
    main_list = []
    sauces_list = []
    response = requests.get(URL.INGREDIENTS).json()
    for ingredient in response['data']:
        if ingredient['type'] == 'bun':
            buns_list.append(ingredient['_id'])
        if ingredient['type'] == 'main':
            main_list.append(ingredient['_id'])
        if ingredient['type'] == 'sauce':
            sauces_list.append(ingredient['_id'])
    bun = random.choice(buns_list)
    main = random.choice(main_list)
    sauce = random.choice(sauces_list)
    random_order = [bun, main, sauce]
    return random_order


def return_order_number(response):
    body = response.json()
    number = (body['order'])['number']
    return str(number)


def new_user():
    payload = {
        "email": generate_random_email(),
        "password": generate_random_string(8),
        "name": generate_random_string(5)
    }
    return payload


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_random_email():
    email = generate_random_string(5)
    email += '_test@ya.ru'
    return email
