from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utilities.test_data import TestData


class ProductsPage(BasePage):

    product1_add_to_cart_field = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    product2_add_to_cart_field = (By.ID, 'add-to-cart-sauce-labs-bike-light')
    shopping_cart_link = (By.CLASS_NAME, 'shopping_cart_link')

    def __init__(self):
        super().__init__(self)

    def add_to_cart(self,add_locator):
        self.click(add_locator)
        self.click(self.shopping_cart_link)

cart = ProductsPage()
cart.add_to_cart(TestData.product1_add_to_cart_field)









