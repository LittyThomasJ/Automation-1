import unittest
from pages.checkoutformdesigner import CheckoutFormDesigner
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
from tests.createtestrun import CreateTestRun
from pages.loginpage import LoginWordPress
from tests.basetest import BaseTest
from pages.checkoutpage import CheckoutPage
from section_id import section_id
from dotenv import load_dotenv
from pages.testrailpage import TestRailPage
from pages.basepage import BasePage
import sys
sys.path.append('/Users/zennode/PycharmProjects/WCFE-Free-new')
load_dotenv()


class AdvancedBillingOverride(unittest.TestCase, BaseTest):
    """ For testing all tests within advanced billing override testcases
    Calls to all the actions in each pages are done here
    """
    def __init__(self):
        self.row = 5
        self.section_type = 'billing'
        self.field_name = 'billing_address_1'

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument('--headless')
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        # cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.set_page_load_timeout(100)
        cls.driver.maximize_window()
        cls.driver.get(os.environ.get('WCFEF_LOGIN_URL'))
        username = os.environ.get('WCFEF_USERNAME')
        password = os.environ.get('WCFEF_PASSWORD')
        login = LoginWordPress(cls.driver)
        login.login_wordpress_dashboard(username, password)
        cls.obj_base_page = BasePage(cls.driver)

    def test_label_override(self, logger):
        section_data_label = self.get_section_data('billing_override_label_override')
        for label in section_data_label:
            field_label = self.obj_base_page.strip_data(label['custom_field_label'])
            case_type = self.obj_base_page.clean_data(label['custom_custom_value_type'])
            case_id = label['id']
            test_case_title = label['title']
            # Set fields in backend
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            res_checkout_form_designer, message = obj_checkout_form_designer.add_override(case_type, self.section_type, self.row, 'label_override', self.field_name, field_label)
            if (res_checkout_form_designer):
                # Check for checkout page for added field
                obj_checkout_page = CheckoutPage(self.driver)
                self.get_url(os.environ.get('WCFEF_CHECKOUT_PAGE_URL'))
                result_checkout, message = obj_checkout_page.check_label_override(field_label, self.field_name, case_type, self.section_type)
                if (result_checkout):
                    result, status = "Passed", 1
                else:
                    result, status = "Failed", 5
            else:
                result, status = "Failed", 5
            self.print_message(test_case_title, status,  [field_label], message, result, logger, case_id)

    def test_class_override(self, logger):
        section_data_class = self.get_section_data('billing_override_class_override')
        for class_override in section_data_class:
            field_class = self.obj_base_page.strip_data(class_override['custom_field_class'])
            case_type = self.obj_base_page.clean_data(class_override['custom_custom_value_type'])
            case_id = class_override['id']
            test_case_title = class_override['title']
            # Set fields in backend
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            res_checkout_form_designer, message = obj_checkout_form_designer.add_override(case_type, self.section_type, self.row, 'class_override', self.field_name, field_class)
            if (res_checkout_form_designer):
                # Check for checkout page for added field
                obj_checkout_page = CheckoutPage(self.driver)
                self.get_url(os.environ.get('WCFEF_CHECKOUT_PAGE_URL'))
                result_checkout, message = obj_checkout_page.check_class_override(self.field_name, field_class, self.section_type, case_type)
                if (result_checkout):
                    result, status = "Passed", 1
                else:
                    result, status = "Failed", 5
            else:
                result, status = "Failed", 5
            self.print_message(test_case_title, status,  [field_class], message, result, logger, case_id)

    def test_placeholder_override(self, logger):
        section_data_placeholder_override = self.get_section_data('billing_override_placeholder_override')
        for placeholder_override in section_data_placeholder_override:
            field_placeholder = self.obj_base_page.strip_data(placeholder_override['custom_field_place_holder'])
            case_type = self.obj_base_page.clean_data(placeholder_override['custom_custom_value_type'])
            case_id = placeholder_override['id']
            test_case_title = placeholder_override['title']
            # Set fields in backend
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            res_checkout_form_designer, message = obj_checkout_form_designer.add_override(case_type, self.section_type, self.row, 'placeholder_override', self.field_name, field_placeholder)
            if (res_checkout_form_designer):
                # Check for checkout page for added field
                obj_checkout_page = CheckoutPage(self.driver)
                self.get_url(os.environ.get('WCFEF_CHECKOUT_PAGE_URL'))
                result_checkout, message = obj_checkout_page.check_placeholder_override(self.field_name, field_placeholder, self.section_type, case_type)
                if (result_checkout):
                    result, status = "Passed", 1
                else:
                    result, status = "Failed", 5
            else:
                result, status = "Failed", 5
            self.print_message(test_case_title, status,  [field_placeholder], message, result, logger, case_id)

    def test_required_override(self, logger):
        section_data_required_override = self.get_section_data('billing_override_required_override')
        for required_override in section_data_required_override:
            case_type = self.obj_base_page.clean_data(required_override['custom_custom_value_type'])
            case_id = required_override['id']
            test_case_title = required_override['title']
            # Set fields in backend
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            res_checkout_form_designer, message = obj_checkout_form_designer.add_override(case_type, self.section_type, self.row, 'required_override', self.field_name)
            if (res_checkout_form_designer):
                # Check for checkout page for added field
                obj_checkout_page = CheckoutPage(self.driver)
                self.get_url(os.environ.get('WCFEF_CHECKOUT_PAGE_URL'))
                result_checkout, message = obj_checkout_page.check_required_override(self.field_name, self.section_type, case_type)
                if (result_checkout):
                    result, status = "Passed", 1
                else:
                    result, status = "Failed", 5
            else:
                result, status = "Failed", 5
            self.print_message(test_case_title, status,  [case_type], message, result, logger, case_id)

    def test_priority_override(self, logger):
        section_data_priority_override = self.get_section_data('billing_override_required_override')
        for priority_override in section_data_priority_override:
            case_type = self.obj_base_page.clean_data(priority_override['custom_custom_value_type'])
            case_id = priority_override['id']
            test_case_title = priority_override['title']
            # Set fields in backend
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            res_checkout_form_designer, message = obj_checkout_form_designer.add_priority_override(self.section_type, case_type)
            if (res_checkout_form_designer):
                # Check for checkout page for added field
                obj_checkout_page = CheckoutPage(self.driver)
                self.get_url(os.environ.get('WCFEF_CHECKOUT_PAGE_URL'))
                result_checkout, message = obj_checkout_page.check_priority_override(self.section_type)
                if (result_checkout):
                    result, status = "Passed", 1
                else:
                    result, status = "Failed", 5
            else:
                result, status = "Failed", 5
            self.print_message(test_case_title, status,  [case_type], message, result, logger, case_id)

    @classmethod
    def tearDownClass(cls):
        print("Advanced Billing Override Completed")
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
