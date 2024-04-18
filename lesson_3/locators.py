main_title = ('xpath', '//h1[text()="Практика с ожиданиями в Selenium"]')

start_button = ('xpath', '//button[@id="startTest"]')

registration_form = ('xpath', '//div[@id="registrationForm"]')
# class не равен 'hidden'

login_field = ('xpath', '//input[@id="login"]')

password_field = ('xpath', '//input[@id="password"]')

agree_checkbox = ('xpath', '//input[@id="agree"]')

register_button = ('xpath', '//button[@id="register"]')

loader = ('xpath', '//div[@id="loader"]')
# class не равен 'hidden'

success_message = ('xpath', '//p[@id="successMessage"]')
# class не равен 'hidden'

# add_remove
add_button = ('xpath', '//button[@onclick="addElement()"]')
remove_button = ('xpath', '//button[@class="added-manually"]')

#basic auth
basic_auth_success_text= ('xpath', '//div/h3')

#broken image
img = ('xpath', '//div/img')
not_found = ('xpath', '//h1[text()="Not Found"]')

#checkbox
checkbox = ('xpath', '//input[@type="checkbox"]')
checkbox_checked = ('xpath', '//input[@checked]')
checkbox_1 = ('xpath', '(//input[@type="checkbox"])[1]')
checkbox_2 = ('xpath', '(//input[@type="checkbox"])[2]')