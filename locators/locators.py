from selenium.webdriver.common.by import By


class EmailAuthorizationPageLocators:
    FIELD_EMAIL = (By.XPATH, '//input[@id="rcmloginuser"]')
    FIELD_PASSWORD = (By.XPATH, '//input[@id="rcmloginpwd"]')
    BUTTON_LOG_IN = (By.XPATH, '//button[@id="rcmloginsubmit"]')


class EmailHomePageLocators:
    H1 = (By.XPATH, '//h1')
    BUTTON_TO_WRITE_MESSAGE = (By.XPATH, '//a[@href="./?_task=mail&_action=compose"]')
    BUTTON_DELETE_MAIL = (By.XPATH, '//a[@class="button delete"]')
    MESSAGE_ON_CONFIRMATION_OF_MAIL_DELETE = (By.XPATH, '//div[@class="confirmation content"]')
    UNREAD_MAIL = (By.XPATH, '//tr[contains(@class, "message unread")]')
    TEXT_SUBJECT_UNREAD_EMAIL = (By.XPATH, '//tr[contains(@class, "message unread")]/td[@class="subject"]/a/span')
    IFRAME_MAIL = (By.XPATH, '//iframe[@id="messagecontframe"]')
    TEXT_BODY_EMAIL = (By.XPATH, '//div[@id="messagebody"]//p')


class NewEmailPageLocators:
    FIELD_TO = (By.XPATH, '//textarea[@id="_to"]')
    FIELD_SUBJECT = (By.XPATH, '//input[@id="compose-subject"]')

    IFRAME_BODY_OF_MAIL = (By.XPATH, '//iframe[@id="composebody_ifr"]')

    FIELD_BODY_OF_MAIL = (By.XPATH, '//body[@id="tinymce"]')
    TEXT_IN_FIELD_BODY_OF_MAIL = (By.XPATH, '//body[@id="tinymce"]/p')

    BUTTON_SEND_MAIL = (By.XPATH, '//a[@class="button send"]')
    BUTTON_SEND_MAIL_WITHOUT_SUBJECT = (By.XPATH, '//button[@class="mainaction send ui-button ui-corner-all ui-widget"]')
