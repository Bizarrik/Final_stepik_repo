import pytest
from .pages.product_page import ProductPage

@pytest.mark.parametrize('link_var', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# @pytest.mark.parametrize('link', ["okay_link",
#                                   pytest.param("bugged_link", marks=pytest.mark.xfail),
#                                   "okay_link"])

def test_guest_can_add_product_to_basket(browser, link_var):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link_var}"
    page = ProductPage(browser, link)
    page.open()
    page.should_add_item_to_basket()
    # input("Press Enter to continue...")
    # page.should_be_add_to_basket_button()
    # page.should_click_button_and_add_item_to_basket()
    # page.should_solve_quiz()
    # page.should_be_success_message_with_item_name()
    # page.should_be_info_message_with_item_price()