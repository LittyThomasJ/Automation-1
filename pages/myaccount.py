from locators.locators import Locators
from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class MyAccount:
    """ Actions in my-account page is done here"""

    def __init__(self, driver):
        self.driver = driver
        self.logout_xpath = Locators.logout_xpath

    def logout(self):
        obj_base_page = BasePage(self.driver)
        obj_base_page.wait_page_load()
        obj_base_page.click_button_xpath(self.logout_xpath)
        # self.driver.find_element(By.XPATH, self.logout_xpath).click()
