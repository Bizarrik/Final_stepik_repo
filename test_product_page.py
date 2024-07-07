import pytest
from .pages.product_page import ProductPage

# @pytest.mark.parametrize('link_var', ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", "?promo=offer4", "?promo=offer5", "?promo=offer6", "?promo=offer7", "?promo=offer8", "?promo=offer9"])

# def test_guest_can_add_product_to_basket(browser, link_var):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{link_var}/"

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_add_item_to_basket()
    input("Press Enter to continue...")
    # page.should_be_add_to_basket_button()
    # page.should_click_button_and_add_item_to_basket()
    # page.should_solve_quiz()