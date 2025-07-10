import allure
from locators.main_page_locators import MainPageLocators, ConstructorPageLocators
from locators.orders_page_locators import OrdersPageLocators
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePageSteps


class ProfilePageSteps(BasePageSteps):

    @allure.step('Ждем кликабельности кнопки Личный кабинет в хэдере')
    def wait_clickability_profile_button_header(self):
        self.wait_clickability_button(MainPageLocators.BUTTON_ACCOUNT_MAIN_PAGE)

    @allure.step('Кликаем на кнопку Личный кабинет')
    def click_profile_button_header(self):
        self.click_on_element(MainPageLocators.BUTTON_ACCOUNT_MAIN_PAGE)

    @allure.step('Ждем прогрузки кнопки Лента заказов в хэдере')
    def wait_orders_button_header(self):
        self.wait_for_element(MainPageLocators.BUTTON_ORDERS_PAGE)

    @allure.step('Ждем кликабельности кнопки Лента заказов в хэдере')
    def wait_clickability_orders_button_header(self):
        self.wait_clickability_button(MainPageLocators.BUTTON_ORDERS_PAGE)

    @allure.step('Ждем прогрузки кнопки Лента заказов в хэдере')
    def wait_clickability_logout_button(self):
        self.wait_clickability_button(ProfilePageLocators.BUTTON_LOGOUT)

    @allure.step('Ждем исчезновения оверлея')
    def wait_overlay_close(self):
        self.wait_element_disappeared(MainPageLocators.OVERLAY)


    @allure.step('Кликаем на кнопку Лента Заказов')
    def click_orders_button_header(self):
        self.click_on_element(MainPageLocators.BUTTON_ORDERS_PAGE)

    @allure.step('Ждем прогрузки заголовка Лента заказов')
    def wait_orders_feed_header(self):
        self.wait_for_element(OrdersPageLocators.HEADER_ORDERS)

    @allure.step('Проверяем наличие заголовка Лента заказов')
    def check_orders_feed_header(self):
        return self.check_is_displayed_element(OrdersPageLocators.HEADER_ORDERS)


    @allure.step('Ждем прогрузки заголовка Лента заказов')
    def wait_orders_feed_header(self):
        self.wait_for_element(OrdersPageLocators.HEADER_ORDERS)

    @allure.step('Кликаем на кнопку Конструктор в хэдере')
    def click_constructor_button(self):
        self.click_on_element(OrdersPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Ждем прогрузки кнопки конструктора')
    def wait_constructor_button(self):
        self.wait_for_element(MainPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Ждем кликабельности кнопки конструктора')
    def wait_constructor_button_clickability(self):
        self.wait_clickability_button(MainPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Ждем прогрузки заголовка СОберите бургер')
    def wait_constructor_header(self):
        self.wait_for_element(ConstructorPageLocators.HEADER_CONSTRUCTOR)

    @allure.step('Проверяем наличие заголовка Соберите бургер')
    def check_constructor_header(self):
        return self.check_is_displayed_element(ConstructorPageLocators.HEADER_CONSTRUCTOR)