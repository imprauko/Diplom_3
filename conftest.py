import pytest
from selenium import webdriver

from locators.main_page_locators import MainPageLocators, ConstructorPageLocators
from pages.login_page import LoginPageSteps
from urls import Urls
from locators.profile_page_locators import ProfilePageLocators
from test_data import TestData


@pytest.fixture(params=("chrome", "firefox"))
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def setup_logged_in(driver):
    login_page = LoginPageSteps(driver)
    login_page.open(Urls.login_page)
    login_page.login(TestData.login_data['email'], TestData.login_data['password'])
    login_page.wait_element_disappeared(MainPageLocators.OVERLAY)

    login_page.wait_for_element(ConstructorPageLocators.HEADER_CONSTRUCTOR)

    yield driver
    if login_page.check_is_displayed_element(ConstructorPageLocators.BUTTON_CLOSE_ORDER_NUMBER):
        login_page.wait_clickability_button(ConstructorPageLocators.BUTTON_CLOSE_ORDER_NUMBER)
        login_page.click_on_element(ConstructorPageLocators.BUTTON_CLOSE_ORDER_NUMBER)
    else:
        login_page.wait_element_disappeared(MainPageLocators.OVERLAY)
        login_page.wait_clickability_button(MainPageLocators.BUTTON_ACCOUNT_MAIN_PAGE)
        login_page.click_on_element(MainPageLocators.BUTTON_ACCOUNT_MAIN_PAGE)
        login_page.wait_clickability_button(ProfilePageLocators.BUTTON_LOGOUT)
        login_page.wait_element_disappeared(MainPageLocators.OVERLAY)