# test cases for main page
import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        """проверка перехода на страницу авторизации"""
        link = 'http://selenium1py.pythonanywhere.com/'
        page = MainPage(browser=browser, url=link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser=browser, url=browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        """проверка видимости ссылки на страницу авторизации"""
        # Гость открывает главную страницу
        # Ожидаем, что гость видит ссылку на страницу авторизации
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        """проверка отсутсвия товара в корзине при переходе с главной страницы"""
        # Гость открывает главную страницу
        # Переходит в корзину по кнопке в шапке сайта
        # Ожидаем, что в корзине нет товаров
        # Ожидаем, что есть текст о том что корзина пуста
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasketPage(browser, link)
        page.open()
        page.go_to_basket_page()
        page.should_be_empty_basket()
        page.should_be_no_products_on_basket_page()
