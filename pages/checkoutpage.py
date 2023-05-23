import time
from locators.locators import Locators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.basepage import BasePage


class CheckoutPage:
    """ Actions in checkout page is done here"""
    def __init__(self, driver):
        self.driver = driver
        self.place_order_xpath = Locators.place_order
        self.shipping_checkbox = Locators.shipping_checkbox
        self.label_xpath = Locators.label_xpath
        self.placeholder_default_checkbox_xpath = Locators.placeholder_default_checkbox_xpath

    def check_name(self, field_name, case_type, section_type, field_type):
        obj_base_page = BasePage(self.driver)
        if section_type == 'shipping':
            obj_base_page.wait_page_load()
            obj_base_page.click_button_id(self.shipping_checkbox)
        obj_base_page.wait_page_load()
        if field_type == "heading":
            element = self.driver.find_elements(By.XPATH, "//div[@id='"+field_name+"_field']")
        else:
            if field_type == "paragraph":
                element = self.driver.find_elements(By.ID, field_name+'_field')
            else:
                if field_type in ["multiselect", "checkboxgroup"]:
                    field_name = field_name + "[]"

                element = self.driver.find_elements(By.NAME, field_name)
        if element:
            return True, "Element with entered field name in front end is found"
        else:
            return False, "Element with entered field name in front end is not found"

    def check_label(self, field_label, field_name, case_type, section_type, action_type, field_type=""):
        obj_base_page = BasePage(self.driver)
        if section_type == 'shipping':
            obj_base_page.wait_page_load()
            obj_base_page.click_button_id(self.shipping_checkbox)
        obj_base_page.wait_page_load()
        if (action_type == 'edit') and (section_type == 'billing' or section_type == 'shipping' or section_type == 'additional'):
            element = self.driver.find_elements(By.XPATH, "//*[@id='"+field_name+"_field']/label")
        elif field_type == "checkbox":
            element = self.driver.find_elements(By.XPATH, "(//label[contains(@class,'checkbox')])[1]")
        elif field_type == "heading":
            element = self.driver.find_elements(By.XPATH, "//div[@id='"+field_name+"_field']")
        elif field_type == "hidden":
            element = self.driver.find_elements(By.NAME, field_name)
        else:
            element = self.driver.find_elements(By.XPATH, "/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/form[2]/div[1]/div[1]/div[1]/div[1]/p[12]/label[1]")

        if len(element) > 0:
            if field_type == "hidden":
                obj_base_page.wait_page_load()
                element = self.driver.find_element(By.XPATH, self.place_order_xpath)
                self.driver.execute_script("arguments[0].click();", element)
                obj_base_page.wait_page_load()
                time.sleep(1)
                return True, "Element Found"
            else:
                value = element[0].text
                if case_type == 'empty':
                    return False, "Element found for empty case"
                else:
                    if field_label in value:
                        return True, "Label found"
                    else:
                        return False, "Label not found"
        else:
            if case_type == 'empty':
                return True, "Label not found for empty case"
            else:
                return False, "Label not found"

    def check_placeholder(self, field_name, field_placeholder, case_type, section_type, field_type=""):
        obj_base_page = BasePage(self.driver)
        if section_type == 'shipping':
            obj_base_page.wait_page_load()
            obj_base_page.click_button_id(self.shipping_checkbox)
                # time.sleep(1)
        obj_base_page.wait_page_load()
        if field_type in ["multiselect", "checkboxgroup"]:
            field_name = field_name + "[]"
        element = self.driver.find_elements(By.NAME, field_name)
        if len(element) > 0:
            self.driver.execute_script("arguments[0].scrollIntoView();", element[0])
            if case_type == 'empty':
                attribute = 'data-placeholder'
                if field_name in ['billing_country', 'shipping_country', 'select_field_01']:
                    # print((field_type is not None), )
                    if (field_type is not None) and (field_type != "") and (field_type == 'select'):
                        if element[0].get_attribute(attribute) == "Choose an option":
                            return True, "Choose an option for empty case"
                        else:
                            return False, "Contents not displayed as predicted"
                    else:
                        if element[0].get_attribute(attribute) == "Select a country / region…":
                            return True, "Select a country / region… displayed as assumed"
                        else:
                            return False, "Select a country / region… not displayed as assumed"
                elif field_name in ['billing_state', 'shipping_state']:
                    if element[0].get_attribute(attribute) == "Select an option…":
                        return True, "Select an option… displayed as assumed"
                    else:
                        return False, "Select an option… not displayed as assumed"
                else:
                    attribute = 'placeholder'
                    if element[0].get_attribute(attribute) == "":
                        return True, "None"
                    else:
                        return False, "Placeholder found for empty case"
            else:
                if (field_name in ['billing_country', 'shipping_country', 'select_field_01', 'billing_state', 'shipping_state']) or (field_type in ["multiselect", "checkboxgroup"]):
                    attribute = 'data-placeholder'
                else:
                    attribute = 'placeholder'
                if field_placeholder == element[0].get_attribute(attribute):
                    return True, "Placeholder displayed as assumed"
                else:
                    return False, "Placeholder not displayed as assumed"
        else:
            return False, "Element not found"

    def check_default_value(self, field_name, field_default_value, case_type, section_type, action_type, field_type=""):
        obj_base_page = BasePage(self.driver)
        if section_type == 'shipping':
            obj_base_page.wait_page_load()
            obj_base_page.click_button_id(self.shipping_checkbox)
        obj_base_page.wait_page_load()
        if field_type in ["multiselect", "checkboxgroup"]:
            field_name = field_name + "[]"
        element = self.driver.find_elements_by_name(field_name)
        if len(element) > 0:
            self.driver.execute_script("arguments[0].scrollIntoView();", element[0])
            if case_type == "empty" or case_type == 'invalid':
                if (field_type in ["select", "radio"]) and (action_type == "create"):
                    if element[0].get_attribute('value') != "":
                        return True, "Default value not found for empty or invalid case"
                    else:
                        return False, "Default value found for empty or invalid case"
                elif field_type == "hidden" and action_type == "create":
                    checkbox = self.driver.find_elements(By.XPATH, '//*[@id="terms"]')
                    obj_base_page.wait_page_load()
                    if len(checkbox) > 0:
                        try:
                            self.driver.find_element(By.XPATH, '//*[@id="terms"]').click()
                            obj_base_page.wait_page_load()
                            self.driver.find_element(By.XPATH, self.place_order_xpath).click()
                        except:
                            self.driver.find_element(By.XPATH, '//*[@id="terms"]').click()
                            self.driver.find_element(By.XPATH, self.place_order_xpath).click()
                    else:
                        # time.sleep(2)
                        element = self.driver.find_element(By.XPATH, self.place_order_xpath)
                        self.driver.execute_script("arguments[0].click();", element)
                        time.sleep(1)
                        obj_base_page.wait_page_load()
                    return True, "Passed"
                else:
                    if element[0].get_attribute('value') == "":
                        return True, "Default value not found for empty or invalid case"
                    else:
                        return False, "Default value found for empty or invalid case"
            else:
                if field_type == "hidden" and action_type == "create":
                    checkbox = self.driver.find_elements(By.XPATH, '//*[@id="terms"]')
                    if len(checkbox) > 0:
                        try:
                            self.driver.find_element(By.XPATH, '//*[@id="terms"]').click()
                            self.driver.find_element(By.XPATH, self.place_order_xpath).click()

                        except:
                            self.driver.find_element(By.XPATH, '//*[@id="terms"]').click()
                            self.driver.find_element(By.XPATH, self.place_order_xpath).click()
                    else:
                        # time.sleep(2)
                        element = self.driver.find_element(By.XPATH, self.place_order_xpath)
                        self.driver.execute_script("arguments[0].click();", element)
                        time.sleep(1)
                        obj_base_page.wait_page_load()
                    return True, "Passed"
                else:
                    if field_default_value == element[0].get_attribute('value'):
                        return True, "Default value displayed as entered"
                    else:
                        return False, "Default value not displayed as entered"
        else:
            return False, "Element not found"

    def check_field_class(self, field_name, field_class, section_type, field_type=""):
        obj_base_page = BasePage(self.driver)
        if section_type == 'shipping':
            obj_base_page.wait_page_load()
            obj_base_page.click_button_id(self.shipping_checkbox)
                # time.sleep(1)
        obj_base_page.wait_page_load()
            # time.sleep(1)
        if field_type == "hidden":
            element_id = field_name
        else:
            element_id = field_name + '_field'
        if field_type == "heading":
            element = self.driver.find_elements(By.XPATH, "//div[@id='"+field_name+"_field']")
        else:
            element = self.driver.find_elements(By.ID, element_id)

        if len(element) > 0:
            self.driver.execute_script("arguments[0].scrollIntoView();", element[0])
            classes = element[0].get_attribute('class')
            if field_class in classes:
                return True, "Class entered in backend is found at front end"
            else:
                return False, "Class entered in backend is not found at front end"
        else:
            return False, "Element not found"

    def check_field_validation(self, field_name, field_input, case_type, validation_type, section_type, country="", state="", postcode=""):
        obj_base_page = BasePage(self.driver)
        if validation_type in ["postcode", "state"]:
            field_name_list = {"billing_first_name": "Manu", "billing_last_name": "Thomas", "billing_company": "Zennode", "billing_address_1": "panthiramkaavu", "billing_address_2": "nellikode", "billing_city": "kozhikode", "billing_phone": 9856432123, "billing_email": "manu@gmail.com"}

        else:
            field_name_list = {"billing_first_name": "Manu", "billing_last_name": "Thomas", "billing_company": "Zennode", "billing_country": "IN", "billing_address_1": "panthiramkaavu", "billing_address_2": "nellikode", "billing_city": "kozhikode", "billing_state": "KL", "billing_postcode": 673016, "billing_phone": 9856432123, "billing_email": "manu@gmail.com"}
        for name, value in field_name_list.items():
            if field_name != name:
                if name in ["billing_country", "billing_state", 'shipping_state', 'shipping_country']:
                    i_type = Select(self.driver.find_element(By.NAME, name))
                    i_type.select_by_value(value)
                    obj_base_page.wait_page_load()
                else:
                    ele = self.driver.find_element(By.NAME, name)
                    ele.clear()
                    ele.send_keys(value)
                    obj_base_page.wait_page_load()


        if section_type == 'shipping':
            obj_base_page.wait_page_load()
            obj_base_page.click_button_id(self.shipping_checkbox)
        obj_base_page.wait_page_load()
        if validation_type in ["postcode", "state"]:
            if field_name in ["shipping_state", "billing_state"]:
                state = field_input
            if section_type == "shipping":
                if country == "DE":
                    country_state_list = {"billing_country": country, "shipping_country": country}
                else:
                    country_state_list = {"billing_country": country, "billing_state": state, "shipping_country": country, "shipping_state": state}
            else:
                if country == "DE":
                    country_state_list = {"billing_country": country}
                else:
                    country_state_list = {"billing_country": country, "billing_state": state}
            for country_state, value in country_state_list.items():
                if (country in ["GB", "FJ"]) and (country_state in ["billing_state", "shipping_state"]):
                    self.driver.find_element(By.NAME, country_state).send_keys(value)
                    obj_base_page.wait_page_load()
                else:
                    i_type = Select(self.driver.find_element(By.NAME, country_state))
                    i_type.select_by_value(value)
                    obj_base_page.wait_page_load()

            pincode = self.driver.find_elements(By.NAME, "billing_postcode")
            if len(pincode) > 0:
                pincode[0].clear()
                if validation_type == "postcode":
                    pincode[0].send_keys(field_input)
                    obj_base_page.wait_page_load()
                else:
                    pincode[0].send_keys(postcode)
                    obj_base_page.wait_page_load()
            if section_type == "shipping":
                pincode = self.driver.find_elements(By.NAME, "shipping_postcode")
                if len(pincode) > 0:
                    pincode[0].clear()
                    if validation_type == "postcode":
                        pincode[0].send_keys(field_input)
                        obj_base_page.wait_page_load()
                    else:
                        pincode[0].send_keys(postcode)
                        obj_base_page.wait_page_load()


        field_name_ele = self.driver.find_elements(By.NAME, field_name)
        if len(field_name_ele) > 0:
            if (field_name in ["billing_country", "billing_state", "shipping_state", "shipping_country"]) and (country not in ["FJ", "GB"]):
                i_type = Select(field_name_ele[0])
                i_type.select_by_value(field_input)
                obj_base_page.wait_page_load()
            else:
                field_name_ele[0].clear()
                if (field_input is not None) and (field_input != ""):
                    field_name_ele[0].send_keys(field_input.strip())
                    obj_base_page.wait_page_load()
            checkbox = self.driver.find_elements(By.XPATH, '//*[@id="terms"]')
            if len(checkbox) > 0:
                try:
                    self.driver.find_element(By.XPATH, '//*[@id="terms"]').click()
                    self.driver.find_element(By.XPATH, self.place_order_xpath).click()
                except:
                    self.driver.find_element(By.XPATH, '//*[@id="terms"]').click()
                    self.driver.find_element(By.XPATH, self.place_order_xpath).click()
            else:
                # time.sleep(2)
                element = self.driver.find_element(By.XPATH, self.place_order_xpath)
                self.driver.execute_script("arguments[0].click();", element)
                obj_base_page.wait_page_load()
                time.sleep(1)

            xpath = '//ul[@class="woocommerce-error"]'
            notification = self.driver.find_elements(By.XPATH, xpath)
            if 'invalid' in case_type:
                if len(notification) > 0:
                    return True, "Notification found for invalid case"
                else:
                    return False, "Notification not found for invalid case"
            else:
                if len(notification) > 0:
                    return False, "Notification found for valid case"
                else:
                    return True, "Notification not found for valid case"

    def check_field_enable(self, field_name, case_type, section_type, field_type=""):
        obj_base_page = BasePage(self.driver)
        if section_type == 'shipping':
            obj_base_page.wait_page_load()
            obj_base_page.click_button_id(self.shipping_checkbox)
                # time.sleep(1)
        obj_base_page.wait_page_load()

            # time.sleep(1)
        if field_type in ["multiselect", "checkboxgroup"]:
            field_name = field_name + "[]"
        if field_type == "heading":
            element = self.driver.find_elements(By.XPATH, "//div[@id='"+field_name+"_field']")
        elif field_type == "paragraph":
            element = self.driver.find_elements(By.ID, field_name+"_field")
        else:
            element = self.driver.find_elements(By.NAME, field_name)
        if case_type == "enable":
            if len(element) > 0:
                return True, "Element found for enable case"
            else:
                return False, "Element not found for enable case"
        else:
            if len(element) > 0:
                return False, "Element found for disable case"
            else:
                return True, "Element not found for disable case"

    def clear_auto_saved(self, field_name, section_type):
        obj_base_page = BasePage(self.driver)
        if section_type == 'shipping':
            obj_base_page.wait_page_load()
            obj_base_page.click_button_id(self.shipping_checkbox)
        obj_base_page.wait_page_load()
        if field_name in ['billing_country', 'shipping_country']:
            select = Select(self.driver.find_element(By.NAME, field_name))
            obj_base_page.wait_page_load()
            selected_option = select.first_selected_option
            self.driver.execute_script("arguments[0].removeAttribute('selected')", selected_option)
            obj_base_page.wait_page_load()
            element = self.driver.find_element(By.XPATH, self.place_order_xpath)
            self.driver.execute_script("arguments[0].click();", element)
            obj_base_page.wait_page_load()
            time.sleep(1)
        else:
            field_name_ele = self.driver.find_elements(By.NAME, field_name)
            if len(field_name_ele) > 0:

                field_name_ele[0].clear()
                obj_base_page.wait_page_load()
                if field_name not in ['order_comments']:
                    element = self.driver.find_element(By.XPATH, self.place_order_xpath)
                    self.driver.execute_script("arguments[0].click();", element)
                    obj_base_page.wait_page_load()
                    time.sleep(1)

    def edit_field(self, field_name, field_label, section_type, first_name, last_name, company, country, street_address, apartment, town, state, post_code, phone, email, order_comments="", billing_field_input="", field_type=""):
        obj_base_page = BasePage(self.driver)
        if section_type == 'shipping':
            obj_base_page.wait_page_load()
            obj_base_page.click_button_id(self.shipping_checkbox)
        obj_base_page.wait_page_load()
        if field_type == "paragraph":
            element = self.driver.find_elements(By.ID, field_name+"_field")
        else:
            if field_type in ["multiselect", "checkboxgroup"]:
                field_name = field_name + "[]"
            element = self.driver.find_elements(By.NAME, field_name)
        if len(element) > 0:
            self.driver.find_element(By.NAME, 'billing_first_name').clear()
            self.driver.find_element(By.NAME, 'billing_first_name').send_keys(first_name)
            obj_base_page.wait_page_load()
            self.driver.find_element(By.NAME, 'billing_last_name').clear()
            self.driver.find_element(By.NAME, 'billing_last_name').send_keys(last_name)
            obj_base_page.wait_page_load()
            self.driver.find_element(By.NAME, 'billing_company').clear()
            self.driver.find_element(By.NAME, 'billing_company').send_keys(company)
            obj_base_page.wait_page_load()
            select_country = Select(self.driver.find_element(By.NAME, 'billing_country'))
            select_country.select_by_value(country)
            obj_base_page.wait_page_load()
            self.driver.find_element(By.NAME, 'billing_address_1').clear()
            self.driver.find_element(By.NAME, 'billing_address_1').send_keys(street_address)
            obj_base_page.wait_page_load()
            self.driver.find_element(By.NAME, 'billing_address_2').clear()
            self.driver.find_element(By.NAME, 'billing_address_2').send_keys(apartment)
            obj_base_page.wait_page_load()
            self.driver.find_element(By.NAME, 'billing_city').clear()
            self.driver.find_element(By.NAME, 'billing_city').send_keys(town)
            obj_base_page.wait_page_load()
            select_state = Select(self.driver.find_element_by_name('billing_state'))
            select_state.select_by_value(state)
            obj_base_page.wait_page_load()
            self.driver.find_element(By.NAME, 'billing_postcode').clear()
            self.driver.find_element(By.NAME, 'billing_postcode').send_keys(post_code)
            obj_base_page.wait_page_load()
            self.driver.find_element(By.NAME, 'billing_phone').clear()
            self.driver.find_element(By.NAME, 'billing_phone').send_keys(phone)
            obj_base_page.wait_page_load()
            self.driver.find_element(By.NAME, 'billing_email').clear()
            self.driver.find_element(By.NAME, 'billing_email').send_keys(email)
            obj_base_page.wait_page_load()
            if billing_field_input is not None and billing_field_input != '':
                if field_type in ['select', 'multiselect']:
                    sel_type = Select(self.driver.find_element(By.NAME, field_name))
                    sel_type.select_by_value(billing_field_input)
                    obj_base_page.wait_page_load()
                elif field_type in ["radio", "checkbox"]:
                    self.driver.find_element(By.NAME, field_name).click()
                    obj_base_page.wait_page_load()
                elif field_type in ["checkboxgroup"]:
                    self.driver.find_element(By.XPATH, "(//input[@value='"+billing_field_input+"'])[1]").click()
                    obj_base_page.wait_page_load()
                elif field_type in ["hidden", "paragraph"]:
                    pass
                elif field_type in ["datetime_local", "date", "month", "time", "week"]:
                    element = self.driver.find_elements(By.NAME, field_name)
                    self.driver.execute_script(f"arguments[0].setAttribute('value', '"+billing_field_input+"')", element[0])
                    # element[0].send_keys(Keys.RETURN)
                else:
                    self.driver.find_element(By.NAME, field_name).send_keys(billing_field_input)
                    obj_base_page.wait_page_load()
            if (order_comments is not None) and (order_comments != ''):
                self.driver.find_element(By.NAME, 'order_comments').send_keys(order_comments)
                obj_base_page.wait_page_load()

            if section_type == 'shipping':
                self.driver.find_element(By.NAME, 'shipping_first_name').clear()
                self.driver.find_element(By.NAME, 'shipping_first_name').send_keys(first_name)
                obj_base_page.wait_page_load()
                self.driver.find_element(By.NAME, 'shipping_last_name').clear()
                self.driver.find_element(By.NAME, 'shipping_last_name').send_keys(last_name)
                obj_base_page.wait_page_load()
                self.driver.find_element(By.NAME, 'shipping_company').clear()
                self.driver.find_element(By.NAME, 'shipping_company').send_keys(company)
                obj_base_page.wait_page_load()
                select_country_ship = Select(self.driver.find_element(By.NAME, 'shipping_country'))
                select_country_ship.select_by_value(country)
                obj_base_page.wait_page_load()
                self.driver.find_element(By.NAME, 'shipping_address_1').clear()
                self.driver.find_element(By.NAME, 'shipping_address_1').send_keys(street_address)
                obj_base_page.wait_page_load()
                self.driver.find_element(By.NAME, 'shipping_address_2').clear()
                self.driver.find_element(By.NAME, 'shipping_address_2').send_keys(apartment)
                obj_base_page.wait_page_load()
                self.driver.find_element(By.NAME, 'shipping_city').clear()
                self.driver.find_element(By.NAME, 'shipping_city').send_keys(town)
                obj_base_page.wait_page_load()
                select_state_ship = Select(self.driver.find_element(By.NAME, 'shipping_state'))
                select_state_ship.select_by_value(state)
                obj_base_page.wait_page_load()
                self.driver.find_element(By.NAME, 'shipping_postcode').clear()
                self.driver.find_element(By.NAME, 'shipping_postcode').send_keys(post_code)
                obj_base_page.wait_page_load()

            element = self.driver.find_element(By.XPATH, self.place_order_xpath)
            self.driver.execute_script("arguments[0].click();", element)
            obj_base_page.wait_page_load()
            time.sleep(1)
            return True, "Element found as assumed"
        else:
            return True, "Element not found"

    def place_order(self, field_name, section_type, field_type, field_input=""):
        obj_base_page = BasePage(self.driver)
        if section_type == 'shipping':
            obj_base_page.wait_page_load()
            obj_base_page.click_button_id(self.shipping_checkbox)
        obj_base_page.wait_page_load()
        if field_type in ["multiselect", "checkboxgroup"]:
            field_name = field_name + "[]"
        element = self.driver.find_elements(By.NAME, field_name)
        if len(element) > 0:
            if field_type in ["select", "multiselect"]:
                sel_type = Select(element[0])
                sel_type.select_by_value(field_input)
            elif field_type in ["radio", "checkboxgroup"]:
                self.driver.find_element(By.NAME, field_name).click()
                obj_base_page.wait_page_load()
            elif field_type == "hidden":
                pass
            elif field_type in ["datetime_local", "date", "month", "time", "week"]:
                self.driver.execute_script(f"arguments[0].setAttribute('value', '"+field_input+"')", element[0])
            else:
                element[0].send_keys(field_input)
            element = self.driver.find_element(By.XPATH, self.place_order_xpath)
            self.driver.execute_script("arguments[0].click();", element)
            obj_base_page.wait_page_load()
            time.sleep(1)
            return True, "Element found as assumed"
        else:
            return False, "Element not found"

    def check_label_override(self, field_label, field_name, case_type, section_type):
        obj_base_page = BasePage(self.driver)
        if section_type == 'shipping':
            obj_base_page.wait_page_load()
            obj_base_page.click_button_id(self.shipping_checkbox)
        obj_base_page.wait_page_load()
        element = self.driver.find_elements(By.XPATH, "//*[@id='"+field_name+"_field']/label")
        if len(element) > 0:
            self.driver.execute_script("arguments[0].scrollIntoView();", element[0])
            value = element[0].text
            if case_type == "enable":
                if field_label in value:
                    return True, "Label same as entered for enable case"
                else:
                    return False, "Label not same as entered for enable case"
            else:
                if field_label in value:
                    return False, "Label same as entered for disable case"
                else:
                    return True, "Label not same as entered for disable case"
        else:
            return False, "Element not found"

    def check_class_override(self, field_name, field_class, section_type, case_type):
        obj_base_page = BasePage(self.driver)
        if section_type == 'shipping':
            obj_base_page.wait_page_load()
            obj_base_page.click_button_id(self.shipping_checkbox)
        obj_base_page.wait_page_load()
        element_id = field_name + '_field'
        element = self.driver.find_elements(By.ID, element_id)
        if len(element) > 0:
            self.driver.execute_script("arguments[0].scrollIntoView();", element[0])
            classes = element[0].get_attribute('class')
            if case_type == 'enable':
                if field_class in classes:
                    return True, "Class found for enable case"
                else:
                    return False, "Class not found for enable case"
            else:
                if field_class in classes:
                    return False, "Class found for disable case"
                else:
                    return True, "Class not found for disable case"
        else:
            return False, "Element not found"

    def check_placeholder_override(self, field_name, field_placeholder, section_type, case_type):
        obj_base_page = BasePage(self.driver)
        if section_type == 'shipping':
            obj_base_page.wait_page_load()
            obj_base_page.click_button_id(self.shipping_checkbox)
        obj_base_page.wait_page_load()

        element = self.driver.find_elements(By.NAME, field_name)
        if len(element) > 0:
            self.driver.execute_script("arguments[0].scrollIntoView();", element[0])
            classes = element[0].get_attribute('class')
            if case_type == 'enable':
                if field_placeholder == element[0].get_attribute('placeholder'):
                    return True, "Placeholder same as entered for enabled case"
                else:
                    return False, "Placeholder not same as entered for enabled case"
            else:
                if field_placeholder == element[0].get_attribute('placeholder'):
                    return False, "Placeholder same as entered for disabled case"
                else:
                    return True, "Placeholder not same as entered for disabled case"
        else:
            return False, "Element not found"

    def check_required_override(self, field_name, section_type, case_type):
        obj_base_page = BasePage(self.driver)
        if section_type == 'shipping':
            obj_base_page.wait_page_load()
            obj_base_page.click_button_id(self.shipping_checkbox)
        obj_base_page.wait_page_load()
        element = self.driver.find_elements(By.XPATH, "//*[@id='"+field_name+"_field']/label")
        value = element[0].text
        if case_type == "enable":
            if "*" in value:
                return False, "* found on element's label for enabled case"
            else:
                return True, "* not found on element's label for enabled case"
        else:
            if "*" in value:
                return True, "* found on element's label for disabled case"
            else:
                return False, "* not found on element's label for disabled case"

    def check_priority_override(self, section_type):
        obj_base_page = BasePage(self.driver)
        if section_type == 'shipping':
            obj_base_page.wait_page_load()
            obj_base_page.click_button_id(self.shipping_checkbox)
        obj_base_page.wait_page_load()
        element = self.driver.find_elements(By.XPATH, '//*[@id="billing_address_1_field"]')
        if len(element) > 0:
            priority = element[0].get_attribute('data-priority')
            if priority == '90':
                return True, "Passed"
            else:
                return False, "Failed"
        else:
            return False, "Element not found"

    def check_required(self, field_name, section_type, test_case_type, action_type, field_type="", field_input=""):
        obj_base_page = BasePage(self.driver)
        if section_type == 'shipping':
            obj_base_page.wait_page_load()
            obj_base_page.click_button_id(self.shipping_checkbox)
            field_name_list = {"billing_first_name": "Manu", "billing_last_name": "Thomas", "billing_company": "Zennode", "billing_country": "IN", "billing_address_1": "panthiramkaavu", "billing_address_2": "nellikode", "billing_city": "kozhikode", "billing_state": "KL", "billing_postcode": 673016, "billing_phone": 9856432123, "billing_email": "manu@gmail.com", "shipping_first_name": "Manu", "shipping_last_name": "Thomas", "shipping_company": "Zennode", "shipping_country": "IN", "shipping_address_1": "panthiramkaavu", "shipping_address_2": "nellikode", "shipping_city": "kozhikode", "shipping_state": "KL", "shipping_postcode": 673016}
        else:
            field_name_list = {"billing_first_name": "Manu", "billing_last_name": "Thomas", "billing_company": "Zennode", "billing_country": "IN", "billing_address_1": "panthiramkaavu", "billing_address_2": "nellikode", "billing_city": "kozhikode", "billing_state": "KL", "billing_postcode": 673016, "billing_phone": 9856432123, "billing_email": "manu@gmail.com"}
        obj_base_page.wait_page_load()
        for name, value in field_name_list.items():
            if field_name != name:
                if name in ["billing_country", "billing_state", "shipping_country", "shipping_state"]:
                    i_type = Select(self.driver.find_element(By.NAME, name))
                    i_type.select_by_value(value)
                    obj_base_page.wait_page_load()
                else:
                    # print("send")
                    ele = self.driver.find_element(By.NAME, name)
                    ele.clear()
                    ele.send_keys(value)
                    obj_base_page.wait_page_load()
        if field_type in ["multiselect", "checkboxgroup"]:
            field_name = field_name + "[]"
        element_one = self.driver.find_elements(By.NAME, field_name.strip())
        if len(element_one):
            if (field_name in ['billing_country', 'shipping_country', 'billing_state', 'shipping_state']) or (field_type in ['select', 'multiselect']):
                sel_type = Select(element_one[0])
                if "without" not in test_case_type:
                    sel_type.select_by_value(field_input)
                    obj_base_page.wait_page_load()
            elif field_type in ['radio']:
                if "without" not in test_case_type:
                    self.driver.find_element(By.XPATH, '//*[@id="'+field_name.strip()+'_'+field_input.strip()+'"]').click()
                    obj_base_page.wait_page_load()
                # element_one[0].click()
            elif field_type in ["checkboxgroup"]:
                if "without" not in test_case_type:
                    self.driver.find_element(By.XPATH, "(//input[@value='"+field_input+"'])[1]").click()
                    obj_base_page.wait_page_load()

            elif field_type in ['checkbox']:
                if "without" not in test_case_type:
                    self.driver.find_element(By.NAME, field_name).click()
                    obj_base_page.wait_page_load()
            elif field_type in ["datetime_local", "date", "month", "time", "week"]:
                # print("hii")
                # wait = WebDriverWait(self.driver, 30)
                # date= wait.until(EC.element_to_be_clickable((By.NAME, field_name)))
                if "without" not in test_case_type:
                    self.driver.execute_script(f"arguments[0].setAttribute('value', '"+field_input+"')", element_one[0])
            else:
                element_one[0].clear()
                if "without" not in test_case_type:
                    element_one[0].send_keys(field_input)
                    obj_base_page.wait_page_load()
        else:
            # print("4")
            return False

        if (action_type == 'edit') and (section_type == 'billing' or section_type == 'shipping' or section_type == 'additional'):
            element_two = self.driver.find_elements(By.XPATH, "//*[@id='"+field_name+"_field']/label")
        elif field_type == "checkbox":
            element_two = self.driver.find_elements(By.XPATH, "(//label[contains(@class,'checkbox')])[1]")
        else:
            element_two = self.driver.find_elements(By.XPATH, "/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/form[2]/div[1]/div[1]/div[1]/div[1]/p[12]/label[1]")
        value = element_two[0].text
        # print(value)
        element = self.driver.find_element(By.XPATH, self.place_order_xpath)
        self.driver.execute_script("arguments[0].click();", element)
        obj_base_page.wait_page_load()
        time.sleep(2)
        xpath = 'woocommerce-error'
        notification = self.driver.find_elements(By.CLASS_NAME, xpath)
        # print(notification)
        if "enable" in test_case_type.lower():
            # print("enable")
            if ("without" in test_case_type):
                if ("*" in value) and (len(notification) > 0):
                    return True, "* in element's label or notification found for without enable case"
                else:
                    return False, "* in element's label or notification not found for without enable case"
            else:
                if ("*" in value) and (len(notification) == 0):
                    return True, "* in element's label or notification found for enable case"
                else:
                    return False, "* in element's label and notification not found for enable case"
        else:
            if ("*" in value) and (len(notification)>0):
                return False, "* in element's label or notification found for disable case"
            else:
                return True, "* in element's label or notification not found for disable case"
    def check_content(self, field_name, case_type, section_type, content):
        element = self.driver.find_elements(By.ID, field_name+'_field')
        if len(element) > 0:
            if case_type == "valid":
                if element[0].text == content:
                    return True, "Content is correctly displayed on frontend"
                else:
                    return False, "Content is not correctly displayed on frontend"
            else:
                return False, "Content is displayed on frontend"
        else:
            if case_type == "valid":
                return False, "Content is not displayed on frontend"
            else:
                return True, "Content is not displayed on frontend"
