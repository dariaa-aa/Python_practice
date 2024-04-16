import pytest
from locators import *
from data import *

# wait = WebDriverWait(driver, 10, poll_frequency=1)

#Authorisation
def test_auth_positive(driver):
    driver.get(base_url)

    driver.find_element(*username_button).send_keys(correct_username)
    driver.find_element(*password_button).send_keys(correct_password)
    driver.find_element(*login_button).click()

    assert driver.current_url == main_page_url, 'mistake in url'
    assert driver.title == 'Swag Labs', 'mistake in title'

def test_auth_negative(driver):
    driver.get(base_url)

    driver.find_element(*username_button).send_keys(fake_username)
    driver.find_element(*password_button).send_keys(fake_password)
    driver.find_element(*login_button).click()

    assert driver.current_url == base_url, 'mistake in url'
    assert driver.find_element(*warning_text).get_attribute('data-test') == 'error', 'mistake in warning'

#Cart
def test_add_cart_catalogue(driver, auth_positive):

    driver.find_element(*add_cart_backpack_button).click()
    assert 'shopping-cart-badge' in driver.page_source
    assert driver.find_element(*qntt_icon).text == '1'

    driver.find_element(*cart_icon).click()
    assert driver.current_url == cart_url
    assert driver.find_element(*backpack_in_cart).text == 'Sauce Labs Backpack'
    assert driver.find_element(*backpack_price_in_cart).text == '$29.99'

def test_remove_item_catalogue(driver, add_to_cart):

    driver.find_element(*cart_icon).click()
    assert driver.current_url == cart_url

    driver.find_element(*remove_button).click()
    driver.find_element(*cart_icon).click()
    assert driver.current_url == cart_url
    # try:
    #     driver.find_element(*qntt_icon)
    # except:
    #     element = 'None'
    # assert element == 'None'
    assert len(driver.find_elements(*item_in_cart)) == 0
    # assert 'shopping-cart-badge' not in driver.page_source
    # assert 'cart_item_label' not in driver.page_source

def test_add_cart_item(driver, auth_positive):

    driver.find_element(*bike_title).click()
    assert driver.current_url == bike_url
    driver.find_element(*add_cart_bike_button).click()
    assert 'shopping-cart-badge' in driver.page_source
    assert driver.find_element(*qntt_icon).text == '1'
    driver.find_element(*cart_icon).click()
    assert driver.current_url == cart_url
    assert driver.find_element(*bike_in_cart).text == 'Sauce Labs Bike Light'
    assert driver.find_element(*bike_price_in_cart).text == '$9.99'

def test_remove_cart_item(driver, auth_positive):
    add_cart_button = ('xpath', '//button[@id="add-to-cart"]')

    driver.find_element(*bike_title).click()
    assert driver.current_url == bike_url
    driver.find_element(*add_cart_bike_button).click()
    driver.find_element(*remove_button).click()
    driver.find_element(*cart_icon).click()
    assert driver.current_url == cart_url

    # try:
    #     driver.find_element(*qntt_icon)
    # except:
    #     element = 'None'
    # assert element == 'None'
    assert len(driver.find_elements(*item_in_cart)) == 0
    # assert 'shopping-cart-badge' not in driver.page_source
    # assert 'remove' not in driver.page_source

#Item
def test_item_label_click(driver, auth_positive):

    driver.find_element(*shirt_label).click()
    assert driver.current_url == shirt_url

def test_item_pic_click(driver, auth_positive):

    driver.find_element(*shirt_pic).click()
    assert driver.current_url == shirt_url

#Order
def test_order_positive(driver, add_to_cart):

    driver.find_element(*cart_icon).click()
    assert driver.current_url == cart_url
    driver.find_element(*checkout_button).click()
    assert driver.current_url == step_one_order_url
    driver.find_element(*fname_field).send_keys(fname)
    driver.find_element(*lname_field).send_keys(lname)
    driver.find_element(*zip_field).send_keys(zip_code)
    assert driver.find_element(*fname_field).get_attribute('value') == fname
    assert driver.find_element(*lname_field).get_attribute('value') == lname
    assert driver.find_element(*zip_field).get_attribute('value') == zip_code
    driver.find_element(*continue_button).click()
    assert driver.current_url == step_two_order_url
    assert driver.find_element(*backpack_in_cart).text == 'Sauce Labs Backpack'
    assert driver.find_element(*total_price_field).text == 'Item total: $29.99'
    assert driver.find_element(*total_field).text == 'Total: $32.39'
    driver.find_element(*finish_button).click()
    assert driver.current_url == complete_order_url
    assert driver.find_element(*thank_you).text == 'Thank you for your order!'

