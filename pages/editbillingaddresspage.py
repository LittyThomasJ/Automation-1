import time
from locators.locators import Locators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class EditBillingPage:
    """ Actions in edit billing address is done here"""
    def __init__(self, driver):
        self.driver = driver

    def check_edit_billing_address(self, field_name, field_input):
        obj_base_page = BasePage(self.driver)
        obj_base_page.wait_page_load()
        input_element = self.driver.find_elements(By.NAME, field_name)
        if len(input_element) > 0:
            input_val = input_element[0].get_attribute("value")
            if input_val in field_input:
                return True, "Field found with entered value"
            else:
                return False, "Field not found with entered value"
        else:
            return False, "Field not found"
