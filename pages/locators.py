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
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register_form > button')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > p.price_color')
    BASKET_TOTAL = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')
    ADDED_TO_BASKET_NAME = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini.pull-right.hidden-xs > span > a')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1)')


class BasePageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini.pull-right.hidden-xs > span > a')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_IS_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner > p')
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '.basket-items')
