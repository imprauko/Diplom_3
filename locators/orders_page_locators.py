from selenium.webdriver.common.by import By


class OrdersPageLocators:
    BUTTON_CONSTRUCTOR = (By.XPATH, '//a[.//p[text()="Конструктор"]]')  # Кнопка "Конструктор"

    HEADER_ORDERS = (By.XPATH, '//h1[text()="Лента заказов"]')  # Заголовок "Лента заказов"
    COUNTER_ORDERS_TOTAL = (By.XPATH, '//div[@class="undefined mb-15"]/p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')  # Счетчик заказов всего
    COUNTER_ORDERS_BY_DAY = (By.XPATH,
                           '//div[3]/p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')  # Счетчик заказов за день
    LIST_ORDERS_PREPARING = (By.XPATH,
                            '//ul[contains(@class, "OrderFeed_orderListReady")]/li[contains(@class, "text_type_digits-default")]') # Список заказов "в работе"
