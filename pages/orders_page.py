import allure

from locators.main_page_locators import MainPageLocators, ConstructorPageLocators
from locators.orders_page_locators import OrdersPageLocators
from pages.base_page import BasePageSteps

class OrdersPageSteps(BasePageSteps):

    @allure.step('Ждем прогрузки кнопки Лента заказов в хэдере')
    def wait_clickability_orders_button_header(self):
        self.wait_clickability_button(MainPageLocators.BUTTON_ORDERS_PAGE)


    @allure.step('Ждем прогрузки счетчика заказов за все время')
    def wait_count_orders_total(self):
        self.wait_for_element(OrdersPageLocators.COUNTER_ORDERS_TOTAL)

    @allure.step('Ждем прогрузки кнопки подтверждения заказа')
    def wait_order_confirm_button(self):
        self.wait_for_element(ConstructorPageLocators.BUTTON_ORDER_CONFIRM)


    @allure.step('Находим номер заказа')
    def get_order_number(self):
        locator = ConstructorPageLocators.HEADER_ORDER_NUMBER

        def condition():
            text = self.get_text(locator)
            return text.isdigit() and int(text) > 9999
        self.wait_for_condition(condition)
        return self.get_text(locator)


    @allure.step('Находим число счетчика заказов за все время')
    def get_count_orders_total(self):
        locator = OrdersPageLocators.COUNTER_ORDERS_TOTAL
        return self.get_text(locator)

    @allure.step('Находим число счетчика заказов за день')
    def get_count_orders_by_day(self):
        locator = OrdersPageLocators.COUNTER_ORDERS_BY_DAY
        return self.get_text(locator)

    @allure.step('Находим наш заказ в листе ожидания')
    def get_order_number_in_list(self,order_number):
        locator = OrdersPageLocators.LIST_ORDERS_PREPARING

        def condition():
            text = self.get_text(locator)
            return text.isdigit() and order_number in text

        self.wait_for_condition(condition)

        return self.get_text(locator)

    @allure.step('Кликаем на кнопку Лента Заказов')
    def click_orders_button_header(self):
        self.click_on_element(MainPageLocators.BUTTON_ORDERS_PAGE)


    @allure.step('Кликаем на кнопку Конструктор в хэдере')
    def click_constructor_button_header(self):
        self.click_on_element(OrdersPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Ждем прогрузки заголовка СОберите бургер')
    def wait_constructor_header(self):
        self.wait_for_element(ConstructorPageLocators.HEADER_CONSTRUCTOR)

    @allure.step('Ждем прогрузки заголовка СОберите бургер')
    def wait_constructor_button(self):
        self.wait_for_element(MainPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Проверяем наличие заголовка Соберите бургер')
    def check_constructor_header(self):
        return self.check_is_displayed_element(ConstructorPageLocators.HEADER_CONSTRUCTOR)

    @allure.step('Добавляем ингредиент в корзину заказа')
    def drag_and_drop_ingredient_panel_to_bucket(self, index):
        self.drag_and_drop(MainPageLocators.INGREDIENT_PANEL[index], ConstructorPageLocators.BUTTON_ORDER_CONFIRM)


    @allure.step('Кликаем на кнопку подтвердить заказ')
    def click_order_confirm_button(self):
        self.click_on_element(ConstructorPageLocators.BUTTON_ORDER_CONFIRM)


    @allure.step('Кликаем на кнопку Лента Заказов')
    def click_orders_button_header(self):
        self.click_on_element(MainPageLocators.BUTTON_ORDERS_PAGE)


    @allure.step('Кликаем на кнопку закрытия попапа нового заказа')
    def close_popup_order(self):
        self.click_on_element(ConstructorPageLocators.BUTTON_CLOSE_ORDER_NUMBER)

    @allure.step('Ждем исчезновения оверлея')
    def wait_overlay_close(self):
        self.wait_element_disappeared(MainPageLocators.OVERLAY)