from selenium.webdriver.common.by import By


class FeedPageLocators:
    # заголовок «Лента заказов»:
    FEED_HEADER = By.XPATH, '//h1[text()="Лента заказов"]'

    # шаблон локатора заказа со стр «Лента заказов»:
    FEED_ORDER_LOCATOR_TEMPLATE = By.XPATH, '//p[text()="#0{}"]/ancestor::a'

    # всплывающее окно заказа:
    ORDER_POPUP_WINDOW = By.XPATH, '// div[contains(@class, "orderBox")]'

    # раздел «В работе»:
    PROGRESS_SECTION_TEMPLATE = By.XPATH, '// ul[contains(@class, "orderListReady")]/child::li[text()="{}"]'

    # счётчик «Выполнено за всё время» (значение):
    ALL_COMPLETED_COUNTER_VALUE = By.XPATH, '// p[text()="Выполнено за все время:"]/following-sibling::p'

    # счётчик «Выполнено за сегодня» (значение):
    TODAY_COMPLETED_COUNTER_VALUE = By.XPATH, '// p[text()="Выполнено за сегодня:"]/following-sibling::p'

