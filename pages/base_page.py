import time

import allure
from selenium.common import ElementClickInterceptedException

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from seletools.actions import drag_and_drop

class BasePageSteps:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликаем на элемент')
    def click_on_element(self, locator):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(locator)
        )

        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        try:
            element.click()
        except ElementClickInterceptedException:
            time.sleep(1)
            element.click()


    @allure.step('Ждем прогрузки элемента')
    def wait_for_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step('Ждем закрытия элемента')
    def wait_element_disappeared(self, locator):
        time.sleep(0.5)
        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step('Проскролливаем до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Получаем текст элемента')
    def get_text(self, locator):
        element = self.driver.find_element(*locator)
        return element.text

    @allure.step('Проверить отображение элемента')
    def check_is_displayed_element(self, locator):
        element = self.driver.find_element(*locator)
        return element.is_displayed()

    @allure.step('Найти элемент')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Перетаскиваем элемент')
    def drag_and_drop(self, source_locator, target_locator):

        # Ждём, если на странице есть оверлей
        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located((By.XPATH, "//*[contains(@class, 'Modal_modal_overlay__x2ZCr')]"))
        )

        source = self.driver.find_element(*source_locator)
        target = self.driver.find_element(*target_locator)

        # Используем seletools
        drag_and_drop(self.driver, source, target)

        # Снова ждём исчезновения оверлея
        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located((By.XPATH, "//*[contains(@class, 'Modal_modal_overlay__x2ZCr')]"))
        )

    @allure.step('Ждем, пока кнопка не станет кликабельной')
    def wait_clickability_button(self, locator):
        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located((By.XPATH, "//*[contains(@class, 'Modal_modal_overlay__x2ZCr')]"))
        )
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))