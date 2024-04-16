#auth

username_button = ('xpath', '//input[@id="user-name"]')
password_button = ('xpath', '//input[@id="password"]')
login_button = ('xpath', '//input[@id="login-button"]')
warning_text = ('xpath', '//h3[contains(text(), "Epic sadface")]')

#cart

qntt_icon = ('xpath', '//span[contains(@class, "cart")]')
cart_icon = ('xpath', '//a[contains(@class, "cart")]')
remove_button = ('xpath', '//button[contains(@id, "remove")]')
add_cart_backpack_button = ('xpath', '//button[contains(@id, "backpack")]')
backpack_in_cart = ('xpath', '//div[text()="Sauce Labs Backpack"]')
backpack_price_in_cart = ('xpath', '//div[text()="29.99"]')
bike_title = ('xpath', '//a[@id="item_0_title_link"]')
add_cart_bike_button = ('xpath', '//button[@id="add-to-cart"]')
bike_in_cart = ('xpath', '//div[text()="Sauce Labs Bike Light"]')
bike_price_in_cart = ('xpath', '//div[text()="9.99"]')
item_in_cart = ('xpath', '//div[@class="cart_item"]')


#Item

shirt_label = ('xpath', '//a[@id="item_1_title_link"]')
shirt_pic = ('xpath', '//img[@alt="Sauce Labs Bolt T-Shirt"]')

#Order

checkout_button = ('xpath', '//button[@id="checkout"]')
fname_field = ('xpath', '//input[@id="first-name"]')
lname_field = ('xpath', '//input[@id="last-name"]')
zip_field = ('xpath', '//input[@id="postal-code"]')
continue_button = ('xpath', '//input[@id="continue"]')
total_price_field = ('xpath', '//div[contains(@class,"subtotal_label")]')
total_field = ('xpath', '//div[contains(@class,"summary_total")]')
finish_button = ('xpath', '//button[@id="finish"]')
thank_you = ('xpath', '//h2[text()="Thank you for your order!"]')

#Filter

item_label_element = ('xpath', '//div[@class="inventory_item_name "]')
item_price_element = ('xpath', '//div[@class="inventory_item_price"]')
filter_button = ('xpath', '//select[@class="product_sort_container"]')
az_button = ('xpath', '//option[@value="az"]')
za_button = ('xpath', '//option[@value="za"]')
lohi_button = ('xpath', '//option[@value="lohi"]')
hilo_button = ('xpath', '//option[@value="hilo"]')

#Menu

menu_button = ('xpath', '//button[@id="react-burger-menu-btn"]')
logout_button = ('xpath', '//a[@id="logout_sidebar_link"]')
about_button = ('xpath', '//a[@id="about_sidebar_link"]')
reset_button = ('xpath', '//a[@id="reset_sidebar_link"]')

#Register

name_field = ('xpath', '//input[@id="username"]')
pass_field = ('xpath', '//input[@id="password"]')
register_button = ('xpath', '//button[@id="registerButton"]')
checkbox_agree = ('xpath', '//input[@id="agreement"]')
