import allure
import pytest

from conftest import setup_logged_in
from pages.main_page import MainPageSteps

class TestIngredients:
    @allure.title(
        'Клик на ингредиент вызавает всплывающее окно с деталями')
    @allure.description(
        'Проверяем клик на ингредиент')
    @pytest.mark.parametrize("index", [1])#list(range(1, 16)))
    def test_open_popup_ingredient_panel(self, setup_logged_in, index):
        main_page = MainPageSteps(setup_logged_in)
        main_page.wait_ingredient_panel(index)
        main_page.scroll_ingredient_panel(index)
        main_page.click_ingredient_panel(index)
        main_page.wait_ingredient_details()
        assert main_page.check_ingredient_details()
        main_page.click_ingredient_details_close_button()

    @allure.title(
        'Проверяем кнопку закрытия деталей ингредиента')
    @allure.description(
        'Проверяем клик на кнопку закрытия попапа')
    @pytest.mark.parametrize("index", [1])#list(range(1, 16)))
    def test_close_popup_ingredient_panel(self, setup_logged_in, index):
        main_page = MainPageSteps(setup_logged_in)
        main_page.wait_ingredient_panel(index)
        main_page.scroll_ingredient_panel(index)
        main_page.click_ingredient_panel(index)
        main_page.wait_ingredient_details_close_button()
        main_page.click_ingredient_details_close_button()
        main_page.wait_popup_close()
        assert not main_page.check_ingredient_details()

    @allure.title(
        'при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    @allure.description(
        'Проверяем счетчик ингредиента при его добавлении')
    @pytest.mark.parametrize("index", [1])#list(range(1, 16)))
    def test_ingredient_panel_change_count(self, setup_logged_in, index):
        main_page = MainPageSteps(setup_logged_in)
        main_page.wait_ingredient_panel_counter(index)
        main_page.scroll_ingredient_panel(index)
        old_count_number = main_page.get_count_number(index)
        main_page.drag_and_drop_ingredient_panel_to_bucket(index)
        new_count_number = main_page.get_count_number(index)
        assert new_count_number > old_count_number
