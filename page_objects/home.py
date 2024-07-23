import data
from actions.actions import Actions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

COLLECTIONS_XPATH = '//div[@class="collection-grid-item"]'
SUBSCRIBE_INPUT = '//input[@id="ContactFooter-email"]'
SUBSCRIBE_BUTTON = '//button[@id="Subscribe"]'


class Home:
    homePageActions = Actions

    def __init__(self, driver):
        self.homePageActions = Actions(driver)

    def visit_home(self):
        home_page = self.homePageActions
        home_page.visit_url(data.BASE_URL)
        home_page.get_current_url()
        home_page.assert_current_url(data.BASE_URL)

    def resize_home_window(self, width, height):
        self.homePageActions.resize_window(width, height)

    def assert_home_domain(self):
        self.homePageActions.assert_domain(data.BASE_URL, data.DOMAIN)

    def assert_logo(self):
        pass
        # TODO: Usar expected conditions
        # madison_island_logo = driver.find_element(By.CLASS_NAME, 'site-header__logo-link')
        # current_logo_text = madison_island_logo.text
        # assert current_logo_text == data.LOGO_TEXT

    def press_page_down(self):
        self.homePageActions.press_key_page_down()

    def click_women_collection(self):
        self.homePageActions.click_element_from_list_by_xpath(COLLECTIONS_XPATH, 0)

    def click_men_collection(self):
        self.homePageActions.click_element_from_list_by_xpath(COLLECTIONS_XPATH, 1)

    def subscribe_to_newsletter(self):
        self.homePageActions.input_text_by_xpath(data.TEST_EMAIL, SUBSCRIBE_INPUT)
        self.homePageActions.click_element_by_xpath(SUBSCRIBE_BUTTON)
