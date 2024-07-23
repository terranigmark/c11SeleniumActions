from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class Actions:

    def __init__(self, driver):
        self.driver = driver

    def visit_url(self, url):
        self.driver.get(url)

    def click_element_by_xpath(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        element.click()

    def click_element_from_list_by_xpath(self, locator, index):
        element = self.driver.find_elements(By.XPATH, locator)
        element[index].click()

    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    def assert_current_url(self, url):
        assert self.get_current_url() == url

    def resize_window(self, width, height):
        self.driver.set_window_size(width, height)

    def assert_domain(self, url, domain):
        driver = self.driver
        current_url = driver.current_url
        assert current_url == url
        assert domain in current_url

    def press_key_page_down(self):
        driver = self.driver
        ActionChains(driver).key_down(Keys.PAGE_DOWN).perform()

    def input_text_by_xpath(self, text, locator):
        driver = self.driver
        input_field = driver.find_element(By.XPATH, locator)
        input_field.send_keys(text)
