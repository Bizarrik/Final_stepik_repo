from selenium.webdriver.common.by import By
from .pages.login_page import LoginPage

def test_guest_should_see_login_elements(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()
    page.should_be_login_form()
    page.should_be_register_form()

