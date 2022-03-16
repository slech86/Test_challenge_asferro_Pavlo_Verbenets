from pages.base_page import BasePage
from locators.locators import NewEmailPageLocators
from сonfiguration import Accounts
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string


class NewEmailPage(BasePage):
    def generate_alphanum_random_string(self, length):  # генерация буквенно-цифровуй случайной строки
        letters_and_digits = string.ascii_letters + string.digits
        random_string = ''.join(random.sample(letters_and_digits, length))
        return random_string

    def filling_in_fields_for_first_type_of_mail(self):  # заполнение полей для первого типа письма
        self.browser.find_element(*NewEmailPageLocators.FIELD_TO).send_keys(Accounts.email)
        self.browser.find_element(*NewEmailPageLocators.FIELD_SUBJECT).send_keys(
            self.generate_alphanum_random_string(10))

        iframe = WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located(NewEmailPageLocators.IFRAME_BODY_OF_MAIL))
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        field_body = self.browser.find_element(*NewEmailPageLocators.FIELD_BODY_OF_MAIL)
        string_for_email_body_field = self.generate_alphanum_random_string(10)
        field_body.send_keys(string_for_email_body_field)
        WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element(NewEmailPageLocators.TEXT_IN_FIELD_BODY_OF_MAIL,
                                             string_for_email_body_field))
        self.browser.switch_to.default_content()  # выход из фрейма

    def filling_in_fields_for_second_type_of_mail(self, data_for_mail):  # заполнение полей для второго типа письма
        self.browser.find_element(*NewEmailPageLocators.FIELD_TO).send_keys(Accounts.email)

        iframe = WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located(NewEmailPageLocators.IFRAME_BODY_OF_MAIL))
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        field_body = self.browser.find_element(*NewEmailPageLocators.FIELD_BODY_OF_MAIL)
        string_for_email_body_field = ''

        for key, value in data_for_mail.items():
            letter_count = 0
            numbers_count = 0
            theme_and_body = key + value
            for i in theme_and_body:
                if i < "A":
                    numbers_count += 1
                else:
                    letter_count += 1
            string_for_email_body_field += f'Received mail on theme {key} with message: {value}. It contains {letter_count} letters and {numbers_count} numbers.\n'

        field_body.send_keys(string_for_email_body_field)
        WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element(NewEmailPageLocators.TEXT_IN_FIELD_BODY_OF_MAIL,
                                             'Received mail on theme '))
        self.browser.switch_to.default_content()  # выход из фрейма

    def mail_sending(self):  # отправка письма
        self.browser.find_element(*NewEmailPageLocators.BUTTON_SEND_MAIL).click()

    def mail_sending_without_subject(self):  # отправка письма без темы
        self.browser.find_element(*NewEmailPageLocators.BUTTON_SEND_MAIL_WITHOUT_SUBJECT).click()
