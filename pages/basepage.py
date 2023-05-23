from selenium.webdriver.support.ui import Select
from locators.locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.save_close_button = Locators.save_close_button
        self.reset_fields = Locators.reset_fields
        self.label_xpath = Locators.edit_label_button
        self.placeholder_xpath = Locators.placeholder_xpath
        self.default_value_xpath_additional = Locators.default_value_xpath_additional
        self.default_value_xpath = Locators.default_value_xpath
        self.field_class_name = Locators.field_class_name
        self.field_validation_xpath = Locators.field_validation_xpath
        self.disable_field_xpath = Locators.disable_field_xpath
        self.shipping_fields_text = Locators.shipping_fields
        self.additional_fields_text = Locators.additional_fields_text
        self.add_field_xpath = Locators.add_field_xpath
        self.field_type_xpath = Locators.field_type_xpath
        self.field_name_xpath = Locators.field_name_xpath
        self.display_order_xpath = Locators.display_order_xpath
        self.option_value_one_xpath = Locators.option_value_one_xpath
        self.option_value_two_xpath = Locators.option_value_two_xpath
        self.option_value_three_xpath = Locators.option_value_three_xpath
        self.option_text_one_xpath = Locators.option_text_one_xpath
        self.option_text_two_xpath = Locators.option_text_two_xpath
        self.option_text_three_xpath = Locators.option_text_three_xpath
        self.add_option_two_xpath = Locators.add_option_two_xpath
        self.add_option_three_xpath = Locators.add_option_three_xpath
        self.advanced_settings_xpath = Locators.advanced_settings_xpath
        self.required_xpath = Locators.required_xpath
        self.reset_advanced_settings = Locators.reset_advanced_settings
        self.place_order_xpath = Locators.place_order

    def common_function(self, function_type, action_type, row="", value="", section_type="", field_type=""):
        if action_type == "button_click":
            if function_type == "reset":
                button_click_status = self.click_button_xpath(self.reset_fields)
                if (button_click_status):
                    try:
                        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
                        alert = self.driver.switch_to.alert
                        alert.accept()
                    except TimeoutException:
                        print("Alert does not Exist in page")
                        pass
                else:
                    print("Button not clickable")

            elif function_type == "edit_field":
                xpath = '//*[@id="thwcfd_checkout_fields"]/tbody/tr['+str(row)+']/td[10]/button'
                self.click_button_xpath(xpath)

            elif function_type == "save_close":
                self.click_button_xpath(self.save_close_button)

            elif function_type == "disable_field":
                self.click_button_xpath(self.disable_field_xpath)

            elif function_type == "shipping":
                self.click_button_link_text(self.shipping_fields_text)

            elif function_type == "additional":
                self.click_button_link_text(self.additional_fields_text)

            elif function_type == "add_field":
                self.click_button_xpath(self.add_field_xpath)

            elif function_type == "display_order_page":
                self.click_button_xpath(self.display_order_xpath)

            elif function_type == "advanced_settings":
                self.click_button_xpath(self.advanced_settings_xpath)

            elif function_type == "required":
                self.click_button_xpath(self.required_xpath)

            elif function_type == "reset_advanced_settings":
                button_click_return = self.click_button_xpath(self.reset_advanced_settings)
                if (button_click_return):
                    try:
                        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
                        alert = self.driver.switch_to.alert
                        alert.accept()
                    except TimeoutException:
                        print("Alert does not Exist in page")
                        pass
                else:
                    print("Something went wrong")

            elif function_type == "add_option_one":
                self.click_button_xpath(self.add_option_two_xpath)

            elif function_type == "add_option_two":
                self.click_button_xpath(self.add_option_three_xpath)

        elif action_type == "send_keys":
            if function_type == "edit_label":
                self.send_keys_xpath(self.label_xpath, value)

            elif function_type == "placeholder":
                self.send_keys_xpath(self.placeholder_xpath, value)

            elif function_type == "default_value":
                if (section_type == "additional") or ((field_type is not None) and (field_type == "textarea")):
                    xpath = self.default_value_xpath_additional
                else:
                    xpath = self.default_value_xpath
                self.send_keys_xpath(xpath, value)

            elif function_type == "field_class":
                self.clear_name(self.field_class_name)
                self.send_keys_name(self.field_class_name, value)

            elif function_type == "field_name":
                self.send_keys_xpath(self.field_name_xpath, value)

            elif function_type == "option_value_one":
                self.send_keys_xpath(self.option_value_one_xpath, value)

            elif function_type == "option_text_one":
                self.send_keys_xpath(self.option_text_one_xpath, value)

            elif function_type == "option_value_two":
                self.send_keys_xpath(self.option_value_two_xpath, value)

            elif function_type == "option_text_two":
                self.send_keys_xpath(self.option_text_two_xpath, value)

            elif function_type == "option_value_three":
                self.send_keys_xpath(self.option_value_three_xpath, value)

            elif function_type == "option_text_three":
                self.send_keys_xpath(self.option_text_three_xpath, value)
        elif action_type == "select":
            if function_type == "field_validation":
                self.deselect_all_xpath(self.field_validation_xpath)
                self.select_by_xpath(self.field_validation_xpath, value)
            elif function_type == "field_type":
                self.select_by_xpath(self.field_type_xpath, value)
        elif action_type == "clear":
            if function_type == "field_label":
                self.clear_xpath(self.label_xpath)
            elif function_type == "field_placeholder":
                self.clear_xpath(self.placeholder_xpath)
            elif function_type == "field_name":
                self.clear_xpath(self.field_name_xpath)
            elif function_type == "field_class":
                self.clear_name(self.field_class_name)

    def clear_xpath(self, xpath):
        element = self.driver.find_elements(By.XPATH, xpath)
        if (element):
            element[0].clear()

    def clear_name(self, name):
        element = self.driver.find_elements(By.NAME, name)
        if (element):
            element[0].clear()

    def send_keys_xpath(self, xpath, value):
        # WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))
        if (value is not None) and (value != ""):
            element = self.driver.find_elements(By.XPATH, xpath)
            if len(element) > 0:
                self.driver.execute_script("arguments[0].scrollIntoView();", element[0])
                element[0].send_keys(value)
        else:
            pass

    def send_keys_name(self, name, value):
        if (value is not None) and (value != ""):
            element = self.driver.find_elements(By.NAME, name)
            if len(element) > 0:
                self.driver.execute_script("arguments[0].scrollIntoView();", element[0])
                element[0].send_keys(value)
        else:
            pass

    def send_keys_id(self, id, value):
        if (value is not None) and (value != ""):
            element = self.driver.find_elements(By.ID, id)
            if len(element) > 0:
                self.driver.execute_script("arguments[0].scrollIntoView();", element[0])
                element[0].send_keys(value)
        else:
            pass

    def click_button_xpath(self, xpath):
        try:
            self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, xpath))))
            return True
        except:
            return False

    def click_button_id(self, id):
        try:
            self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.ID, id))))
            return True
        except:
            return False

    def click_button_name(self, name):
        try:
            self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.NAME, name))))
            return True
        except:
            return False

    def click_button_class(self, class_name):
        try:
            self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.CLASS_NAME, class_name))))
            return True
        except:
            return False

    def click_button_link_text(self, xpath):
        self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.LINK_TEXT, xpath))))
        return True

    def select_by_xpath(self, xpath, value):
        if value is not None and value != "":
            element = self.driver.find_elements(By.XPATH, xpath)
            if len(element) > 0:
                i_type = Select(element[0])
                i_type.select_by_value(value)

    def deselect_all_xpath(self, xpath):
        element = self.driver.find_elements(By.XPATH, xpath)
        if len(element) > 0:
            i_type = Select(element[0])
            i_type.deselect_all()

    def refresh_page(self):
        self.driver.refresh()

    def clean_data(self, value):
        if (value is not None) and (value != ""):
            value = value.strip()
            value = value.lower()
        else:
            pass
        return value

    def strip_data(self, value):
        if value:
            value = value.strip()
        return value

    def wait_place_order(self):
        while True:
            n=60
            wait = WebDriverWait(self.driver, n)
            try:
                wait.until(EC.element_to_be_clickable((By.XPATH, self.place_order_xpath)))
                self.driver.implicitly_wait(10)
                break
                # wait.until(lambda driver: self.driver.execute_script('return document.readyState') == 'complete')
            except Exception as e:
                n+=10

    def wait_page_load(self):
        n=60
        while True:
            wait = WebDriverWait(self.driver, n)
            try:
                wait.until(lambda driver: self.driver.execute_script('return jQuery.active') == 0)
                wait.until(lambda driver: self.driver.execute_script('return document.readyState') == 'complete')
                self.driver.implicitly_wait(10)
                break
            except Exception as e:
                n=10
                continue
