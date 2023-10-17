from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckOut(BasePage):
    checkout = (By.ID, 'checkout')
    first_name_field = (By.ID, 'first-name')
    last_name_field = (By.ID, 'last-name')
    zip_code_field = (By.ID, 'postal-code')
    continue_button = (By.ID, 'continue')
    finish_button = (By.ID, 'finish')

    first_name_keys = 'Dele'
    last_name_keys = 'Ali'
    zip_code_keys = '120036'

    def __init__(self, driver):
        super().__init__(driver)










