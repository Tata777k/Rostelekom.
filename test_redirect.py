import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
import random
import time
from conftest import *
from pages import *

@pytest.mark.parametrize("product_url", [
        'http://lk.rt.ru', 'https://lk.rt.ru',
        'http://my.rt.ru', 'https://my.rt.ru',
        'http://start.rt.ru', 'https://start.rt.ru',
        'http://lk.smarthome.rt.ru', 'https://lk.smarthome.rt.ru',
#        'http://key.rt.ru', 'https://key.rt.ru', #не рабо
])
def test_redir(web_browser, product_url):
    """Проверка редирект на https страницу
    """
    web_browser.get(product_url);
    wait = WebDriverWait(web_browser, 10)
    wait.until(EC.url_contains('https://b2c.passport.rt.ru'))
    wait.until(EC.title_contains('Ростелеком'))
    assert web_browser.current_url.startswith('https://b2c.passport.rt.ru/')


@pytest.mark.parametrize("product_url", [
        'http://key.rt.ru', 'https://key.rt.ru',
])
def test_redir_key(web_browser, product_url):
    """Проверка редирект на https страницу
    """
    web_browser.get(product_url);
    wait = WebDriverWait(web_browser, web_browser.my_timeout)
    web_browser.find_element(By.CLASS_NAME,'go_kab').click()
    wait.until(EC.url_contains('https://b2c.passport.rt.ru'))
    wait.until(EC.title_contains('Ростелеком'))
    assert web_browser.current_url.startswith('https://b2c.passport.rt.ru/')
    

@pytest.mark.parametrize("product_url", [
        'https://start.rt.ru',
        'https://lk.rt.ru',
        'https://my.rt.ru',
        'https://lk.smarthome.rt.ru',
])
def test_authorisation_email2(web_browser, product_url, user):
    web_browser.get(product_url);
    wait = WebDriverWait(web_browser, web_browser.my_timeout)
    AuthByCodePage(web_browser, wait).go_to_password_auth()
    auth_by_pass_page = AuthByPassPage(web_browser, wait)
    auth_by_pass_page.tap_email().send_acc(user.email).send_pass(user.password).click_login_button()
    check_user_logged_in(web_browser, user)
    log_out(web_browser)

def rwait():
    time.sleep(random.uniform(2,6))

def check_user_logged_in(web_browser, user):
    assert f"{user.human_name}" != ""
    wait = WebDriverWait(web_browser, web_browser.my_timeout)
    wait.until(lambda driver: driver.find_elements(By.XPATH,f"//*[contains(text(), {user.human_name})]") or driver.find_elements(By.PARTIAL_LINK_TEXT, 'Перейти'))
    if web_browser.find_elements(By.PARTIAL_LINK_TEXT, 'Перейти'):
       web_browser.find_element(By.PARTIAL_LINK_TEXT, 'Перейти').click()
    
    wait.until(EC.visibility_of_element_located((By.XPATH,f"//*[contains(text(), {user.human_name})]")))

def log_out(web_browser):
    web_browser.delete_all_cookies() #не раб без домена
    web_browser.get('https://b2c.passport.rt.ru/');
    wait = WebDriverWait(web_browser, web_browser.my_timeout)
    rwait()
    wait.until(EC.visibility_of_element_located((By.ID,'logout-btn'))).click()
    wait.until(EC.visibility_of_element_located((By.ID,'username')))


@pytest.mark.parametrize("product_url", [
       'https://key.rt.ru'
])
def test_authorisation_email_key(web_browser, product_url, user):
    web_browser.get(product_url);
    wait = WebDriverWait(web_browser, web_browser.my_timeout)
    KeyAuthPage(web_browser, wait).goto_login()
    AuthByCodePage(web_browser, wait).go_to_password_auth()
    auth_by_pass_page = AuthByPassPage(web_browser, wait)
    auth_by_pass_page.tap_email().send_acc(user.email).send_pass(user.password).click_login_button()
    check_user_logged_in(web_browser, user)
    log_out(web_browser)


@pytest.mark.parametrize("product_url", [
        #'https://lk.rt.ru',
        'https://my.rt.ru',
        #'https://start.rt.ru',
        #'https://lk.smarthome.rt.ru',
])
def test_authorisation_login(web_browser, product_url, user):
    web_browser.get(product_url);
    wait = WebDriverWait(web_browser, web_browser.my_timeout)
    wait.until(EC.url_contains('https://b2c.passport.rt.ru'))
    wait.until(EC.title_contains('Ростелеком'))
    wait.until(EC.visibility_of_element_located((By.ID,'standard_auth_btn'))).click()
    wait.until(EC.visibility_of_element_located((By.ID,'t-btn-tab-login'))).click()
    web_browser.find_element(By.ID, 'username').send_keys(user.login)
    # Вводим пароль
    web_browser.find_element(By.ID, 'password').send_keys(user.password)
    web_browser.find_element(By.ID,'kc-login').click()
    check_user_logged_in(web_browser, user)
    log_out(web_browser)
    
