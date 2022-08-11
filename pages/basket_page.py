from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        """проверка наличия сообщения о пустой корзине"""
        basket_content = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_TEXT)
        assert basket_content.text == 'Your basket is empty. Continue shopping', 'Basket is not empty'

    def should_be_no_products_on_basket_page(self):
        """проверка отсутствия товара в корзине"""
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET)
