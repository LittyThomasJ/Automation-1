from locators.locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.basepage import BasePage


class AdminOrderPage:
    """ Check for added fields in cart page is done here """
    def __init__(self, driver):
        self.driver = driver
        self.view_admin_order_button_by_class_name = Locators.admin_order_class_name_xpath
        self.billing_order_data = Locators.billing_order_data_xpath
        self.order_data = Locators.order_data_xpath

    def edit_field(self, field_val, field_name, section_type, action_type, field_label=""):
        obj_base_page = BasePage(self.driver)
        obj_base_page.wait_page_load()
        obj_base_page.click_button_class(self.view_admin_order_button_by_class_name)
        obj_base_page.wait_page_load()
        # admin_order_button = self.driver.find_elements(By.CLASS_NAME, self.view_admin_order_button_by_class_name)
        # if len(admin_order_button) > 0:
        #     admin_order_button[0].click()
        if action_type == "create":

            element = self.driver.find_elements(By.XPATH, "//p[contains(.,'"+field_label+": "+field_val+"')]")
            if len(element) > 0:
                return True, "Element found"
            else:
                return False, "Element not found"
        else:
            if field_name == "billing_phone":
                phone = self.driver.find_elements(By.XPATH, "//a[@href='tel:"+field_val+"']")
                if len(phone) > 0:
                    return True, "Element found"
                else:
                    return False, "Element not found"
            elif field_name == "billing_email":
                email = self.driver.find_elements(By.XPATH, "//a[@href='mailto:"+field_val+"']")
                if len(email) > 0:
                    return True, "Element found"
                else:
                    return False, "Element not found"
            else:
                if field_val == "KL":
                    field_val = "Kerala"
                if section_type == "billing":
                    obj_base_page.wait_page_load()
                    value = self.driver.find_elements(By.XPATH, self.billing_order_data)
                    if len(value) > 0:
                        val = value[0].text
                else:
                    value = self.driver.find_elements(By.XPATH, self.order_data)
                    if len(value) > 0:
                        val = value[0].text
                if field_val in val:
                    return True, "Element found"
                else:
                    return False, "Element not found"
        # else:
        #     # print("No Admin Order Button")
        #     return False, "Admin order button not found"