@pytest.mark.parametrize("product_url", [

       'https://key.rt.ru', #не рабо
])
def test_authorisation_login_key(web_browser, product_url, user):
    web_browser.get(product_url);
    wait = WebDriverWait(web_browser, web_browser.my_timeout)
    KeyAuthPage(web_browser, wait).goto_login()
    AuthByCodePage(web_browser, wait).go_to_password_auth()
    AuthByPassPage(web_browser, wait).tap_login().send_acc(user.login).send_pass(user.password).click_login_button()
    check_user_logged_in(web_browser, user)
    log_out(web_browser)



@pytest.mark.parametrize("product_url", [
        #'https://lk.rt.ru',
        'https://my.rt.ru',
        #'https://start.rt.ru',
        #'https://lk.smarthome.rt.ru',
])
def test_authorisation_phone(web_browser, product_url, user):
    web_browser.get(product_url);
    wait = WebDriverWait(web_browser, web_browser.my_timeout)
    rwait()
    AuthByCodePage(web_browser, wait).go_to_password_auth()
    rwait()
    AuthByPassPage(web_browser, wait).tap_phone().send_acc(user.phone).send_pass(user.password).click_login_button()
    log_out(web_browser)
    
    
@pytest.mark.parametrize("product_url", [
       'https://key.rt.ru'
])
def test_authorisation_phone_key(web_browser, product_url, user):
    web_browser.get(product_url);
    wait = WebDriverWait(web_browser, web_browser.my_timeout)
    KeyAuthPage(web_browser, wait).goto_login();
    AuthByCodePage(web_browser, wait).go_to_password_auth();
    AuthByPassPage(web_browser, wait).tap_phone().send_acc(user.phone).send_pass(user.password).click_login_button()
    check_user_logged_in(web_browser, user)
    log_out(web_browser)
    

@pytest.mark.parametrize("product_url", [
        'https://lk.rt.ru',
        'https://my.rt.ru',
        'https://start.rt.ru',
        'https://lk.smarthome.rt.ru'
])
def test_authorisation_badpass(web_browser, product_url, user):
    web_browser.get(product_url);
    wait = WebDriverWait(web_browser, web_browser.my_timeout)
    AuthByCodePage(web_browser, wait).go_to_password_auth()
#    wait.until(EC.url_contains('https://b2c.passport.rt.ru'))
#    wait.until(EC.title_contains('Ростелеком'))
#    wait.until(EC.visibility_of_element_located((By.ID,'standard_auth_btn'))).click()
    rwait()
    wait.until(EC.visibility_of_element_located((By.ID,'t-btn-tab-phone'))).click()
    web_browser.find_element(By.ID, 'username').send_keys(user.phone)
    # Вводим пароль
    rwait()
    web_browser.find_element(By.ID, 'password').send_keys(user.badpass)
    web_browser.find_element(By.ID,'kc-login').click()
    assert wait.until(EC.visibility_of_element_located((By.ID, 'form-error-message')))
    


@pytest.mark.parametrize("product_url", [
        'https://lk.rt.ru',
        'https://start.rt.ru',

])
@pytest.mark.parametrize("tabka1, acc_data, tabka2", [
        #куда_сначала  что_ввели  где_оказались
        (phoneTab,"+79991112233",phoneTab),
        (mailTab,"+79991112233",phoneTab),
        pytest.param(loginTab,"+79991112233",phoneTab, marks=pytest.mark.xfail(reason='bug')),
        pytest.param(lsTab,"+79991112233",phoneTab, marks=pytest.mark.xfail(reason='bug')),
        (phoneTab,"xpeHb@yandex.ru",mailTab),
        (mailTab,"xpeHb@yandex.ru",mailTab),
        (loginTab,"xpeHb@yandex.ru",mailTab),
        pytest.param(lsTab,"xpeHb@yandex.ru",mailTab, marks=pytest.mark.xfail(reason='bug')),
        (loginTab,"rtkid_6669", loginTab),
        (phoneTab,"rtkid_6669",loginTab),
        (mailTab,"rtkid_6669",loginTab),
        pytest.param(lsTab,"rtkid_6669",loginTab, marks=pytest.mark.xfail(reason='bug')),
        (lsTab,"123456789012", lsTab),
        (loginTab,"123456789012", lsTab),
        pytest.param(phoneTab,"123456789012", lsTab, marks=pytest.mark.xfail(reason='bug')),
        (mailTab,"123456789012", lsTab)
        #pytest.param(,,, marks=pytest.mark.xfail(reason='bug'))
])
def test_switch_tab(web_browser, product_url, user, tabka1, acc_data, tabka2):
    web_browser.get(product_url);
    wait = WebDriverWait(web_browser, web_browser.my_timeout)
    AuthByCodePage(web_browser, wait).go_to_password_auth()
    wait.until(EC.visibility_of_element_located(tabka1.locator)).click()
    assert "rt-tab--active" in web_browser.find_element(By.ID, tabka1.id).get_attribute("class")
    web_browser.find_element(By.ID, 'username').click()
    web_browser.find_element(By.ID, 'username').send_keys(acc_data)
    web_browser.find_element(By.ID, 'password').click()
    web_browser.find_element(By.ID, 'password').send_keys(user.password)
    assert "rt-tab--active" in web_browser.find_element(By.ID, tabka2.id).get_attribute("class")

