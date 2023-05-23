from locators.locators import Locators
from selenium.webdriver.common.by import By
from pages.basepage import BasePage

class ThankYouPage:
    """ Check for added fields in thank you page is done here """

    def __init__(self, driver):
        self.driver = driver
        self.shipping_address_xpath = Locators.shipping_address_xpath
        self.billing_address_xpath = Locators.billing_address_xpath

    def edit_field(self, field_val, section_type, action_type, field_label="", field_default_value=""):
        obj_base_page = BasePage(self.driver)
        if action_type == 'create':

            label = self.driver.find_elements(By.XPATH, "//th[text()='"+field_label+":']")
            obj_base_page.wait_page_load()
            input_val = self.driver.find_elements(By.XPATH, "//td[text()='"+field_val+"']")
            obj_base_page.wait_page_load()
            if len(label) >0 and len(input_val) > 0:
                return True, "Field found with entered value"
            else:
                # print(1)
                return False, "Field not found with entered value"
        else:
            if field_val == "KL":
                field_val = "Kerala"
            if section_type == "shipping":
                input_val = self.driver.find_elements(By.XPATH, self.shipping_address_xpath)
                obj_base_page.wait_page_load()
                if len(input_val) > 0:
                    if field_val in input_val[0].text:
                        return True, "Element found with entered value"
                    else:
                        return False, "Element not found with entered value"
                else:
                    return False, "Element not found"
            elif section_type == "additional":
                input_val = self.driver.find_elements(By.XPATH, "//td[text()='"+field_val+"']")
                obj_base_page.wait_page_load()
                if len(input_val) > 0:
                    return True, "Element found with entered value"
                else:
                    return False, "Element not found with entered value"
            else:
                input_val = self.driver.find_elements(By.XPATH, self.billing_address_xpath)
                obj_base_page.wait_page_load()

                if len(input_val) > 0:
                    if field_val in input_val[0].text:
                        return True, "Element found with entered value"
                    else:
                        return False, "Element not found with entered value"
                else:
                    return False, "Element not found"

    def check_order_page(self, field_label, field_input, case_type):
        obj_base_page = BasePage(self.driver)
        label_val = self.driver.find_elements(By.XPATH, "//th[text()='" + field_label + ":']")
        obj_base_page.wait_page_load()
        input_val = self.driver.find_elements(By.XPATH, "//td[text()='" + field_input + "']")
        obj_base_page.wait_page_load()
        # print(label_val, input_val, field_input)
        if len(label_val) > 0 and len(input_val) > 0:
            if case_type == "enable":
                return True, "Entered element found"
            else:
                return False, "Entered element not found"
        else:
            if case_type == "enable":
                return False, "Entered element found"
            else:
                return True, "Entered element not found"

    def check_default_value(self, field_default_value, test_case_type):
        obj_base_page = BasePage(self.driver)
        default_val = self.driver.find_elements(By.XPATH, "//td[normalize-space()='"+field_default_value+"']")
        obj_base_page.wait_page_load()
        if len(default_val) > 0:
            if test_case_type == "valid":
                return True, "Entered element found for valid case"
            else:
                return False, "Entered element found for invalid case"
        else:
            if test_case_type == "valid":
                return False, "Entered element not found for valid"
            else:
                return True, "Entered element not found for invalid case"

    def check_label(self, field_label):
        obj_base_page = BasePage(self.driver)
        element = self.driver.find_elements(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/main/article/div[1]/div/div/section[1]/table[2]/tbody/tr/th")
        # print(element)
        obj_base_page.wait_page_load()
        if len(element) > 0:
            # print(element[0].text)
            if field_label in element[0].text:
                return True, "Element Found"
            else:
                return False, "Element not Found"
        else:
            return False, "Element not Found"
