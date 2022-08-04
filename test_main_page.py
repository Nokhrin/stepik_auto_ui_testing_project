from selenium.webdriver.common.by import By
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser=browser, url=link)
    page.open()
    page.go_to_login_page()

    # command to check the test
    # pytest -v --tb=line --language=en test_main_page.py
