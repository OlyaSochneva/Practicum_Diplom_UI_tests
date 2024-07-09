## QA Diplom_3

#### Тесты веб-приложения Stellar Burgers

Содержимое проекта:

**tests** - папка с тестами

**pages** - папка со страницами по модели РОМ

**locators** - папка с локаторами

**conftest.py** - файл с с фикстурами

**assistant_methods** - файл со вспомогательными методами (генераторы и тд)

**allure_results** - отчёты

**requirements.txt** - внешние зависимости
## Тесты
### main page

**test_move_to_constructor_section**

Проверка: переход по клику на «Конструктор»

Фикстуры: driver

Страницы и методы:

common_header: click_on_order_feed, click_on_constructor

**test_open_popup_window_by_click_on_ingredient**

Проверка: если кликнуть на ингредиент, появится всплывающее окно с деталями

Фикстуры: driver

Страницы и методы:

main_page: click_on_ingredient

**test_closing_ingredient_popup_window**

Проверка: всплывающее окно закрывается кликом по крестику

Фикстуры: driver

Страницы и методы:

main_page: click_on_ingredient, close_ingr_popup_window

**test_ingredient_counter_increased_after_adding_in_the_order**

Проверка: при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается

Фикстуры: chrome (не работает в firefox)

Страницы и методы:

main_page: add_to_basket, return_ingr_counter_value

**test_authorised_user_can_make_order**

Проверка: залогиненный пользователь может оформить заказ

Фикстуры: chrome (не работает в firefox), test_user

Страницы и методы:

main_page: click_on_login_button, add_random_order_to_basket, click_on_order_button

login_page: login

### reset_password_page

**test_move_to_reset_password_page_by_click_reset_password**

Проверка: переход на страницу восстановления пароля по кнопке «Восстановить пароль»

Фикстуры: driver

Страницы и методы:

main_page: click_on_login_button

login_page: click_on_reset_password

**test_enter_email_and_click_reset_button**

Проверка: ввод почты и клик по кнопке «Восстановить»

Фикстуры: driver

Страницы и методы:

main_page: click_on_login_button

login_page: click_on_reset_password

reset_password_page: enter_email_and_press_reset


**test_click_on_visibility_button_make_pass_input_field_active**

Проверка: клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его

Фикстуры: driver

Страницы и методы:

main_page: click_on_login_button

login_page: click_on_reset_password

reset_password_page: enter_new_password_flow, click_pass_visibility_button_and_return_pass_input_field

### personal_page
**test_move_to_personal_account_by_click_on_button**

Проверка: переход по клику на «Личный кабинет»

Фикстуры: driver, test_user

Страницы и методы:

common_header: click_on_personal_account_button

login_page: login

**test_move_to_order_history_section**

Проверка: переход в раздел «История заказов»

Фикстуры: driver, test_user

Страницы и методы:

common_header: click_on_personal_account_button

login_page: login

personal_page: click_on_order_history

**test_logout_from_personal_account**

Проверка: выход из аккаунта

Фикстуры: driver, test_user

Страницы и методы:

common_header: click_on_personal_account_button

login_page: login

personal_page: click_on_logout_button

### feed_page

**test_move_to_order_feed_page**

Проверка: переход по клику на «Лента заказов»

Фикстуры: driver

Страницы и методы:

common_header: click_on_order_feed

**test_open_order_popup_window_by_click_on_order**

Проверка: если кликнуть на заказ, откроется всплывающее окно с деталями

Фикстуры: driver, create_order_and_return_number

Страницы и методы:

common_header: click_on_order_feed

feed_page: create_order_locator, click_on_order

**test_users_order_from_order_history_displayed_in_feed_page**

Проверка: заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»

Фикстуры: driver, test_user, create_order_and_return_number

Страницы и методы:

common_header: click_on_personal_account_button, click_on_order_feed

login_page: login

personal_page: click_on_order_history, return_order_number_from_history

feed_page: create_order_locator

**test_completed_counters_increases_with_new_order**

Проверка: при создании нового заказа счётчики Выполнено за всё время и Выполнено за сегодня увеличиваются

Фикстуры: driver, test_user, order_payload

Параметры: локатор счётчика 

Страницы и методы:

common_header: click_on_order_feed

feed_page: return_counter_value

**test_new_order_number_appears_in_progress_section**

Проверка: после оформления заказа его номер появляется в разделе В работе

Фикстуры: driver, create_order_and_return_number

Страницы и методы:

common_header: click_on_order_feed

feed_page: wait_my_order_and_return_progress_section

### Фикстуры:
**chrome_driver** - инициализирует драйвер Chrome с разрешением 1920х1080

**firefox_driver** - инициализирует драйвер Firefox с разрешением 1920х1080

**test_user** - регистрирует нового пользователя, возвращает его почту, пароль и токен, потом удаляет его

**order_payload** - возвращает payload для создания заказа

Вспом. методы: build_random_order()

**create_order_and_return_number(test_user, order_payload)** - делает заказ и возвращает номер

Вспом. методы: return_order_number