#Filter
def test_filter_az(driver, auth_positive):
    items_list = []

    driver.find_element(*filter_button).click()
    driver.find_element(*az_button).click()
    items = driver.find_elements(*item_label_element)
    for item in items:
        items_list.append(item.text)

    items_list_sorted = sorted(items_list)
    assert items_list == items_list_sorted

def test_filter_za(driver, auth_positive):
    items_list = []

    driver.find_element(*filter_button).click()
    driver.find_element(*za_button).click()
    items = driver.find_elements(*item_label_element)
    for item in items:
        items_list.append(item.text)

    items_list_sorted = sorted(items_list, reverse=True)
    assert items_list == items_list_sorted

def test_filter_lohi(driver, auth_positive):
    items_list = []

    driver.find_element(*filter_button).click()
    driver.find_element(*lohi_button).click()
    items = driver.find_elements(*item_price_element)
    for item in items:
        items_list.append(float(item.text[1:-1]))

    items_list_sorted = sorted(items_list)
    assert items_list == items_list_sorted

def test_filter_hilo(driver, auth_positive):
    items_list = []

    driver.find_element(*filter_button).click()
    driver.find_element(*hilo_button).click()
    items = driver.find_elements(*item_price_element)
    for item in items:
        items_list.append(float(item.text[1:-1]))

    items_list_sorted = sorted(items_list, reverse=True)
    assert items_list == items_list_sorted

#Menu
def test_menu_logout(driver, auth_positive):

    driver.find_element(*menu_button).click()
    driver.find_element(*logout_button).click()

def test_menu_about(driver, auth_positive):

    driver.find_element(*menu_button).click()
    driver.find_element(*about_button).click()
    assert driver.current_url == about_url

def test_menu_reset(driver, add_to_cart):

    driver.find_element(*menu_button).click()
    driver.find_element(*reset_button).click()

    # try:
    #     driver.find_element(*qntt_icon)
    # except:
    #     element = 'None'
    # assert element == 'None'

    assert 'shopping_cart_badge' not in driver.page_source
    # assert 'remove' not in driver.page_source

#Register

def test_registration_positive(driver, form_clear):
    name = driver.find_element(*name_field)
    password = driver.find_element(*pass_field)
    checkbox = driver.find_element(*checkbox_agree)
    register = driver.find_element(*register_button)

    name.send_keys(name_cor)
    password.send_keys(pass_cor)
    checkbox.click()

    register.click()

    assert driver.current_url != base_url_2

@pytest.mark.xfail
@pytest.mark.negative
@pytest.mark.defect
def test_registration_negative(driver, form_clear):
    name = driver.find_element(*name_field)
    password = driver.find_element(*pass_field)
    checkbox = driver.find_element(*checkbox_agree)
    register = driver.find_element(*register_button)

    name.send_keys('      ')
    password.send_keys('        ')
    checkbox.click()

    register.click()

    assert driver.current_url != base_url_2

def test_enabled_button(driver, form_clear):
    name = driver.find_element(*name_field)
    password = driver.find_element(*pass_field)
    checkbox = driver.find_element(*checkbox_agree)
    register = driver.find_element(*register_button)

    name.send_keys(name_cor)
    password.send_keys(pass_cor)
    checkbox.click()

    assert register.is_enabled()
def test_empty_field(driver, form_clear):
    name = driver.find_element(*name_field)
    password = driver.find_element(*pass_field)
    checkbox = driver.find_element(*checkbox_agree)
    register = driver.find_element(*register_button)

    checkbox.click()

    name.send_keys(name_cor)
    assert not register.is_enabled()
    name.clear()

    password.send_keys(pass_cor)
    assert not register.is_enabled()