import data
from page_objects.home import Home
from page_objects.collections_men import Men
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestMenCollection:
    driver = None
    home = None
    men = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.home = Home(cls.driver)
        cls.men = Men(cls.driver)
        cls.home.visit_home()
        cls.home.resize_home_window(1600, 1080)

    def test_men_collection_happy_path(self):
        home_page = self.home
        men_collection = self.men
        home_page.assert_home_domain()
        home_page.press_page_down()
        home_page.click_men_collection()
        men_collection.visit_first_item()

    @classmethod
    def teardown_class(cls):
        sleep(2)
        cls.driver.quit()


# print(data.MENS_COLLECTION_ITEMS['BOWERY CHINO PANTS'])
# men.visit_item_by_key_name(data.MENS_COLLECTION_ITEMS['BOWERY CHINO PANTS'])

#
# item_title = driver.find_element(By.XPATH, '//h1').text
# assert item_title == data.ITEM_NAME_FOR_PURCHASE
#
# select_size = driver.find_element(By.XPATH, '//*[@id="SingleOptionSelector-0"]')
# select = Select(select_size)
# select.select_by_value('36')
#
# select_color = driver.find_element(By.XPATH, '//*[@id="SingleOptionSelector-1"]')
# select = Select(select_color)
# select.select_by_index(1)
#
# add_to_cart_button = driver.find_element(By.ID, 'AddToCartText-product-template')
# add_to_cart_current_text = add_to_cart_button.text
# assert add_to_cart_current_text.lower() == 'add to cart'
# add_to_cart_button.click()
#
# quantity_input = driver.find_element(By.XPATH, '//input[@name="updates[]"]')
# quantity_input.clear()
# quantity_input.send_keys('3')
# quantity_input.send_keys(Keys.RETURN)
# update_button = driver.find_element(By.NAME, 'update')
# article_total = driver.find_element(By.XPATH, '//div[contains(text(), "$420.00")]')
# assert article_total.text == '$420.00'
#
# driver.find_element(By.NAME, 'checkout').click()
# current_url = driver.current_url
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.visibility_of_element_located((By.ID, 'checkout-pay-button')))
# sleep(3)
# assert 'checkouts' in current_url
#
# sleep(2)
# driver.quit()