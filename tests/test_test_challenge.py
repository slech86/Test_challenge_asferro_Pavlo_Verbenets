import pytest
from pages.email_authorization_page import EmailAuthorizationPage
from pages.email_home_page import EmailHomePage
from pages.new_email_page import NewEmailPage
from сonfiguration import Accounts
from singleton import Singleton


class TestChallenge:

    @pytest.fixture(scope="function", autouse=True)
    def mailbox_registration(self, browser):  # регистрация в почтовый ящик
        email_authorization_page = EmailAuthorizationPage(browser, Accounts.url_email)
        email_authorization_page.open()
        email_authorization_page.email_authorization()  # авторизация email

    def test_collection_of_data(self, browser):  # сбор данных
        for i in range(10):  # здесь указывается количество писем с которых будет формироваться данные
            email_home_page = EmailHomePage(browser, browser.current_url)
            email_home_page.go_to_page_for_creating_new_email()  # переход на страницу создания нового письма

            new_email_page = NewEmailPage(browser, browser.current_url)
            new_email_page.filling_in_fields_for_first_type_of_mail()  # заполнение полей для первого типа письма
            new_email_page.mail_sending()  # отправка письма

            email_home_page.waiting_for_homepage_to_open()  # ожидание открытия домашней страницы
            email_home_page.having_an_unread_email()  # наличие непрочитанного письма

            text_subject_email = email_home_page.get_email_subject_text()  # получение текста темы письма
            text_body_email = email_home_page.get_email_body_text()  # получение текста тела письма

            singleton = Singleton()  # использую Singleton для передачи словаря в следующий тест
            singleton.data_for_mail[text_subject_email] = text_body_email

            email_home_page.deleting_selected_email()  # удаление выбранного письма

    def test_sending_last_mail(self, browser):  # отправка последнего письма
        email_home_page = EmailHomePage(browser, browser.current_url)
        email_home_page.go_to_page_for_creating_new_email()  # переход на страницу создания нового письма

        new_email_page = NewEmailPage(browser, browser.current_url)
        singleton = Singleton()
        new_email_page.filling_in_fields_for_second_type_of_mail(singleton.data_for_mail)  # заполнение полей для второго типа письма
        new_email_page.mail_sending()  # отправка письма
        new_email_page.mail_sending_without_subject()  # отправка письма без темы

        email_home_page.waiting_for_homepage_to_open()  # ожидание открытия домашней страницы
        email_home_page.having_an_unread_email()  # наличие непрочитанного письма
