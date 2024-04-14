import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

@pytest.fixture
def auth_positive():
    driver.get('https://www.saucedemo.com/')
    username_button = ('xpath', '//input[@id="user-name"]')
    password_button = ('xpath', '//input[@id="password"]')
    login_button = ('xpath', '//input[@id="login-button"]')

    username = 'standard_user'
    password = 'secret_sauce'

    driver.find_element(*username_button).send_keys(username)
    driver.find_element(*password_button).send_keys(password)
    driver.find_element(*login_button).click()

@pytest.fixture
def add_to_cart(auth_positive):
    add_cart_button = ('xpath', '//button[contains(@id, "backpack")]')

    driver.find_element(*add_cart_button).click()

#Authorisation
def test_auth_positive():
    driver.get('https://www.saucedemo.com/')
    username_button = ('xpath', '//input[@id="user-name"]')
    password_button = ('xpath', '//input[@id="password"]')
    login_button = ('xpath', '//input[@id="login-button"]')

    username = 'standard_user'
    password = 'secret_sauce'

    driver.find_element(*username_button).send_keys(username)
    driver.find_element(*password_button).send_keys(password)
    driver.find_element(*login_button).click()

    assert driver.current_url == 'https://www.saucedemo.com/inventory.html', 'mistake in url'
    assert driver.title == 'Swag Labs', 'mistake in title'

def test_auth_negative():
    driver.get('https://www.saucedemo.com/')
    username_button = ('xpath', '//input[@id="user-name"]')
    password_button = ('xpath', '//input[@id="password"]')
    login_button = ('xpath', '//input[@id="login-button"]')
    warning_text = ('xpath', '//h3[contains(text(), "Epic sadface")]')

    username = 'user'
    password = 'user'

    driver.find_element(*username_button).send_keys(username)
    driver.find_element(*password_button).send_keys(password)
    driver.find_element(*login_button).click()

    assert driver.current_url == 'https://www.saucedemo.com/', 'mistake in url'
    assert driver.find_element(*warning_text).get_attribute('data-test') == 'error', 'mistake in warning'

#Cart
def test_add_cart_catalogue(auth_positive):
    add_cart_button = ('xpath', '//button[contains(@id, "backpack")]')
    qntt_icon = ('xpath', '//span[contains(@class, "cart")]')
    cart_icon = ('xpath', '//a[contains(@class, "cart")]')
    item_in_cart = ('xpath', '//div[text()="Sauce Labs Backpack"]')
    price_in_cart = ('xpath', '//div[text()="29.99"]')

    driver.find_element(*add_cart_button).click()
    assert driver.find_element(*qntt_icon).text == '1'

    driver.find_element(*cart_icon).click()
    assert driver.current_url == 'https://www.saucedemo.com/cart.html'
    assert driver.find_element(*item_in_cart).text == 'Sauce Labs Backpack'
    assert driver.find_element(*price_in_cart).text == '$29.99'

def test_remove_item_catalogue(add_to_cart):
    cart_icon = ('xpath', '//a[contains(@class, "cart")]')
    qntt_icon = ('xpath', '//span[contains(@class, "cart")]')
    remove_button = ('xpath', '//button[contains(@id, "remove")]')
    removed_item = ('xpath', '//div[@class="removed_cart_item"]')

    driver.find_element(*cart_icon).click()
    assert driver.current_url == 'https://www.saucedemo.com/cart.html'

    driver.find_element(*remove_button).click()
    try:
        driver.find_element(*qntt_icon)
    except:
        element = 'None'
    assert element == 'None'
    assert driver.find_element(*removed_item)

def test_add_cart_item(auth_positive):
    item = ('xpath', '//a[@id="item_0_title_link"]')
    add_cart_button = ('xpath', '//button[@id="add-to-cart"]')
    qntt_icon = ('xpath', '//span[contains(@class, "cart")]')
    cart_icon = ('xpath', '//a[contains(@class, "cart")]')
    item_in_cart = ('xpath', '//div[text()="Sauce Labs Bike Light"]')
    price_in_cart = ('xpath', '//div[text()="9.99"]')

    driver.find_element(*item).click()
    assert driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=0'
    driver.find_element(*add_cart_button).click()
    assert driver.find_element(*qntt_icon).text == '1'
    driver.find_element(*cart_icon).click()
    assert driver.current_url == 'https://www.saucedemo.com/cart.html'
    assert driver.find_element(*item_in_cart).text == 'Sauce Labs Bike Light'
    assert driver.find_element(*price_in_cart).text == '$9.99'

def test_remove_cart_item(auth_positive):
    item = ('xpath', '//a[@id="item_0_title_link"]')
    add_cart_button = ('xpath', '//button[@id="add-to-cart"]')
    qntt_icon = ('xpath', '//span[contains(@class, "cart")]')
    remove_button = ('xpath', '//button[@id="remove"]')

    driver.find_element(*item).click()
    assert driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=0'
    driver.find_element(*add_cart_button).click()
    driver.find_element(*remove_button).click()

    try:
        driver.find_element(*qntt_icon)
    except:
        element = 'None'
    assert element == 'None'

#Item
def test_item_label_click(auth_positive):
    item_label = ('xpath', '//a[@id="item_1_title_link"]')

    driver.find_element(*item_label).click()
    assert driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=1'

def test_item_pic_click(auth_positive):
    item_pic = ('xpath', '//img[@alt="Sauce Labs Bolt T-Shirt"]')

    driver.find_element(*item_pic).click()
    assert driver.current_url == 'https://www.saucedemo.com/inventory-item.html?id=1'

