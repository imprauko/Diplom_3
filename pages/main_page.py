import allure
from locators.main_page_locators import MainPageLocators, ConstructorPageLocators
from locators.orders_page_locators import OrdersPageLocators
from pages.base_page import BasePageSteps


class MainPageSteps(BasePageSteps):
    @allure.step('Ждем прогрузки панели ингредиента')
    def wait_ingredient_panel(self,index):
        self.wait_for_element(MainPageLocators.INGREDIENT_PANEL[index])

    @allure.step('Ждем закрытия попапа')
    def wait_popup_close(self):
        self.wait_element_disappeared(MainPageLocators.BUTTON_CLOSE_DETAILS)


    @allure.step('Проскролливаем до панели ингредиента')
    def scroll_ingredient_panel(self, index):
        self.scroll_to_element(MainPageLocators.INGREDIENT_PANEL[index])

    @allure.step('Кликаем на панель ингредиента')
    def click_ingredient_panel(self, index):
        self.click_on_element(MainPageLocators.INGREDIENT_PANEL[index])

    @allure.step('Ждем прогрузки Заголовка деталей ингредиента')
    def wait_ingredient_details(self):
        self.wait_for_element(MainPageLocators.HEADER_DETAILS)

    @allure.step('Ждем исчезновения Заголовка деталей ингредиента')
    def wait_ingredient_details_close_header(self):
        self.wait_element_disappeared(MainPageLocators.HEADER_DETAILS)

    @allure.step('Ждем прогрузки кнопки закрытия деталей ингредиента')
    def wait_ingredient_details_close_button(self):
        self.wait_for_element(MainPageLocators.BUTTON_CLOSE_DETAILS)

    @allure.step('Кликаем на кнопку закрытия деталей ингредиента')
    def click_ingredient_details_close_button(self):
        self.click_on_element(MainPageLocators.BUTTON_CLOSE_DETAILS)

    @allure.step('Проверяем наличие заголовка Детали ингредиента')
    def check_ingredient_details(self):
        return self.check_is_displayed_element(MainPageLocators.HEADER_DETAILS)

    @allure.step('Ждем прогрузки кнопки Лента заказов в хэдере')
    def wait_clickability_orders_button_header(self):
        self.wait_clickability_button(MainPageLocators.BUTTON_ORDERS_PAGE)

    @allure.step('Кликаем на кнопку Лента Заказов')
    def click_orders_button_header(self):
        self.click_on_element(MainPageLocators.BUTTON_ORDERS_PAGE)

    @allure.step('Ждем прогрузки заголовка Лента заказов')
    def wait_orders_feed_header(self):
        self.wait_for_element(OrdersPageLocators.HEADER_ORDERS)

    @allure.step('Проверяем наличие заголовка Лента заказов')
    def check_orders_feed_header(self):
        return self.check_is_displayed_element(OrdersPageLocators.HEADER_ORDERS)

    @allure.step('Находим число счетчика ингредиента')
    def get_count_number(self, index):
        locator = MainPageLocators.INGREDIENT_PANEL_COUNTER[index]
        return self.get_text(locator)

    @allure.step('Ждем прогрузки счетчика панели ингредиента')
    def wait_ingredient_panel_counter(self, index):
        self.wait_for_element(MainPageLocators.INGREDIENT_PANEL_COUNTER[index])

    @allure.step('Добавляем ингредиент в корзину заказа')
    def drag_and_drop_ingredient_panel_to_bucket(self, index):
        self.drag_and_drop(MainPageLocators.INGREDIENT_PANEL[index], ConstructorPageLocators.BUTTON_ORDER_CONFIRM)