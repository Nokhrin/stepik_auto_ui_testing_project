from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form1')
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#login_link')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')

    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form1')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > p.price_color')
    # BASKET_URL = 'http://selenium1py.pythonanywhere.com/en-gb/basket/'
    BASKET_TOTAL = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')
    ADDED_TO_BASKET_NAME = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini.pull-right.hidden-xs > span > a')
