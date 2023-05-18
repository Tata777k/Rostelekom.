import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="session")
def web_browser():
    driver = webdriver.Chrome(executable_path="./chromedriver")
#    driver.my_timeout = 70
    driver.my_timeout = 20
    yield driver
    driver.quit()

class Tab:
    def __init__(self, id):
        self.id = id
        self.locator=(By.ID, id)
        name = id[ id.rfind('-')+1 :]
        self.__name__ = f"tab_{name}"

phoneTab = Tab('t-btn-tab-phone')
mailTab = Tab('t-btn-tab-mail')
loginTab = Tab('t-btn-tab-login')
lsTab = Tab('t-btn-tab-ls')

class User:
    pass

@pytest.fixture(scope="session")
def user():
    u = User()
    u.email = 'iva.gla7@gmail.com'
    u.password = 'gk.ifCbkf'
    u.badpass = 'reqyz,kby'
    u.human_name = 'Ипполит'
    u.login = 'rtkid_1683569115151'
    u.badlogin = 'rtkid_6666666666666'
    u.phone = '+79040528600'
    return u

