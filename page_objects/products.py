import data
from selenium import webdriver
from selenium.webdriver.common.by import By


class Products:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def validate_item_name(self):
        driver = self.driver
        item_title = driver.find_element(By.XPATH, '//h1').text
        assert item_title == data.MENS_COLLECTION_ITEMS.keys()[2]
