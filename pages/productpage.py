from selenium.webdriver.common.by import By
from pages.basepage import BasePage

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button_by_name = "add-to-cart"

    def add_to_cart(self):
        obj_base_page = BasePage(self.driver)
        obj_base_page.wait_page_load()
        obj_base_page.click_button_name(self.add_to_cart_button_by_name)
        # self.driver.find_element(By.NAME, self.add_to_cart_button_by_name).click()
