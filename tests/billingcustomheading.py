import unittest
from pages.checkoutformdesigner import CheckoutFormDesigner
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
from tests.createtestrun import CreateTestRun
from pages.loginpage import LoginWordPress
from pages.checkoutpage import CheckoutPage
from tests.basetest import BaseTest
from pages.basepage import BasePage
from section_id import section_id
from dotenv import load_dotenv
from pages.testrailpage import TestRailPage
import sys
sys.path.append('/Users/zennode/PycharmProjects/WCFE-Free-new')
load_dotenv()


class BillingCustomHeading(unittest.TestCase, BaseTest):
    """ For testing all tests within billing custom heading testcases
    Calls to all the actions in each pages are done here
    """
    def __init__(self):
        self.section_type = "billing"
        self.action_type = "create"

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

    def test_field_name(self, logger):
        # self.field_name('billing_custom_heading_field_name', logger)
        section_data_name = self.get_section_data('billing_custom_heading_field_name')
        for name in section_data_name:
            field_type = self.obj_base_page.clean_data(name['custom_field_type'])
            case_type = self.obj_base_page.strip_data(name['custom_custom_value_type'])
            field_name = self.obj_base_page.strip_data(name['custom_field_name'])
            field_label = self.obj_base_page.strip_data(name['custom_field_label'])
            case_id = name['id']
            test_case_title = name['title']
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            res_checkout_form_designer, message = obj_checkout_form_designer.add_name(field_name, field_type, case_type, self.section_type, field_label=field_label)
            if (res_checkout_form_designer):
                if case_type in ['empty', 'invalid']:
                    result, status = "Passed", 1
                else:
                    # Check for checkout page for added field
                    obj_checkout_page = CheckoutPage(self.driver)
                    self.get_url(os.environ.get('WCFEF_CHECKOUT_PAGE_URL'))
                    result_checkout, message = obj_checkout_page.check_name(field_name, case_type,
                                                                    self.section_type, field_type)
                    if (result_checkout):
                        result, status = "Passed", 1
                    else:
                        result, status = "Failed", 5
            else:
                result, status = "Failed", 5
            self.print_message(test_case_title, status,  [field_name, field_type],
                                                                    message, result, logger, case_id)

    # For testing
    def test_field_label(self, logger):
        self.field_label('billing_custom_heading_field_label', logger, section_type=self.section_type, action_type=self.action_type)

        # section_data_label = self.get_section_data('billing_custom_heading_field_label')
        # for label in section_data_label:
        #     field_type = self.obj_base_page.clean_data(label['custom_field_type'])
        #     field_label = self.obj_base_page.strip_data(label['custom_field_label'])
        #     case_type = self.obj_base_page.clean_data(label['custom_custom_value_type'])
        #     field_name = self.obj_base_page.strip_data(label['custom_field_name'])
        #     case_id = label['id']
        #     test_case_title = label['title']
        #     obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
        #     self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
        #     res_checkout_form_designer, message = obj_checkout_form_designer.add_label(field_label, case_type, self.section_type, self.action_type, field_type=field_type, field_name=field_name)
        #     if (res_checkout_form_designer):
        #         if case_type == "without fieldname":
        #             result, status = "Passed", 1
        #         else:
        #             # Check for checkout page for added field
        #             obj_checkout_page = CheckoutPage(self.driver)
        #             self.get_url(os.environ.get('WCFEF_CHECKOUT_PAGE_URL'))
        #             result_checkout, message = obj_checkout_page.check_label(field_label, field_name, case_type, self.section_type, self.action_type, field_type=field_type)
        #             if (result_checkout):
        #                 result, status = "Passed", 1
        #             else:
        #                 result, status = "Failed", 5
        #     else:
        #         result, status = "Failed", 5
        #     self.print_message(test_case_title, status,  [field_name, field_type],
        #                                                             message, result, logger, case_id)

    def test_field_class(self, logger):

        section_data_field_class = self.get_section_data('billing_custom_heading_field_class')
        for field_class in section_data_field_class:
            field_type = self.obj_base_page.clean_data(field_class['custom_field_type'])
            field_name = self.obj_base_page.strip_data(field_class['custom_field_name'])
            field_class_value = self.obj_base_page.strip_data(field_class['custom_field_class'])
            field_label = self.obj_base_page.strip_data(field_class['custom_field_label'])
            case_id = field_class['id']
            test_case_title = field_class['title']
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            res_checkout_form_designer, message = obj_checkout_form_designer.add_field_class(field_class_value, self.section_type, self.action_type, field_type=field_type, field_name=field_name, field_label=field_label)

            if (res_checkout_form_designer):
                # Check for checkout page for added field
                obj_checkout_page = CheckoutPage(self.driver)
                self.get_url(os.environ.get('WCFEF_CHECKOUT_PAGE_URL'))
                result_checkout, message = obj_checkout_page.check_field_class(field_name, field_type, field_class_value, self.section_type)

                if (result_checkout):
                    result, status = "Passed", 1
                else:
                    result, status = "Failed", 5
            else:
                result, status = "Failed", 5
            self.print_message(test_case_title, status,  [field_name, field_class_value],
                                                                    message,
                                                                    result, logger, case_id)

    def test_enable_field(self, logger):

        section_data_enable_field = self.get_section_data('billing_custom_heading_enable_field')
        for enable_field in section_data_enable_field:
            field_type = self.obj_base_page.clean_data(enable_field['custom_field_type'])
            field_name = self.obj_base_page.strip_data(enable_field['custom_field_name'])
            case_type = self.obj_base_page.clean_data(enable_field['custom_custom_value_type'])
            field_label = self.obj_base_page.strip_data(enable_field['custom_field_label'])
            case_id = enable_field['id']
            test_case_title = enable_field['title']
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            res_checkout_form_designer, message = obj_checkout_form_designer.add_field_enable(case_type, self.section_type, self.action_type, field_type=field_type, field_name=field_name, field_label=field_label)

            if (res_checkout_form_designer):
                # Check for checkout page for added field
                obj_checkout_page = CheckoutPage(self.driver)
                self.get_url(os.environ.get('WCFEF_CHECKOUT_PAGE_URL'))
                result_checkout, message = obj_checkout_page.check_field_enable(field_name, case_type, self.section_type, field_type=field_type)
                if (result_checkout):
                    result, status = "Passed", 1
                else:
                    result, status = "Failed", 5
            else:
                result, status = "Failed", 5
            self.print_message(test_case_title, status,  [field_name, field_type],
                                                                    message,
                                                                    result, logger, case_id)

    def test_create_field(self, logger):

        section_data_label = self.get_section_data('billing_custom_heading_create_field')
        for label in section_data_label:
            street_address = "chakkaalakkal"
            first_name = "phhhh"
            last_name = "jkkkjj"
            state = "KL"
            country = "IN"
            apartment = "kkk"
            town = "manjeri"
            company = "zenn"
            phone = "9846789876"
            email = "litty4ever@gmail.com"
            post_code = "670987"
            field_type = self.obj_base_page.clean_data(label['custom_field_type'])
            field_name = self.obj_base_page.strip_data(label['custom_field_name'])
            field_label = self.obj_base_page.strip_data(label['custom_field_label'])
            field_input = self.obj_base_page.strip_data(label['custom_field_input_value'])
            case_type = 'valid'
            case_id = label['id']
            test_case_title = label['title']
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            res_checkout_form_designer, message = obj_checkout_form_designer.add_label(field_label, case_type, self.section_type, self.action_type, field_type=field_type, field_name=field_name)
            if (res_checkout_form_designer):
                # Check for checkout page for added field
                obj_checkout_page = CheckoutPage(self.driver)
                self.get_url(os.environ.get('WCFEF_CHECKOUT_PAGE_URL'))
                result_checkout, message = obj_checkout_page.edit_field(field_name, field_label, self.section_type, first_name, last_name, company, country, street_address, apartment, town, state, post_code, phone, email, billing_field_input=field_input)
                if (result_checkout):
                    result, status = "Passed", 1
                else:
                    result, status = "Failed", 5
            else:
                result, status = "Failed", 5
            self.print_message(test_case_title, status,  [field_name, field_type, field_label, field_input],
                                                                    message,
                                                                    result, logger, case_id)

    @classmethod
    def tearDownClass(cls):
        print("Custom Heading Completed")
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
