# test cases for product page
import time
import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


@pytest.mark.guest
class TestGuestActions:
    """проверка действий незарегистрированного пользователя"""

    @pytest.mark.parametrize('link', [
        'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear',
        'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'])
    def test_guest_can_add_product_to_basket(self, browser, link):
        """проверка добавления в корзину товаров из разных промоакций"""
        page = ProductPage(browser=browser, url=link)
        page.open()
        page.should_be_equal_price_and_total()
        time.sleep(100)

    @pytest.mark.need_review
    @pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                              pytest.param(
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  marks=pytest.mark.xfail),
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def test_guest_can_add_product_to_basket(self, browser, link):
        """проверка добавления в корзину товаров из разных промоакций"""
        page = ProductPage(browser=browser, url=link)
        page.open()
        page.should_be_equal_price_and_total()
        page.should_be_equal_product_name_and_added_product_name()

    @pytest.mark.xfail(reason='Product was added to the basket, so we expect to have success message')
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # Открываем страницу товара
        # Добавляем товар в корзину
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        page = ProductPage(browser=browser, url=link)
        page.open()
        page.add_to_basket_button()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        # Открываем страницу товара
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        page = ProductPage(browser=browser, url=link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail(reason='Product was added to the basket, so we expect to have success message')
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # Открываем страницу товара
        # Добавляем товар в корзину
        # Проверяем, что нет сообщения об успехе с помощью is_disappeared
        link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        page = ProductPage(browser=browser, url=link)
        page.open()
        page.add_to_basket_button()
        page.should_disappear_message()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        # Гость открывает страницу товара
        # Переходит в корзину по кнопке в шапке
        # Ожидаем, что в корзине нет товаров
        # Ожидаем, что есть текст о том что корзина пуста
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = BasketPage(browser, link)
        page.open()
        page.go_to_basket_page()
        page.should_be_empty_basket()
        page.should_be_no_products_on_basket_page()


@pytest.mark.registration
class TestUserAddToBasketFromProductPage:
    """проверка действий зарегистрированного пользователя"""

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # открыть страницу регистрации;
        # зарегистрировать нового пользователя;
        # проверить, что пользователь залогинен.
        self.link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        self.email = str(time.time()) + "@fakemail.org"
        self.password = str(time.time())
        page = LoginPage(browser=browser, url=self.link)
        page.open()
        page.register_new_user(email=self.email, password=self.password)
        page.should_be_authorized_user()
        # set the link for following tests
        self.link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'

    def test_user_cant_see_success_message(self, browser):
        # Открываем страницу товара
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        page = ProductPage(browser=browser, url=self.link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        # Открываем страницу товара
        # Добавляем товар в корзину
        # Сверяем стоимость товара и итог в корзине
        # Сверяем название товара на странице товара и в корзине
        page = ProductPage(browser=browser, url=self.link)
        page.open()
        page.should_be_equal_price_and_total()
        page.should_be_equal_product_name_and_added_product_name()
