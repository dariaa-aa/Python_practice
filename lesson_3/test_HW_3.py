import time

import pytest
from selenium.webdriver.support import expected_conditions as EC
from data import *
from locators import *

#explicit wait
def test_registration_expl(driver_expl, wait):
    driver_expl.get(base_url)
    assert driver_expl.find_element(*main_title).text == 'Практика с ожиданиями в Selenium'
    wait.until(EC.visibility_of_element_located(start_button))
    wait.until(EC.element_to_be_clickable(start_button)).click()
    assert driver_expl.find_element(*registration_form).get_attribute('class') != 'hidden'
    driver_expl.find_element(*login_field).send_keys(login)
    driver_expl.find_element(*password_field).send_keys(password)
    driver_expl.find_element(*agree_checkbox).click()
    driver_expl.find_element(*register_button).click()
    wait.until(EC.visibility_of_element_located(loader))
    assert driver_expl.find_element(*loader).get_attribute('class') != 'hidden'
    wait.until(EC.visibility_of_element_located(success_message))
    assert driver_expl.find_element(*success_message).get_attribute('class') != 'hidden'

#implicit wait
def test_registration_impl(driver_impl):
    driver_impl.get(base_url)
    assert driver_impl.find_element(*main_title).text == 'Практика с ожиданиями в Selenium'
    driver_impl.find_element(*start_button).click()
    driver_impl.find_element(*login_field).send_keys(login)
    driver_impl.find_element(*password_field).send_keys(password)
    driver_impl.find_element(*agree_checkbox).click()
    driver_impl.find_element(*register_button).click()
    assert driver_impl.find_element(*loader).get_attribute('class') != 'hidden'
    driver_impl.find_element(*success_message).click()
    assert driver_impl.find_element(*success_message).get_attribute('class') != 'hidden'

#time sleep
def test_registration_ts(driver):
    driver.get(base_url)
    assert driver.find_element(*main_title).text == 'Практика с ожиданиями в Selenium'
    time.sleep(5)
    driver.find_element(*start_button).click()
    assert driver.find_element(*registration_form).get_attribute('class') != 'hidden'
    driver.find_element(*login_field).send_keys(login)
    driver.find_element(*password_field).send_keys(password)
    driver.find_element(*agree_checkbox).click()
    driver.find_element(*register_button).click()
    assert driver.find_element(*loader).get_attribute('class') != 'hidden'
    time.sleep(5)
    assert driver.find_element(*success_message).get_attribute('class') != 'hidden'

def test_register_negative(driver_expl, wait):

    driver_expl.get(base_url)
    assert driver_expl.find_element(*main_title).text == 'Практика с ожиданиями в Selenium'
    wait.until(EC.visibility_of_element_located(start_button))
    wait.until(EC.element_to_be_clickable(start_button)).click()

    assert driver_expl.find_element(*registration_form).get_attribute('class') != 'hidden'
    driver_expl.find_element(*login_field).send_keys(login)
    driver_expl.find_element(*register_button).click()
    alert = wait.until(EC.alert_is_present())
    assert alert.text == 'Пожалуйста, заполните все поля и согласитесь с правилами.'
    driver_expl.switch_to.alert
    alert.accept()
    driver_expl.find_element(*login_field).clear()
    assert driver_expl.find_element(*login_field).text == ''

    driver_expl.find_element(*password_field).send_keys(password)
    driver_expl.find_element(*register_button).click()
    alert = wait.until(EC.alert_is_present())
    assert alert.text == 'Пожалуйста, заполните все поля и согласитесь с правилами.'
    driver_expl.switch_to.alert
    alert.accept()
    driver_expl.find_element(*password_field).clear()
    assert driver_expl.find_element(*password_field).text == ''

    driver_expl.find_element(*agree_checkbox).click()
    driver_expl.find_element(*register_button).click()
    alert = wait.until(EC.alert_is_present())
    assert alert.text == 'Пожалуйста, заполните все поля и согласитесь с правилами.'
    driver_expl.switch_to.alert
    alert.accept()

def test_add_remove(driver):
    driver.get(add_url)
    for i in range(num):
        driver.find_element(*add_button).click()
    remove = driver.find_elements(*remove_button)
    for i in remove:
        i.click()
    assert len(driver.find_elements(*remove_button)) == 0

def test_basic_auth(driver):
    driver.get(basic_auth_url)
    driver.get(f'https://{basic_auth_data}the-internet.herokuapp.com/basic_auth')
    assert driver.find_element(*basic_auth_success_text).text == 'Basic Auth'

def test_broken_img(driver):
    driver.get(broken_url)
    images = driver.find_elements(*img)
    image_srcs = []
    for image in images:
        image_srcs.append(image.get_attribute('src'))
    for src in image_srcs:
        driver.get(src)
        # if len(driver.find_elements(*not_found)) != 0:
        if 'found' in driver.page_source:
            assert len(driver.find_elements(*not_found)) > 0

def test_checkboxes(driver):
    driver.get(checkbox_url)
    checked_checkboxes= driver.find_elements(*checkbox_checked)
    for checked in checked_checkboxes:
        checked.click()
    checkboxes = driver.find_elements(*checkbox)
    for check in checkboxes:
        check.click()

    for check in checkboxes:
        assert check.is_selected()