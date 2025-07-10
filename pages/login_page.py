from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePageSteps
from locators.login_page_locators import LoginPageLocators

class LoginPageSteps(BasePageSteps):

    def login(self, email, password):
        self.send_keys(LoginPageLocators.INPUT_LOGIN, email)
        self.send_keys(LoginPageLocators.INPUT_LOGIN_PASSWORD, password)
        self.wait_element_disappeared(MainPageLocators.OVERLAY)
        self.wait_clickability_button(LoginPageLocators.BUTTON_LOGIN)
        self.find_element(LoginPageLocators.BUTTON_LOGIN).click()