import time
from pages.base_page import BasePage
from locators.locators import EmailHomePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EmailHomePage(BasePage):
    def waiting_for_homepage_to_open(self):  # ожидание открытия домашней страницы
        WebDriverWait(self.browser, 15).until(EC.text_to_be_present_in_element(EmailHomePageLocators.H1, 'Почта'))
    # при условии что язык интерфейса "Русский"

    def go_to_page_for_creating_new_email(self):  # переход на страницу создания нового письма
        self.browser.find_element(*EmailHomePageLocators.BUTTON_TO_WRITE_MESSAGE).click()

    def deleting_selected_email(self):  # удаление выбранного письма
        self.browser.find_element(*EmailHomePageLocators.BUTTON_DELETE_MAIL).click()
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(EmailHomePageLocators.MESSAGE_ON_CONFIRMATION_OF_MAIL_DELETE))

    def having_an_unread_email(self):  # наличие непрочитанного письма
        assert self.is_element_present(*EmailHomePageLocators.UNREAD_MAIL), 'Нет не прочитанного письма'

    def get_email_subject_text(self):  # получение текста темы письма
        text_subject_email = self.browser.find_element(*EmailHomePageLocators.TEXT_SUBJECT_UNREAD_EMAIL).text
        return text_subject_email

    def get_email_body_text(self):  # получение текста тела письма
        self.browser.find_element(*EmailHomePageLocators.UNREAD_MAIL).click()
        iframe = self.browser.find_element(*EmailHomePageLocators.IFRAME_MAIL)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        time.sleep(0.1)
        text_body_email = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(EmailHomePageLocators.TEXT_BODY_EMAIL)).text
        self.browser.switch_to.default_content()  # выход из фрейма
        return text_body_email
