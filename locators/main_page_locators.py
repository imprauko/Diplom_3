from selenium.webdriver.common.by import By


class MainPageLocators:
    BUTTON_ACCOUNT_MAIN_PAGE = (By.XPATH, '//a[@href="/account"]')  # "Личный кабинет"
    BUTTON_CONSTRUCTOR = (By.XPATH, '//a[.//p[text()="Конструктор"]]')  # Кнопка "Конструктор"
    BUTTON_ORDERS_PAGE = (By.XPATH, '//a[@href="/feed"]')  # "Список заказов"

    INGREDIENT_PANEL = { # "Панель с ингредиентом"
        1: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]'), # "булка 1"
        2: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]'), # "булка 2"
        3: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa72"]'), # "соус 1"
        4: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa73"]'), # "соус 2"
        5: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa74"]'), # "соус 3"
        6: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa75"]'), # "соус 4"
        7: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6f"]'), # "начинка 1"
        8: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa70"]'), # "начинка 2"
        9: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa71"]'), # "начинка 3"
        10: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6e"]'), # "начинка 4"
        11: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa76"]'), # "начинка 5"
        12: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa77"]'), # "начинка 6"
        13: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa78"]'), # "начинка 7"
        14: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa79"]'), # "начинка 8"
        15: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa7a"]'), # "начинка 9"
    }
    INGREDIENT_PANEL_COUNTER = {  # "Счетчик панели ингредиента"
        1: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]/div/p[@class="counter_counter__num__3nue1"]'),  # "булка 1"
        2: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]/div/p[@class="counter_counter__num__3nue1"]'),  # "булка 2"
        3: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa72"]/div/p[@class="counter_counter__num__3nue1"]'),  # "соус 1"
        4: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa73"]/div/p[@class="counter_counter__num__3nue1"]'),  # "соус 2"
        5: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa74"]/div/p[@class="counter_counter__num__3nue1"]'),  # "соус 3"
        6: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa75"]/div/p[@class="counter_counter__num__3nue1"]'),  # "соус 4"
        7: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6f"]/div/p[@class="counter_counter__num__3nue1"]'),  # "начинка 1"
        8: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa70"]/div/p[@class="counter_counter__num__3nue1"]'),  # "начинка 2"
        9: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa71"]/div/p[@class="counter_counter__num__3nue1"]'),  # "начинка 3"
        10: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6e"]/div/p[@class="counter_counter__num__3nue1"]'),  # "начинка 4"
        11: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa76"]/div/p[@class="counter_counter__num__3nue1"]'),  # "начинка 5"
        12: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa77"]/div/p[@class="counter_counter__num__3nue1"]'),  # "начинка 6"
        13: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa78"]/div/p[@class="counter_counter__num__3nue1"]'),  # "начинка 7"
        14: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa79"]/div/p[@class="counter_counter__num__3nue1"]'),  # "начинка 8"
        15: (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa7a"]/div/p[@class="counter_counter__num__3nue1"]'),  # "начинка 9"
    }
    HEADER_DETAILS = (By.XPATH, '//h2[text()="Детали ингредиента"]') # Заголовок "Детали ингредиента" во всплывающем окне
    BUTTON_CLOSE_DETAILS = (
        By.XPATH,
        '//section[contains(@class, "Modal_modal_opened")]/div/button[contains(@class, "Modal_modal__close__TnseK")]')  # Кнопка "Закрыть" во всплывающем окне "Детали ингредиента"

class ConstructorPageLocators:
    HEADER_CONSTRUCTOR = (By.XPATH, '//h1[text()="Соберите бургер"]')  # Заголовок "Соберите бургер"

    BUTTON_ORDER_CONFIRM = (By.XPATH, '//button[text()="Оформить заказ"]')  # Оформить заказ
    HEADER_ORDER_NUMBER = (By.XPATH, '//div[contains(@class, "Modal_modal__contentBox__sCy8X pt-30 pb-30")]/h2[contains(@class, "Modal_modal__title_shadow__3ikwq")]')  # Номер заказа во всплывающем окне
    BUTTON_CLOSE_ORDER_NUMBER = (By.XPATH,
                           '//section[contains(@class, "Modal_modal_opened")]/div/button[contains(@class, "Modal_modal__close__TnseK")]')  # Кнопка "Закрыть" во всплывающем окне
