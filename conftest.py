import time

import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import MainPageLocators, ConstructorPageLocators
from urls import Urls
from locators.login_page_locators import LoginPageLocators
from locators.profile_page_locators import ProfilePageLocators
from test_data import TestData


@pytest.fixture(params=("chrome", "firefox"))
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(Urls.main_page)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(Urls.main_page)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def setup_logged_in(driver):
    driver.get(Urls.login_page)

    driver.find_element(*LoginPageLocators.INPUT_LOGIN).send_keys(TestData.login_data['email'])
    driver.find_element(*LoginPageLocators.INPUT_LOGIN_PASSWORD).send_keys(TestData.login_data['password'])

    WebDriverWait(driver, 30).until(
        EC.invisibility_of_element_located((By.XPATH, "//*[contains(@class, 'Modal_modal_overlay__x2ZCr')]"))
    )
    time.sleep(0.5)
    button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(LoginPageLocators.BUTTON_LOGIN)
    )
    button.click()

    WebDriverWait(driver, 20).until(EC.presence_of_element_located(
            ConstructorPageLocators.HEADER_CONSTRUCTOR))
    time.sleep(0.5)

    yield driver

    # Ждём, пока исчезнет оверлей
    WebDriverWait(driver, 20).until(
        EC.invisibility_of_element_located((By.XPATH, "//*[contains(@class, 'Modal_modal_overlay__x2ZCr')]"))
    )

    # Теперь кликаем по кнопке аккаунта и кнопке выхода
    driver.find_element(*MainPageLocators.BUTTON_ACCOUNT_MAIN_PAGE).click()
    time.sleep(0.5)

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(ProfilePageLocators.BUTTON_LOGOUT)
    ).click()
    WebDriverWait(driver, 20).until(
        EC.invisibility_of_element_located((By.XPATH, "//*[contains(@class, 'Modal_modal_overlay__x2ZCr')]"))
    )