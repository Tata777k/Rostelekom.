from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By

class AuthByCodePage:
    password_auth_button_id = 'standard_auth_btn'
    get_code_button_id = 'otp_get_code'

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def go_to_password_auth(self):
        self.wait.until(EC.url_contains('https://b2c.passport.rt.ru'))
        self.wait.until(EC.title_contains('Ростелеком'))
        self.wait.until(EC.visibility_of_element_located((By.ID,self.password_auth_button_id))).click()

class AuthByPassPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def tap_email(self):
        self.wait.until(EC.visibility_of_element_located((By.ID,'t-btn-tab-mail'))).click()
        return self

    def tap_login(self):
        self.wait.until(EC.visibility_of_element_located((By.ID,'t-btn-tab-login'))).click()
        return self

    def tap_phone(self):
        self.wait.until(EC.visibility_of_element_located((By.ID,'t-btn-tab-phone'))).click()
        return self

    def send_acc(self, email):
        self.driver.find_element(By.ID, 'username').send_keys(email)
        return self

    def send_pass(self, password):
        self.driver.find_element(By.ID, 'password').send_keys(password)
        return self

    def click_login_button(self):
        self.driver.find_element(By.ID,'kc-login').click()

    def click_forgot_password_button(self):
        self.wait.until(EC.visibility_of_element_located((By.ID,'forgot_password'))).click()


class RestorePassPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def tap_email(self):
        self.wait.until(EC.visibility_of_element_located((By.ID,'t-btn-tab-mail'))).click()
        return self

    def tap_login(self):
        self.wait.until(EC.visibility_of_element_located((By.ID,'t-btn-tab-login'))).click()
        return self

    def tap_phone(self):
        self.wait.until(EC.visibility_of_element_located((By.ID,'t-btn-tab-phone'))).click()
        return self

    def send_acc(self, email):
        self.driver.find_element(By.ID, 'username').send_keys(email)
        return self

#    def send_pass(self, password):
#        self.driver.find_element(By.ID, 'password').send_keys(password)
#        return self
    def read_and_send_captcha(self):
        if self.driver.find_elements(By.ID, 'captcha'):
            captcha = input("введите капчу: ")
            self.driver.find_element(By.ID, 'captcha').send_keys(captcha)
        return self

    def click_reset_button(self):
        self.driver.find_element(By.ID,'reset').click()

class KeyAuthPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def goto_login(self):
        self.driver.find_element(By.CLASS_NAME,'go_kab').click()






