from pages.testrailpage import TestRailPage
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators
from pages.basepage import BasePage


class CartPage:
    """ Check for added fields in cart page is done here """
    def __init__(self, driver):
        self.driver = driver
        self.cart_delete_button_by_xpath = Locators.cart_delete_xpath
        self.table_class_name = Locators.table_class_name_xpath
        self.cart_row_xpath = Locators.cart_row_xpath

    def clear_cart(self):
        """ For clearing elements in cart """
        obj_base_page = BasePage(self.driver)
        table = self.driver.find_elements(By.CLASS_NAME, self.table_class_name)
        if len(table) > 0:
            rows = self.driver.find_elements(By.CLASS_NAME, self.cart_row_xpath)
            for i in rows:

                obj_base_page.wait_page_load()
                obj_base_page.click_button_xpath(self.cart_delete_button_by_xpath)
                # try:
                #     element = WebDriverWait(self.driver, 100).until(
                #         EC.presence_of_all_elements_located((By.XPATH, self.cart_delete_button_by_xpath)))
                #     if len(element) > 0:
                #
                #         element[0].click()
                #         # time.sleep(.5)
                #         self.driver.refresh()
                #
                # except StaleElementReferenceException as e:
                #     self.driver.implicitly_wait(5)
                #     self.driver.find_element(By.XPATH, self.cart_delete_button_by_xpath).click()
                # except ElementClickInterceptedException as e:
                #     element = self.driver.find_element(By.XPATH, self.cart_delete_button_by_xpath)
                #     self.driver.execute_script("arguments[0].scrollIntoView();", element)
                    # element.click()
