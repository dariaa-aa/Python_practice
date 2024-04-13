import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.saucedemo.com/')
username_button = ('xpath', '//input[@id="user-name"]')
password_button = ('xpath', '//input[@id="password"]')
login_button = ('xpath', '//input[@id="login-button"]')

username = 'standard_user'
password = 'secret_sauce'

driver.find_element(*username_button).send_keys(username)
driver.find_element(*password_button).send_keys(password)
time.sleep(3)
driver.find_element(*login_button).click()
time.sleep(3)

assert driver.current_url == 'https://www.saucedemo.com/inventory.html', 'mistake in url'
assert driver.title == 'Swag Labs', 'mistake in title'
