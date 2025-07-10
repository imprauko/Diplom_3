import allure

from pages.main_page import MainPageSteps
from pages.orders_page import OrdersPageSteps
from pages.profile_page import ProfilePageSteps


class TestButtonTranspassClick:
    @allure.title(
        'Проверяем переход на страницу листа заказов через кнопку на главной странице')
    @allure.description(
        'переход на страницу заказов через кнопку в хэдере')
    def test_orders_feed_button_from_main(self, setup_logged_in):
        main_page = MainPageSteps(setup_logged_in)
        main_page.wait_popup_close()
        main_page.wait_clickability_orders_button_header()
        main_page.click_orders_button_header()
        main_page.wait_orders_feed_header()
        assert main_page.check_orders_feed_header()

    @allure.title(
        'Проверяем переход на страницу листа заказов через кнопку на странице Личный кабинет')
    @allure.description(
        'переход на страницу заказов через кнопку в хэдере')
    def test_orders_feed_button_from_profile(self, setup_logged_in):
        main_page = ProfilePageSteps(setup_logged_in)
        main_page.wait_clickability_profile_button_header()
        main_page.click_profile_button_header()
        main_page.wait_orders_button_header()
        main_page.wait_overlay_close()
        main_page.wait_clickability_orders_button_header()
        main_page.wait_clickability_logout_button()
        main_page.click_orders_button_header()
        main_page.wait_orders_feed_header()
        assert main_page.check_orders_feed_header()

    @allure.title(
        'Проверяем переход на страницу конструктора через кнопку на странице листа заказов')
    @allure.description(
        'переход на страницу конструктора через кнопку в хэдере')
    def test_constructor_button_from_feed(self, setup_logged_in):
        main_page = OrdersPageSteps(setup_logged_in)
        main_page.wait_clickability_orders_button_header()
        main_page.click_orders_button_header()
        main_page.wait_constructor_button()
        main_page.click_constructor_button_header()
        main_page.wait_constructor_header()
        assert main_page.check_constructor_header()

    @allure.title(
        'Проверяем переход на страницу конструктора через кнопку на странице Личный кабинет')
    @allure.description(
        'переход на страницу конструктора через кнопку в хэдере')
    def test_constructor_button_from_profile(self, setup_logged_in):
        main_page = ProfilePageSteps(setup_logged_in)
        main_page.wait_clickability_profile_button_header()
        main_page.click_profile_button_header()
        main_page.wait_constructor_button()
        main_page.wait_overlay_close()
        main_page.wait_constructor_button_clickability()
        main_page.wait_clickability_logout_button()
        main_page.click_constructor_button()
        main_page.wait_constructor_header()
        assert main_page.check_constructor_header()