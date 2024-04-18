import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from data import *

@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--headless')

    yield options

@pytest.fixture
def driver(chrome_options):
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)

    yield driver

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, 10, poll_frequency=1)

    yield wait

@pytest.fixture
def auth_positive(driver):
    driver.get(base_url)

    driver.find_element(*username_button).send_keys(correct_username)
    driver.find_element(*password_button).send_keys(correct_password)
    driver.find_element(*login_button).click()
    assert driver.current_url == main_page_url
    assert len(driver.find_elements(*main_page_container)) != 0
    assert len(driver.find_elements(*main_page_items)) == 6

    yield
    driver.find_element(*menu_button).click()
    driver.find_element(*logout_button).click()

@pytest.fixture
def add_to_cart(driver, auth_positive):

    driver.find_element(*add_cart_backpack_button).click()

@pytest.fixture
def form_clear(driver):
    driver.get(base_url_2)
    assert driver.current_url == base_url_2

    name = driver.find_element(*name_field)
    password = driver.find_element(*pass_field)
    checkbox = driver.find_element(*checkbox_agree)

    if checkbox.is_selected():
        checkbox.click()

    if name.text != '' or password.text != '':
        name.clear()
        password.clear()

    assert name.text == ''
    assert password.text == ''
    assert not checkbox.is_selected()
