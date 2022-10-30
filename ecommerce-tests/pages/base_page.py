
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class BasePage():

    def __init__(self, driver):
        """ This function is called every time a new object of the base class is created"""
        self.driver = driver

    def click(self, by_locator):
        """ Performs click on web element whose locator is passed to it"""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(by_locator)).click()

    def enter_text(self, by_locator, text):
        """ Performs text entry of the passed in text, in a web element whose locator is passed to it"""
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_title(self) -> str:
        """Returns the title of the page"""
        return self.driver.title

    def get_url_page(self) -> str:
        """Returns the title of the page"""
        return self.driver.current_url

    def get_component_text(self, by_locator) -> str:
        """Returns the text of any component"""
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text

    def get_filter_to_page(self, text):
        menu_dropdown = Select(self.driver.find_element(By.CLASS_NAME, 'product_sort_container'))
        value_selected = menu_dropdown.select_by_value(text)

        return value_selected