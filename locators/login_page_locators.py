from selenium.webdriver.common.by import By


class LoginPageLocators:
    INPUT_LOGIN = (By.XPATH, '//div/input[@name="name"]')  # Поле логина
    INPUT_LOGIN_PASSWORD = (By.XPATH, '//div/input[@name="Пароль"]')  # Поле пароля
    BUTTON_LOGIN = (By.XPATH, '//button[text()="Войти"]')  # Кнопка "Войти"
    HEADER_LOGIN_PAGE = (By.XPATH, '//h2[text()="Вход"]')  # Заголовок "Вход"