from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        basket_content = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_TEXT)
        assert basket_content.text == 'Your basket is empty. Continue shopping', 'Basket is not empty'
