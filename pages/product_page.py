from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket_button(self):
        """click add to basket and retrieve response code"""
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text

    def go_to_basket(self):
        view_basket_button = self.browser.find_element(*ProductPageLocators.VIEW_BASKET_BUTTON)
        view_basket_button.click()

    def get_added_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.ADDED_TO_BASKET_NAME)
        return product_name.text

    def get_basket_total(self):
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        return basket_total.text

    def should_be_equal_product_name_and_added_product_name(self):
        product_name = self.get_product_name()
        self.add_to_basket_button()
        added_name = self.get_added_product_name()
        assert product_name == added_name, 'Name in the basket is not equal to product name'

    def should_be_equal_price_and_total(self):
        product_price = self.get_product_price()
        self.add_to_basket_button()
        basket_total = self.get_basket_total()
        assert product_price == basket_total, 'Basket total is not equal to product price'
