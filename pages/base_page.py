import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop

class BasePageSteps:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step('Открываем ссылку')
    def open(self, url):
        self.driver.get(url)

    @allure.step('Кликаем на элемент')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Ждем прогрузки элемента')
    def wait_for_element(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Ждем закрытия элемента')
    def wait_element_disappeared(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

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
        elements = self.driver.find_elements(*locator)
        return len(elements) > 0 and elements[0].is_displayed()

    @allure.step('Найти элемент')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Перетаскиваем элемент')
    def drag_and_drop(self, source_locator, target_locator):
        source = self.driver.find_element(*source_locator)
        target = self.driver.find_element(*target_locator)
        drag_and_drop(self.driver, source, target)

    @allure.step('Ждем, пока кнопка не станет кликабельной')
    def wait_clickability_button(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step('Заполняем плейсхолдер')
    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step('Ждем, пока не выполнится заданное условие')
    def wait_for_condition(self, condition):
        return self.wait.until(lambda driver: condition())