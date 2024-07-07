import pytest
from .pages.product_page import ProductPage

# @pytest.mark.parametrize('link_var', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#
# # @pytest.mark.parametrize('link', ["okay_link",
# #                                   pytest.param("bugged_link", marks=pytest.mark.xfail),
# #                                   "okay_link"]) НУЖНО ОТМЕТИТЬ 7 УРЛ КАК ПАДАЮЩИЙ
#
# def test_guest_can_add_product_to_basket(browser, link_var):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link_var}"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_add_item_to_basket()
#     # input("Press Enter to continue...")
#
# @pytest.mark.xfail(reason="expected bug")
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_click_button_and_add_item_to_basket()
#     page.should_not_be_success_message()
#
# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()
#
# @pytest.mark.xfail(reason="expected bug")
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_click_button_and_add_item_to_basket()
#     page.should_disapear_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-robot-novels_25/"
    page = ProductPage(browser, link)
    page.open()
    page.should_open_basket_page()
    page.should_be_empty_basket_message()
