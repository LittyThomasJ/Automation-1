from locators.locators import Locators
from pages.basepage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutFormDesigner:
    """ All the actions done in checkout form designer page is done here"""

    def __init__(self, driver):
        self.driver = driver
        self.error_msg_noti_xpath = Locators.error_msg_noti_xpath
        self.check_label_xpath = Locators.check_label_xpath
        self.check_placeholder_xpath = Locators.check_placeholder_xpath
        self.saved_notification_xpath = Locators.saved_notification_xpath
        self.name_required_xpath = Locators.name_required_xpath
        self.label_override_xpath = Locators.label_override_xpath
        self.save_changes_xpath = Locators.save_changes_xpath
        self.class_override_xpath = Locators.class_override_xpath
        self.placeholder_override_xpath = Locators.placeholder_override_xpath
        self.required_override_xpath = Locators.required_override_xpath
        self.priority_override_xpath = Locators.priority_override_xpath

    def reset_field(self):
        obj_base_page = BasePage(self.driver)
        obj_base_page.wait_page_load()
        obj_base_page.refresh_page()
        obj_base_page.wait_page_load()
        obj_base_page.common_function("reset", "button_click")

    def add_label(self, field_label, case_type, section_type, action_type, row="", field_type="", field_name="",
                  option_value_one="", option_text_one="", option_value_two="", option_text_two="",
                  option_value_three="", option_text_three="", field_default_value="", field_content=""):
        obj_base_page = BasePage(self.driver)
        obj_base_page.wait_page_load()
        self.reset_field()
        obj_base_page.wait_page_load()
        if section_type in ["shipping", "additional"]:
            obj_base_page.common_function(section_type, "button_click")
            obj_base_page.wait_page_load()
        else:
            pass
        if action_type == "edit":
            obj_base_page.common_function("edit_field", "button_click", row=row)
            obj_base_page.wait_page_load()
        else:
            obj_base_page.common_function("add_field", "button_click")
            obj_base_page.wait_page_load()
            obj_base_page.common_function("field_type", "select", value=field_type)
            obj_base_page.wait_page_load()
            obj_base_page.common_function("field_name", "clear")
            if (field_name is not None) and (field_name != ""):
                obj_base_page.common_function("field_name", "send_keys", value=field_name)
                obj_base_page.wait_page_load()
            if field_type in ['select', 'radio', 'multiselect', 'checkboxgroup']:
                obj_base_page.common_function("option_value_one", "send_keys", value=option_value_one)
                obj_base_page.wait_page_load()
                obj_base_page.common_function("option_text_one", "send_keys", value=option_text_one)
                obj_base_page.wait_page_load()
                obj_base_page.common_function("add_option_one", "button_click")
                obj_base_page.wait_page_load()
                obj_base_page.common_function("option_value_two", "send_keys", value=option_value_two)
                obj_base_page.wait_page_load()
                obj_base_page.common_function("option_text_two", "send_keys", value=option_text_two)
                obj_base_page.wait_page_load()
                if (option_value_three is not None) and (option_value_three != ""):
                    obj_base_page.common_function("add_option_two", "button_click")
                    obj_base_page.wait_page_load()
                    obj_base_page.common_function("option_value_three", "send_keys", value=option_value_three)
                    obj_base_page.wait_page_load()
                    obj_base_page.common_function("option_text_three", "send_keys", value=option_text_three)
                    obj_base_page.wait_page_load()

        obj_base_page.common_function("field_label", "clear")
        if field_type == 'radio':
            pass
        else:
            obj_base_page.common_function("field_placeholder", "clear")
            obj_base_page.wait_page_load()
        if field_label is not None and field_label != "":
            obj_base_page.common_function("edit_label", "send_keys", value=field_label)
            obj_base_page.wait_page_load()
        if (field_default_value is not None) and (field_default_value != "") and field_type == "hidden":
            obj_base_page.common_function("default_value", "send_keys", value=field_default_value)
            obj_base_page.wait_page_load()
        if field_type == "paragraph":
            obj_base_page.send_keys_xpath("(//input[@name='i_label'])[1]", field_content)
        # time.sleep(1)
        obj_base_page.wait_page_load()
        obj_base_page.common_function("save_close", "button_click")
        obj_base_page.wait_page_load()
        if case_type == "without fieldname":
            notification = self.driver.find_elements(By.XPATH, self.error_msg_noti_xpath)
            obj_base_page.wait_page_load()
            if len(notification) > 0:
                if notification[0].text == 'Name is required':
                    return True, "Notification is correctly displayed"
                else:
                    return False, "Notification is not correctly displayed"
            else:
                return False, "Notification is not found"
        else:
            if action_type == 'edit':
                element = self.driver.find_elements(By.XPATH,
                                                    "//table[@id='thwcfd_checkout_fields']/tbody[1]/tr[" + str(
                                                        row) + "]/td[5]")
            elif field_type == "paragraph":
                # print("para")
                element = self.driver.find_elements(By.XPATH, "(//td[normalize-space()='"+field_name+"'])[1]")
            else:
                element = self.driver.find_elements(By.XPATH, self.check_label_xpath)
            obj_base_page.wait_page_load()
            notification = self.driver.find_elements(By.XPATH, self.saved_notification_xpath)
            # print(element, notification)
            if len(element) > 0 and len(notification) > 0:
                if case_type == "empty":
                    if element[0].text == '':
                        return True, "Expected result found"
                    else:
                        return False, "Notification found"
                else:
                    if field_type == "paragraph":
                        return True, "Entered field found on backend"
                    if field_label == element[0].text:
                        return True, "Entered Label is found on backend"
                    else:
                        return False, "Entered Label is not found on backend"
            else:
                return False, "Saved notification is not found on backend"

    def add_placeholder(self, field_placeholder, case_type, section_type, action_type, row="", field_type="",
                        field_name=""):
        obj_base_page = BasePage(self.driver)
        obj_base_page.wait_page_load()
        self.reset_field()
        obj_base_page.wait_page_load()
        if section_type in ["shipping", "additional"]:
            obj_base_page.common_function(section_type, "button_click")
            obj_base_page.wait_page_load()
        else:
            pass
        if action_type == "edit":
            obj_base_page.common_function("edit_field", "button_click", row=row)
            obj_base_page.wait_page_load()
        else:
            obj_base_page.common_function("add_field", "button_click")
            obj_base_page.wait_page_load()
            obj_base_page.common_function("field_type", "select", value=field_type)
            obj_base_page.wait_page_load()
            obj_base_page.common_function("field_name", "clear")
            if (field_name is not None) and (field_name != "") and (case_type != "without name"):
                obj_base_page.common_function("field_name", "send_keys", value=field_name)
                obj_base_page.wait_page_load()
        obj_base_page.common_function("field_placeholder", "clear")
        if field_placeholder is not None and field_placeholder != "":
            obj_base_page.common_function("placeholder", "send_keys", value=field_placeholder)
            obj_base_page.wait_page_load()
            # obj_base_page.add_placeholder(field_placeholder)
        # time.sleep(1)
        obj_base_page.common_function("save_close", "button_click")
        obj_base_page.wait_page_load()
        # obj_base_page.click_save_close()
        if case_type == "without fieldname":
            notification = self.driver.find_elements(By.XPATH, self.error_msg_noti_xpath)
            obj_base_page.wait_page_load()
            if len(notification) > 0:
                return True, "Notification is correctly displayed"
            else:
                return False, "Notification is not found"
        else:
            notification = self.driver.find_elements(By.XPATH, self.saved_notification_xpath)
            obj_base_page.wait_page_load()
            if action_type == 'edit':
                element = self.driver.find_elements(By.XPATH,
                    "//table[@id='thwcfd_checkout_fields']/tbody[1]/tr[" + str(row) + "]/td[6]")
            else:
                element = self.driver.find_elements(By.XPATH, self.check_placeholder_xpath)
            if len(element) > 0 and len(notification) > 0:
                if case_type == "empty":
                    if element[0].text == '':
                        return True, "Expected Result"
                    else:
                        return False, "Notification found"
                else:
                    if field_placeholder == element[0].text:
                        return True, "Placeholder is correctly displayed"
                    else:
                        return False, "Placeholder is not correctly displayed"
            else:
                return False, "Notification or element not found"

    def add_default_value(self, field_default_value, action_type, case_type, section_type, row="", field_type="",
                          field_name="", option_value_one="", option_text_one="", option_value_two="",
                          option_text_two="", option_value_three="", option_text_three="", field_label=""):
        obj_base_page = BasePage(self.driver)
        obj_base_page.wait_page_load()
        # time.sleep(2)
        self.reset_field()
        obj_base_page.wait_page_load()
        obj_base_page.wait_page_load()
        if section_type in ["shipping", "additional"]:
            obj_base_page.common_function(section_type, "button_click")
            obj_base_page.wait_page_load()
        else:
            pass
        if action_type == "edit":
            obj_base_page.common_function("edit_field", "button_click", row=row)
            obj_base_page.wait_page_load()
        else:
            obj_base_page.common_function("add_field", "button_click")
            obj_base_page.wait_page_load()
            obj_base_page.common_function("field_type", "select", value=field_type)
            obj_base_page.wait_page_load()
            obj_base_page.common_function("field_name", "clear")
            obj_base_page.wait_page_load()
            if field_label is not None and field_label != "":
                obj_base_page.common_function("edit_label", "send_keys", value=field_label)
                obj_base_page.wait_page_load()
            if (field_name is not None) and (field_name != "") and (case_type != "without name"):
                obj_base_page.common_function("field_name", "send_keys", value=field_name)
                obj_base_page.wait_page_load()
            if field_type in ["select", 'radio', 'multiselect', 'checkboxgroup']:
                obj_base_page.common_function("option_value_one", "send_keys",
                                              value=option_value_one)
                obj_base_page.wait_page_load()
                obj_base_page.common_function("option_text_one", "send_keys",
                                              value=option_text_one)
                obj_base_page.wait_page_load()
                obj_base_page.common_function("add_option_one", "button_click")
                obj_base_page.wait_page_load()
                obj_base_page.common_function("option_value_two", "send_keys",
                                              value=option_value_two)
                obj_base_page.wait_page_load()
                obj_base_page.common_function("option_text_two", "send_keys",
                                              value=option_text_two)
                obj_base_page.wait_page_load()
                obj_base_page.common_function("add_option_two", "button_click")
                obj_base_page.wait_page_load()
                obj_base_page.common_function("option_value_three", "send_keys",
                                              value=option_value_three)
                obj_base_page.wait_page_load()
                obj_base_page.common_function("option_text_three", "send_keys",
                                              value=option_text_three)
                obj_base_page.wait_page_load()

        if field_default_value is not None and field_default_value != "":
            if field_type is not None:
                obj_base_page.common_function("default_value", "send_keys", value=field_default_value, section_type=section_type, field_type=field_type)
            else:
                obj_base_page.common_function("default_value", "send_keys", value=field_default_value, section_type=section_type)
            obj_base_page.wait_page_load()
        # time.sleep(1)
        obj_base_page.common_function("save_close", "button_click")
        obj_base_page.wait_page_load()
        if case_type == "without fieldname":
            notification = self.driver.find_elements(By.XPATH, self.error_msg_noti_xpath)
            obj_base_page.wait_page_load()
            if len(notification) > 0:
                return True, "Notification is correctly displayed"
            else:
                return False, "Notification is not found"
        elif case_type == "invalid":
            notification = self.driver.find_elements(By.XPATH, self.error_msg_noti_xpath)
            obj_base_page.wait_page_load()
            if len(notification) > 0:
                return True, "Notification found"
            else:
                return False, "Notification is not found"
        else:
            element = self.driver.find_elements(By.XPATH, self.saved_notification_xpath)
            obj_base_page.wait_page_load()
            if len(element) > 0:
                return True, "Notification is found"
            else:
                return False, "Notification is not found"

    def add_field_class(self, field_class, section_type, action_type, row="", field_type="", field_label="", field_name="", field_content=""):
        obj_base_page = BasePage(self.driver)
        obj_base_page.wait_page_load()
        self.reset_field()
        obj_base_page.wait_page_load()
        if section_type in ["shipping", "additional"]:
            obj_base_page.common_function(section_type, "button_click")
            obj_base_page.wait_page_load()
        else:
            pass
        if action_type == "edit":
            obj_base_page.common_function("edit_field", "button_click", row=row)
            obj_base_page.wait_page_load()
        else:
            obj_base_page.common_function("add_field", "button_click")
            obj_base_page.wait_page_load()
            obj_base_page.common_function("field_type", "select", value=field_type)
            obj_base_page.wait_page_load()
            obj_base_page.common_function("field_name", "clear")
            obj_base_page.wait_page_load()
            if (field_name is not None) and (field_name != ""):
                obj_base_page.common_function("field_name", "send_keys", value=field_name)
                obj_base_page.wait_page_load()
            if (field_label is not None) and (field_label != "") and (field_type == "heading"):
                obj_base_page.common_function("edit_label", "send_keys", value=field_label)
                obj_base_page.wait_page_load()
        if field_class is not None and field_class != "":
            obj_base_page.common_function("field_class", "clear")
            obj_base_page.common_function("field_class", "send_keys", value=field_class)
            obj_base_page.wait_page_load()
        if field_type == "paragraph":
            obj_base_page.send_keys_xpath("(//input[@name='i_label'])[1]", field_content)
        # time.sleep(1)
        obj_base_page.common_function("save_close", "button_click")
        obj_base_page.wait_page_load()
        element = self.driver.find_elements(By.XPATH, self.saved_notification_xpath)
        obj_base_page.wait_page_load()
        if len(element) > 0:
            return True,  "Notification is found"
        else:
            return False, "Notification is not found"

    def add_field_validation(self, validation_type, section_type, field_name, action_type, row="", field_type=""):
        obj_base_page = BasePage(self.driver)
        self.reset_field()
        obj_base_page.wait_page_load()
        if section_type in ["shipping", "additional"]:
            obj_base_page.common_function(section_type, "button_click")
            obj_base_page.wait_page_load()
        else:
            pass

        if action_type == "edit":
            obj_base_page.common_function("edit_field", "button_click", row=row)
            obj_base_page.wait_page_load()
        else:
            obj_base_page.common_function("add_field", "button_click")
            obj_base_page.wait_page_load()
            obj_base_page.common_function("field_type", "select", value=field_type)
            obj_base_page.wait_page_load()
            obj_base_page.common_function("field_name", "clear")
            obj_base_page.wait_page_load()
            if (field_name is not None) and (field_name != ""):
                obj_base_page.common_function("field_name", "send_keys", value=field_name)
                obj_base_page.wait_page_load()
        obj_base_page.common_function("field_validation", "select", value=validation_type)
        obj_base_page.wait_page_load()
        # time.sleep(2)
        if field_name in ["shipping_address_2", "shipping_company", "billing_company", "billing_address_2"]:
            obj_base_page.common_function("required", "button_click")
            obj_base_page.wait_page_load()
        obj_base_page.common_function("save_close", "button_click")
        obj_base_page.wait_page_load()
        element = self.driver.find_elements(By.XPATH, self.saved_notification_xpath)
        obj_base_page.wait_page_load()
        if len(element) > 0:
            return True,  "Notification is found"
        else:
            return False, "Notification is not found"

    def add_field_enable(self, case_type, section_type, action_type, row="", field_type="", field_name="", field_label="", field_content=""):
        obj_base_page = BasePage(self.driver)
        obj_base_page.wait_page_load()
        self.reset_field()
        obj_base_page.wait_page_load()
        if section_type in ["shipping", "additional"]:
            obj_base_page.common_function(section_type, "button_click")
            obj_base_page.wait_page_load()
        else:
            pass
        if action_type == "edit":
            obj_base_page.common_function("edit_field", "button_click", row=row)
            obj_base_page.wait_page_load()
        else:
            obj_base_page.common_function("add_field", "button_click")
            obj_base_page.wait_page_load()
            obj_base_page.common_function("field_type", "select", value=field_type)
            obj_base_page.wait_page_load()
            obj_base_page.common_function("field_name", "clear")
            obj_base_page.wait_page_load()
            if (field_name is not None) and (field_name != ""):
                obj_base_page.common_function("field_name", "send_keys", value=field_name)
                obj_base_page.wait_page_load()
            if (field_label is not None) and (field_label != "") and (field_type == "heading"):
                obj_base_page.common_function("edit_label", "send_keys", value=field_label)
                obj_base_page.wait_page_load()
        if field_type == "paragraph":
            obj_base_page.send_keys_xpath("(//input[@name='i_label'])[1]", field_content)
        if case_type == 'disable':
            obj_base_page.common_function("disable_field", "button_click")
            obj_base_page.wait_page_load()
        # time.sleep(1)
        obj_base_page.common_function("save_close", "button_click")
        obj_base_page.wait_page_load()
        element = self.driver.find_elements(By.XPATH, self.saved_notification_xpath)
        if len(element) > 0:
            return True,  "Notification is found"
        else:
            return False,  "Notification is not found"

    def add_name(self, field_name, field_type, case_type, section_type, field_label="", field_content=""):
        obj_base_page = BasePage(self.driver)
        obj_base_page.wait_page_load()
        self.reset_field()
        obj_base_page.wait_page_load()
        if section_type in ["shipping", "additional"]:
            obj_base_page.common_function(section_type, "button_click")
            obj_base_page.wait_page_load()
        else:
            pass
        obj_base_page.common_function("add_field", "button_click")
        obj_base_page.wait_page_load()
        obj_base_page.common_function("field_type", "select", value=field_type)
        obj_base_page.wait_page_load()
        obj_base_page.common_function("field_name", "clear")
        obj_base_page.wait_page_load()
        if (field_name is not None) and (field_name != ""):
            obj_base_page.common_function("field_name", "send_keys", value=field_name)
            obj_base_page.wait_page_load()
        if (field_label is not None) and (field_label != "") and (field_type == "heading"):
            obj_base_page.common_function("edit_label", "send_keys", value=field_label)
            obj_base_page.wait_page_load()
        if field_type == "paragraph":
            obj_base_page.send_keys_xpath("(//input[@name='i_label'])[1]", field_content)
        obj_base_page.common_function("save_close", "button_click")
        obj_base_page.wait_page_load()
        if case_type == "invalid":
            element = self.driver.find_elements(By.XPATH, self.error_msg_noti_xpath)
            obj_base_page.wait_page_load()
            if len(element) > 0:
                if element[
                    0].text == 'NAME/ID must begin with a lowercase letter ([a-z]) or underscores ("_") and may be followed by any number of lowercase letters, digits ([0-9]) and underscores ("_")':
                    return True, "Notification found"
                else:
                    return False, "Notification not found"
            else:
                return False, "Element not found"
        elif case_type == "empty":
            element = self.driver.find_elements(By.XPATH, self.name_required_xpath)
            obj_base_page.wait_page_load()
            if len(element) > 0:
                return True, "Notification found"
            else:
                return False, "Notification not found"
        else:
            element = self.driver.find_elements(By.XPATH, "//td[text()='" + field_name + "']")
            obj_base_page.wait_page_load()
            notification = self.driver.find_elements(By.XPATH, self.saved_notification_xpath)
            obj_base_page.wait_page_load()
            if (len(element) > 0) and (len(notification) > 0):
                if field_name == element[0].text:
                    return True, "Element with entered name is found"
                else:
                    return False, "Element with entered name is not found"
            else:
                return False, "Element or notification not found"

    def add_display_order(self, field_type, field_name, field_label, case_type, section_type, option_value_one="",
                          option_text_one="", option_value_two="", option_text_two="", option_value_three="",
                          option_text_three="", field_default_value=""):
        obj_base_page = BasePage(self.driver)
        obj_base_page.wait_page_load()
        self.reset_field()
        obj_base_page.wait_page_load()
        if section_type in ["shipping", "additional"]:
            obj_base_page.common_function(section_type, "button_click")
            obj_base_page.wait_page_load()
        else:
            pass
        obj_base_page.common_function("add_field", "button_click")
        obj_base_page.wait_page_load()
        obj_base_page.common_function("field_type", "select", value=field_type)
        obj_base_page.wait_page_load()
        obj_base_page.common_function("field_name", "clear")
        obj_base_page.common_function("field_name", "send_keys", value=field_name)
        obj_base_page.wait_page_load()
        obj_base_page.common_function("field_label", "clear")
        obj_base_page.common_function("edit_label", "send_keys", value=field_label)
        obj_base_page.wait_page_load()
        if field_type == "hidden":
            obj_base_page.common_function("default_value", "send_keys", value=field_default_value)
            obj_base_page.wait_page_load()
        if case_type == "disable":
            obj_base_page.common_function("display_order_page", "button_click")
            obj_base_page.wait_page_load()
        if field_type in ['select', 'radio', 'multiselect', 'checkboxgroup']:
            obj_base_page.common_function("option_value_one", "send_keys",
                                          value=option_value_one)
            obj_base_page.wait_page_load()
            obj_base_page.common_function("option_text_one", "send_keys",
                                          value=option_text_one)
            obj_base_page.wait_page_load()
            obj_base_page.common_function("add_option_one", "button_click")
            obj_base_page.wait_page_load()
            obj_base_page.common_function("option_value_two", "send_keys",
                                          value=option_value_two)
            obj_base_page.wait_page_load()
            obj_base_page.common_function("option_text_two", "send_keys",
                                          value=option_text_two)
            obj_base_page.wait_page_load()
            if (option_value_three is not None) and (option_value_three != ""):
                obj_base_page.common_function("add_option_two", "button_click")
                obj_base_page.wait_page_load()
                obj_base_page.common_function("option_value_three", "send_keys",
                                              value=option_value_three)
                obj_base_page.wait_page_load()
                obj_base_page.common_function("option_text_three", "send_keys",
                                              value=option_text_three)
                obj_base_page.wait_page_load()
        obj_base_page.common_function("save_close", "button_click")
        obj_base_page.wait_page_load()
        element = self.driver.find_elements(By.XPATH, "//td[text()='" + field_name + "']")
        obj_base_page.wait_page_load()
        notification = self.driver.find_elements(By.XPATH, self.saved_notification_xpath)
        obj_base_page.wait_page_load()
        if (len(element) > 0) and (len(notification) > 0):
            return True, "Element and notification found as assumed"
        else:
            return False, "Element and notification is not found as assumed"

    def add_override(self, case_type, section_type, row, function_type, field_name, field=""):
        obj_base_page = BasePage(self.driver)
        obj_base_page.wait_page_load()
        self.reset_field()
        obj_base_page.wait_page_load()
        if section_type in ["shipping", "additional"]:
            obj_base_page.common_function(section_type, "button_click")
            obj_base_page.wait_page_load()
        else:
            pass
        obj_base_page.common_function("edit_field", "button_click", row=row)
        obj_base_page.wait_page_load()
        if function_type == "label_override":
            obj_base_page.common_function("field_label", "clear")
            obj_base_page.common_function("edit_label", "send_keys", value=field)
            obj_base_page.wait_page_load()
        elif function_type == "class_override":
            obj_base_page.common_function("field_class", "send_keys", value=field)
            obj_base_page.wait_page_load()
            # obj_base_page.add_field_class(field)
        elif function_type == "placeholder_override":
            obj_base_page.common_function("field_placeholder", "clear")
            # obj_base_page.clear_placeholder()
            obj_base_page.common_function("placeholder", "send_keys", value=field)
            obj_base_page.wait_page_load()
            # obj_base_page.add_placeholder(field)
        elif function_type == "required_override":
            obj_base_page.common_function("required", "button_click")
            obj_base_page.wait_page_load()
            # obj_base_page.disable_required()
        else:
            pass
        obj_base_page.common_function("save_close", "button_click")
        obj_base_page.wait_page_load()
        # obj_base_page.click_save_close()

        element = self.driver.find_elements(By.XPATH,
            "//table[@id='thwcfd_checkout_fields']/tbody[1]/tr[" + str(row) + "]/td[3]")
        obj_base_page.wait_page_load()
        notification = self.driver.find_elements(By.XPATH, self.saved_notification_xpath)
        obj_base_page.wait_page_load()
        if (len(element) > 0) and (len(notification) > 0) and (element[0].text == field_name):
            # obj_base_page.click_advanced_settings()
            obj_base_page.common_function("advanced_settings", "button_click")
            obj_base_page.wait_page_load()
            obj_base_page.common_function("reset_advanced_settings", "button_click")
            obj_base_page.wait_page_load()
            # obj_base_page.reset_default_advanced_settings()
            if function_type == 'label_override':
                override = self.driver.find_elements(By.XPATH, self.label_override_xpath)
            elif function_type == 'class_override':
                override = self.driver.find_elements(By.XPATH, self.class_override_xpath)
            elif function_type == 'placeholder_override':
                override = self.driver.find_elements(By.XPATH, self.placeholder_override_xpath)
            elif function_type == 'required_override':
                override = self.driver.find_elements(By.XPATH, self.required_override_xpath)
            else:
                pass
            obj_base_page.wait_page_load()
            if len(override) > 0:
                checked = override[0].is_selected()
                obj_base_page.wait_page_load()
                if case_type == 'enable':
                    if checked == True:
                        pass
                    else:
                        override[0].click()
                        obj_base_page.wait_page_load()
                else:
                    if checked == True:
                        override[0].click()
                        obj_base_page.wait_page_load()

                    else:
                        pass
                save_changes = self.driver.find_elements(By.XPATH, self.save_changes_xpath)
                if len(save_changes) > 0:
                    save_changes[0].click()
                    obj_base_page.wait_page_load()
                    notification = self.driver.find_elements(By.XPATH, self.saved_notification_xpath)
                    if len(notification) > 0:
                        return True, "Saved notification is found"
                    else:
                        return False, "Saved notification is not found"
                else:
                    return False, "Save and close, button not found"
            else:
                return False, "Element not found"
        else:
            return False, "Element not found with entered value or notification not found"

    def add_priority_override(self, section_type, case_type):
        obj_base_page = BasePage(self.driver)
        obj_base_page.wait_page_load()
        self.reset_field()
        obj_base_page.wait_page_load()
        if section_type in ["shipping", "additional"]:
            obj_base_page.common_function(section_type, "button_click")
            obj_base_page.wait_page_load()
        else:
            pass
        source1 = self.driver.find_element(By.XPATH, '//*[@id="thwcfd_checkout_fields"]/tbody/tr[5]/td[1]')
        target1 = self.driver.find_element(By.XPATH, '//*[@id="thwcfd_checkout_fields"]/tbody/tr[9]/td[1]')
        obj_base_page.wait_page_load()
        actions2 = ActionChains(self.driver)
        actions2.drag_and_drop(source1, target1).perform()
        obj_base_page.wait_page_load()
        self.driver.find_element(By.XPATH,
            "//table[@id='thwcfd_checkout_fields']//thead//tr//th//input[@name='save_fields']").click()
        obj_base_page.wait_page_load()
        # time.sleep(2)
        notification = self.driver.find_elements(By.XPATH, self.saved_notification_xpath)
        obj_base_page.wait_page_load()
        if len(notification) > 0:
            element = self.driver.find_elements(By.XPATH, '//*[@id="thwcfd_checkout_fields"]/tbody/tr[9]')
            obj_base_page.wait_page_load()
            # print(element)
            if len(element) > 0:
                class_name = element[0].find_elements(By.CLASS_NAME, 'td_name')
                obj_base_page.wait_page_load()
                # print(class_name)
                if len(class_name) > 0:
                    value = class_name[0].text
                    # print(value)
                    if value == "billing_address_1":
                        # obj_base_page.click_advanced_settings()
                        obj_base_page.common_function("advanced_settings", "button_click")
                        obj_base_page.wait_page_load()
                        override = self.driver.find_elements(By.XPATH, self.priority_override_xpath)
                        if len(override) > 0:
                            checked = override[0].is_selected()
                            if case_type == 'enable':
                                if (checked):
                                    pass
                                else:
                                    obj_base_page.wait_page_load()
                                    override[0].click()
                            else:
                                if (checked):
                                    obj_base_page.wait_page_load()
                                    override[0].click()

                                else:
                                    pass
                            save_changes = self.driver.find_elements(By.XPATH, self.save_changes_xpath)
                            if len(save_changes) > 0:
                                save_changes[0].click()
                                obj_base_page.wait_page_load()
                                notification = self.driver.find_elements(By.XPATH, self.saved_notification_xpath)
                                if len(notification) > 0:
                                    return True, "Notification Found"
                                else:
                                    return False, "Notification not found"
                            else:
                                return False, "Save changes button not found"
                        else:
                            return False, "Element not found"
                    else:
                        return False, "Value is different"
                else:
                    return False, "Element not found"
            else:
                return False, "Element not found"

        else:
            return False, "Notification not found"

    def enable_priority(self):
        obj_base_page = BasePage(self.driver)
        obj_base_page.wait_page_load()
        obj_base_page.common_function("advanced_settings", "button_click")
        obj_base_page.wait_page_load()
        # obj_base_page.click_advanced_settings()
        obj_base_page.common_function("reset_advanced_settings", "button_click")
        obj_base_page.wait_page_load()
        # obj_base_page.reset_default_advanced_settings()
        class_override = self.driver.find_elements(By.XPATH, self.class_override_xpath)
        obj_base_page.wait_page_load()
        if len(class_override) > 0:
            class_override[0].click()
            obj_base_page.wait_page_load()
            required_override = self.driver.find_elements(By.XPATH, self.required_override_xpath)
            if len(required_override) > 0:
                required_override[0].click()
                obj_base_page.wait_page_load()
                save_changes = self.driver.find_elements(By.XPATH, self.save_changes_xpath)
                if len(save_changes) > 0:
                    save_changes[0].click()
                    obj_base_page.wait_page_load()

    def add_required(self, field_name, field_label, test_case_type, section_type, action_type, field_type="", row="", option_value_one="", option_text_one="", option_value_two="",
    option_text_two="", option_value_three="", option_text_three=""):
        obj_base_page = BasePage(self.driver)
        obj_base_page.wait_page_load()
        self.reset_field()
        obj_base_page.wait_page_load()
        if section_type in ["shipping", "additional"]:
            obj_base_page.common_function(section_type, "button_click")
            obj_base_page.wait_page_load()
        else:
            pass

        if action_type == "edit":
            obj_base_page.common_function("edit_field", "button_click", row=row)
            obj_base_page.wait_page_load()
            # obj_base_page.click_edit(row)
        else:
            obj_base_page.common_function("add_field", "button_click")
            obj_base_page.wait_page_load()
            # obj_base_page.add_field()
            obj_base_page.common_function("field_type", "select", value=field_type)
            obj_base_page.wait_page_load()
            # obj_base_page.select_type(field_type)
            obj_base_page.common_function("field_name", "clear")
            # obj_base_page.clear_field_name()
            if (field_name is not None) and (field_name != ""):
                obj_base_page.common_function("field_name", "send_keys", value=field_name)
                obj_base_page.wait_page_load()

        if field_label is not None and field_label != "":
            obj_base_page.common_function("field_label", "clear")
            obj_base_page.wait_page_load()
            obj_base_page.common_function("edit_label", "send_keys", value=field_label)
            obj_base_page.wait_page_load()

        if ("disable" in test_case_type) and field_name not in ["billing_company", "shipping_company", "shipping_address_2", "billing_address_2", "order_comments"]:
            obj_base_page.common_function("required", "button_click")
            obj_base_page.wait_page_load()
        elif ("enable" in test_case_type) and field_name in ["billing_company", "shipping_company", "shipping_address_2", "billing_address_2", "order_comments"]:
            obj_base_page.common_function("required", "button_click")
            obj_base_page.wait_page_load()

        if field_type in ['select', 'radio', 'multiselect', 'checkboxgroup']:
            obj_base_page.common_function("option_value_one", "send_keys",
                                          value=option_value_one)
            obj_base_page.wait_page_load()
            obj_base_page.common_function("option_text_one", "send_keys",
                                          value=option_text_one)
            obj_base_page.wait_page_load()
            obj_base_page.common_function("add_option_one", "button_click")
            obj_base_page.wait_page_load()
            obj_base_page.common_function("option_value_two", "send_keys",
                                          value=option_value_two)
            obj_base_page.wait_page_load()
            obj_base_page.common_function("option_text_two", "send_keys",
                                          value=option_text_two)
            obj_base_page.wait_page_load()
            obj_base_page.common_function("add_option_two", "button_click")
            obj_base_page.wait_page_load()
            obj_base_page.common_function("option_value_three", "send_keys",
                                          value=option_value_three)
            obj_base_page.wait_page_load()
            obj_base_page.common_function("option_text_three", "send_keys",
                                          value=option_text_three)
            obj_base_page.wait_page_load()
        obj_base_page.common_function("save_close", "button_click")
        obj_base_page.wait_page_load()
        if action_type == 'edit':
            element = self.driver.find_elements(By.XPATH,
                                                "//table[@id='thwcfd_checkout_fields']/tbody[1]/tr[" + str(
                                                    row) + "]/td[5]")
        else:
            element = self.driver.find_elements(By.XPATH, self.check_label_xpath)
        obj_base_page.wait_page_load()

        notification = self.driver.find_elements(By.XPATH, self.saved_notification_xpath)
        if len(element) > 0 and len(notification) > 0:
            # print(element[0].text, field_label)
            if field_label.strip() == element[0].text.strip():
                return True, "Element displayed is same as entered"
            else:
                # print("2")
                return False, "Element displayed is not same as entered"
        else:
            # print("3")
            return False, "Element not found or Notification not found"
