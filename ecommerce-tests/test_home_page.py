from time import sleep
import unittest

from selenium.webdriver import Firefox

from pages.login_page import LoginPage
from pages.home_page import HomePage


class TestHomePage(unittest.TestCase):
    def setUp(self):
        self.driver = Firefox()
        self.login_page = LoginPage(self.driver)
        self.inventory_page = HomePage(self.driver)
        self.driver.get('https://www.saucedemo.com/')

    def test_buy_hilo_success(self):
        self.login_page.autenticar('standard_user', 'secret_sauce')
        self.inventory_page.buy_item_high_price()
        pagina_esperada = self.login_page.get_url_page()
        self.assertIn('cart', pagina_esperada)

    
    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
