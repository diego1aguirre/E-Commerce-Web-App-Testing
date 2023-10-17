from selenium.webdriver.common.by import By
from selenium import webdriver
from utilities.test_data import TestData

class BasePage:
    def __init__(self,driver):
        self.driver = webdriver.Firefox()

    def open_page(self, url):
        self.driver.get(url)

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(*locator).click()

    def set(self,locator,value):
        self.find(*locator).send_keys(value)
    def get_text(self, locator):
        return self.find(*locator).text








