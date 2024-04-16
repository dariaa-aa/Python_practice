from faker import Faker

#auth

correct_username = 'standard_user'
correct_password = 'secret_sauce'

fake_username = 'user'
fake_password = 'user'

#order

fake = Faker('en_US')
fname = fake.first_name()
lname = fake.last_name()
zip_code = fake.postcode()

#url

base_url = 'https://www.saucedemo.com/'
main_page_url = 'https://www.saucedemo.com/inventory.html'
cart_url = 'https://www.saucedemo.com/cart.html'
about_url = 'https://saucelabs.com/'
bike_url = 'https://www.saucedemo.com/inventory-item.html?id=0'
shirt_url = 'https://www.saucedemo.com/inventory-item.html?id=1'

step_one_order_url = 'https://www.saucedemo.com/checkout-step-one.html'
step_two_order_url = 'https://www.saucedemo.com/checkout-step-two.html'
complete_order_url = 'https://www.saucedemo.com/checkout-complete.html'

#Register
base_url_2 = 'https://victoretc.github.io/webelements_information/'

#Data
name_cor = 'Daria'
pass_cor = '123456'