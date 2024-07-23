import data
from actions.actions import Actions
from selenium import webdriver
from selenium.webdriver.common.by import By

PRODUCT_CARD_XPATH = '//div[@class="grid-view-item product-card"]'


class Men:
    collectionsActions = Actions

    def __init__(self, driver):
        self.collectionsActions = Actions(driver)

    def visit_first_item(self):
        self.collectionsActions.click_element_from_list_by_xpath(PRODUCT_CARD_XPATH, 1)

    # def visit_item_by_key_name(self, key_name):
    #     driver = self.driver
    #     driver.find_element(By.LINK_TEXT, data.MENS_COLLECTION_ITEMS.keys()[2]).click()
    #     current_url = driver.current_url
    #     assert data.BOWERY_CHINO_PANTS_SLUG in current_url