def test_logout_start(web_browser, user):
    web_browser.get('https://start.rt.ru');
    wait = WebDriverWait(web_browser, web_browser.my_timeout)
    wait.until(EC.url_contains('https://b2c.passport.rt.ru'))
    wait.until(EC.title_contains('Ростелеком'))
    wait.until(EC.visibility_of_element_located((By.ID,'standard_auth_btn'))).click()
    wait.until(EC.visibility_of_element_located((By.ID,'t-btn-tab-login'))).click()
    web_browser.find_element(By.ID, 'username').send_keys(user.login)
    web_browser.find_element(By.ID, 'password').send_keys(user.password)
    web_browser.find_element(By.ID,'kc-login').click()
    check_user_logged_in(web_browser, user)
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'h2'))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH,f"//*[contains(text(), 'Выйти')]"))).click()

    
def test_logout_smarthome(web_browser, user):
    web_browser.get('https://lk.smarthome.rt.ru');
    wait = WebDriverWait(web_browser, web_browser.my_timeout)
    wait.until(EC.url_contains('https://b2c.passport.rt.ru'))
    wait.until(EC.title_contains('Ростелеком'))
    wait.until(EC.visibility_of_element_located((By.ID,'standard_auth_btn'))).click()
    wait.until(EC.visibility_of_element_located((By.ID,'t-btn-tab-login'))).click()
    web_browser.find_element(By.ID, 'username').send_keys(user.login)
    web_browser.find_element(By.ID, 'password').send_keys(user.password)
    web_browser.find_element(By.ID,'kc-login').click()
    check_user_logged_in(web_browser, user)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/header/div/div[2]/a'))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH,f"//*[contains(text(), 'Выйти')]"))).click()

  
  
@pytest.mark.parametrize("product_url", [
        'https://lk.rt.ru',
        'https://my.rt.ru',
        'https://start.rt.ru',
]) 
def test_authorisation_badlogin(web_browser, product_url, user):
    web_browser.get('https://b2c.passport.rt.ru');
    wait.until(EC.visibility_of_element_located((By.ID,'standard_auth_btn'))).click() #войти с паролем
    rwait()
    wait.until(EC.visibility_of_element_located((By.ID,'t-btn-tab-phone'))).click()
    web_browser.find_element(By.ID, 'username').send_keys(user.badlogin)
    rwait()
    web_browser.find_element(By.ID, 'password').send_keys(user.password)
    web_browser.find_element(By.ID,'kc-login').click()
    assert  wait.until(EC.visibility_of_element_located((By.ID, 'form-error-message')))
    

def test_password_change(web_browser, user, capsys):
    wait = WebDriverWait(web_browser, web_browser.my_timeout)
    web_browser.get('https://b2c.passport.rt.ru/');
    AuthByPassPage(web_browser, wait).click_forgot_password_button()
    rpp = RestorePassPage(web_browser, wait)
    rpp.tap_email().send_acc(user.email)
    with capsys.disabled():
        rpp.read_and_send_captcha()
        rpp.click_reset_button()
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'rt-radio__label')))
    web_browser.find_elements(By.CLASS_NAME,'rt-radio__label')[1].click()
    web_browser.find_elements(By.XPATH, '//button')[0].click()
    assert wait.until(EC.visibility_of_element_located((By.ID, 'rt-code-0')))


def generatioon_captcha():
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    length = int(7)
    password =''
    for i in range(length):
        password += random.choice(chars)
    return password
    
def test_password_select_captcha(web_browser,user):
    wait = WebDriverWait(web_browser, web_browser.my_timeout)
    web_browser.get('https://b2c.passport.rt.ru/');
    AuthByPassPage(web_browser, wait).click_forgot_password_button()
    rpp = RestorePassPage(web_browser, wait)
    rpp.tap_email().send_acc(user.email)
    password = generatioon_captcha()
    wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="captcha"]'))).send_keys(password)
    wait.until(EC.visibility_of_element_located((By.ID,"reset"))).click()
    wait.until(EC.visibility_of_element_located((By.ID, 'form-error-message')))
    


def test_captcha_appears(web_browser,user):
    web_browser.get('https://b2c.passport.rt.ru');
    wait = WebDriverWait(web_browser, web_browser.my_timeout)
    max_without_captcha = 3
    for i in range(max_without_captcha):
        wait.until(EC.visibility_of_element_located((By.ID,'t-btn-tab-login'))).click()
        if web_browser.find_elements(By.XPATH,'//*[@id="captcha"]'):
            break
        web_browser.find_element(By.ID, 'username').send_keys(user.login)
        rwait()
        web_browser.find_element(By.ID, 'password').send_keys(user.badpass)
        loginButton = web_browser.find_element(By.ID,'kc-login')
        loginButton.click()

    wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="captcha"]')))
    
