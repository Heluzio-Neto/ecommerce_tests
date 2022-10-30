from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.carrinho = (By.CLASS_NAME, 'shopping_cart_link')
        self.item = (By.ID,'add-to-cart-sauce-labs-fleece-jacket')
        
    def buy_item_high_price(self):
        self.get_filter_to_page("hilo")
        #self.click(self.item)
        items = self.driver.find_elements(By.CLASS_NAME,'btn btn_primary btn_small btn_inventory')

        for e in items:
            print(e)
            break

        self.click(self.carrinho)