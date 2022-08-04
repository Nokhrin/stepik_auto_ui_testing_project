from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#login_link')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')

    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
