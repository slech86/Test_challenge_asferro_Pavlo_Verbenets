from pages.base_page import BasePage
from locators.locators import EmailAuthorizationPageLocators
from сonfiguration import Accounts


class EmailAuthorizationPage(BasePage):
    def email_authorization(self):  # авторизация email
        self.browser.find_element(*EmailAuthorizationPageLocators.FIELD_EMAIL).send_keys(Accounts.email)
        self.browser.find_element(*EmailAuthorizationPageLocators.FIELD_PASSWORD).send_keys(Accounts.password_email)
        self.browser.find_element(*EmailAuthorizationPageLocators.BUTTON_LOG_IN).click()
