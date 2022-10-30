from time import sleep
import unittest

from selenium.webdriver import Firefox

from pages.login_page import LoginPage


class TestLoginPage(unittest.TestCase):
    def setUp(self):
        self.driver = Firefox()
        self.login_page = LoginPage(self.driver)
        self.driver.get('https://www.saucedemo.com/')

    def test_login_success(self):
        self.login_page.autenticar('standard_user', 'secret_sauce')
        pagina_esperada = self.login_page.get_url_page()
        self.assertIn('inventory', pagina_esperada)

    def test_login_empty(self):
        self.login_page.autenticar('', '')
        self.assertTrue(self.login_page.verificar_erro(
            'Epic sadface: Username is required'))

    def test_user_empty(self):
        self.login_page.autenticar('standard_user', '')
        self.assertTrue(self.login_page.verificar_erro(
            'Epic sadface: Password is required'))
    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
