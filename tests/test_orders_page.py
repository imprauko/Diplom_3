import allure

from conftest import setup_logged_in
from pages.orders_page import OrdersPageSteps


class TestOrderNumbers:
    @allure.title(
        'при создании нового заказа, его номер появляется в разделе "В работе", счётчики «Выполнено за всё время» и "Выполнено за сегодня" увеличиваются')
    @allure.description(
        'Проверяем счетчики "Выполнено за все время", "Выполнено за сегодня" и отображение номера заказа в разделе "В работе"')
    def test_open_popup_ingredient_panel(self, setup_logged_in):
        main_page = OrdersPageSteps(setup_logged_in)
        main_page.wait_clickability_orders_button_header()
        main_page.click_orders_button_header()
        main_page.wait_count_orders_total()
        old_total_number = main_page.get_count_orders_total()
        old_by_day_number = main_page.get_count_orders_by_day()
        main_page.click_constructor_button_header()
        main_page.wait_order_confirm_button()
        main_page.drag_and_drop_ingredient_panel_to_bucket(1)
        main_page.click_order_confirm_button()
        order_number = main_page.get_order_number()
        main_page.close_popup_order()
        main_page.click_orders_button_header()
        main_page.wait_count_orders_total()
        new_total_number = main_page.get_count_orders_total()
        new_by_day_number = main_page.get_count_orders_by_day()
        in_work_list_orders = main_page.get_order_number_in_list(order_number)
        with allure.step("Проверяем увеличение счетчика 'за все время'"):
            assert new_total_number > old_total_number
        with allure.step("Проверяем увеличение счетчика 'за день'"):
            assert new_by_day_number > old_by_day_number
        with allure.step("Проверяем наличие номера заказа в разделе 'заказы в работе'"):
            assert order_number in in_work_list_orders