#Order
def test_order_positive(add_to_cart):
    cart_icon = ('xpath', '//a[contains(@class, "cart")]')
    checkout_button = ('xpath', '//button[@id="checkout"]')
    fname_field = ('xpath', '//input[@id="first-name"]')
    lname_field = ('xpath', '//input[@id="last-name"]')
    zip_fieled = ('xpath', '//input[@id="postal-code"]')
    continue_button = ('xpath', '//input[@id="continue"]')
    item_in_cart = ('xpath', '//div[text()="Sauce Labs Backpack"]')
    total_price_field = ('xpath', '//div[contains(@class,"subtotal_label")]')
    total_field = ('xpath', '//div[contains(@class,"summary_total")]')
    finish_button = ('xpath', '//button[@id="finish"]')
    thank_you = ('xpath', '//h2[text()="Thank you for your order!"]')

    driver.find_element(*cart_icon).click()
    assert driver.current_url == 'https://www.saucedemo.com/cart.html'
    driver.find_element(*checkout_button).click()
    assert driver.current_url == 'https://www.saucedemo.com/checkout-step-one.html'
    driver.find_element(*fname_field).send_keys('Daria')
    driver.find_element(*lname_field).send_keys('Podolskaia')
    driver.find_element(*zip_fieled).send_keys('117525')
    assert driver.find_element(*fname_field).get_attribute('value') == 'Daria'
    assert driver.find_element(*lname_field).get_attribute('value') == 'Podolskaia'
    assert driver.find_element(*zip_fieled).get_attribute('value') == '117525'
    driver.find_element(*continue_button).click()
    assert driver.current_url == 'https://www.saucedemo.com/checkout-step-two.html'
    assert driver.find_element(*item_in_cart).text == 'Sauce Labs Backpack'
    assert driver.find_element(*total_price_field).text == 'Item total: $29.99'
    assert driver.find_element(*total_field).text == 'Total: $32.39'
    driver.find_element(*finish_button).click()
    assert driver.current_url == 'https://www.saucedemo.com/checkout-complete.html'
    assert driver.find_element(*thank_you).text == 'Thank you for your order!'

#Filter
def test_filter_az(auth_positive):
    item_label_element = ('xpath', '//div[@class="inventory_item_name "]')
    filter_button = ('xpath', '//select[@class="product_sort_container"]')
    az_button = ('xpath', '//option[@value="az"]')
    items_list = []

    driver.find_element(*filter_button).click()
    driver.find_element(*az_button).click()
    items = driver.find_elements(*item_label_element)
    for item in items:
        items_list.append(item.text)

    items_list_sorted = sorted(items_list)
    assert items_list == items_list_sorted

def test_filter_za(auth_positive):
    item_label_element = ('xpath', '//div[@class="inventory_item_name "]')
    filter_button = ('xpath', '//select[@class="product_sort_container"]')
    items_list = []
    za_button = ('xpath', '//option[@value="za"]')

    driver.find_element(*filter_button).click()
    driver.find_element(*za_button).click()
    items = driver.find_elements(*item_label_element)
    for item in items:
        items_list.append(item.text)

    items_list_sorted = sorted(items_list, reverse=True)
    assert items_list == items_list_sorted

def test_filter_lohi(auth_positive):
    item_price_element = ('xpath', '//div[@class="inventory_item_price"]')
    filter_button = ('xpath', '//select[@class="product_sort_container"]')
    items_list = []
    lohi_button = ('xpath', '//option[@value="lohi"]')

    driver.find_element(*filter_button).click()
    driver.find_element(*lohi_button).click()
    items = driver.find_elements(*item_price_element)
    for item in items:
        items_list.append(float(item.text[1:-1]))

    items_list_sorted = sorted(items_list)
    assert items_list == items_list_sorted

def test_filter_hilo(auth_positive):
    item_price_element = ('xpath', '//div[@class="inventory_item_price"]')
    filter_button = ('xpath', '//select[@class="product_sort_container"]')
    items_list = []
    hilo_button = ('xpath', '//option[@value="hilo"]')

    driver.find_element(*filter_button).click()
    driver.find_element(*hilo_button).click()
    items = driver.find_elements(*item_price_element)
    for item in items:
        items_list.append(float(item.text[1:-1]))

    items_list_sorted = sorted(items_list, reverse=True)
    assert items_list == items_list_sorted

#Menu
def test_menu_logout(auth_positive):
    menu_button = ('xpath', '//button[@id="react-burger-menu-btn"]')
    logout_button = ('xpath', '//a[@id="logout_sidebar_link"]')

    driver.find_element(*menu_button).click()
    driver.find_element(*logout_button).click()
    assert driver.current_url == 'https://www.saucedemo.com/'

def test_menu_about(auth_positive):
    menu_button = ('xpath', '//button[@id="react-burger-menu-btn"]')
    about_button = ('xpath', '//a[@id="about_sidebar_link"]')

    driver.find_element(*menu_button).click()
    # time.sleep(3) почему не работает без паузы?
    driver.find_element(*about_button).click()
    assert driver.current_url == 'https://saucelabs.com/'

def test_menu_reset(add_to_cart):
    menu_button = ('xpath', '//button[@id="react-burger-menu-btn"]')
    reset_button = ('xpath', '//a[@id="reset_sidebar_link"]')
    qntt_icon = ('xpath', '//span[contains(@class, "cart")]')

    driver.find_element(*menu_button).click()
    time.sleep(3)
    driver.find_element(*reset_button).click()

    try:
        driver.find_element(*qntt_icon)
    except:
        element = 'None'
    assert element == 'None'