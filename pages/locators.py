from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BTN = (By.NAME, "login_submit")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BTN = (By.NAME, "registration_submit")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert.alert-success")
    ITEM_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    ITEM_NAME = (By.TAG_NAME, "h1")
    ITEM_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ITEM_PRICE_IN_INFO = (By.CSS_SELECTOR, "p:nth-child(1) > strong")
    INFO_MESSAGE = (By.CLASS_NAME, "alert.alert-info")

class BasketPageLocators():
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner")
