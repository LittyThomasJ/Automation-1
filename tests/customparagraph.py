import unittest
from pages.checkoutformdesigner import CheckoutFormDesigner
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
from tests.createtestrun import CreateTestRun
from pages.loginpage import LoginWordPress
from tests.basetest import BaseTest
from pages.productpage import ProductPage
from pages.checkoutpage import CheckoutPage
from pages.thankyoupage import ThankYouPage
from pages.adminorderpage import AdminOrderPage
from section_id import section_id
from pages.myaccount import MyAccount
from dotenv import load_dotenv
from pages.basepage import BasePage
import time
from pages.testrailpage import TestRailPage
import sys
sys.path.append('/Users/zennode/PycharmProjects/WCFE-Free-new')
load_dotenv()


class CustomParagraph(unittest.TestCase, BaseTest):
    """ For testing all tests within billing custom paragraph testcases
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
        # cls.obj_base_test = BaseTest()

    def test_field_name(self, logger):
        # self.field_name('custom_paragraph_field_name', logger)
        section_data_name = self.get_section_data('custom_paragraph_field_name')
        # print(section_data_name)
        for name in section_data_name:
            field_type = name['custom_field_type']
            case_type = name['custom_custom_value_type']
            field_name = name['custom_field_name']
            case_id = name['id']
            test_case_title = name['title']
            content = "Hlooo"
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            res_checkout_form_designer, message = obj_checkout_form_designer.add_name(field_name, field_type,
                                                                                          case_type, self.section_type, field_content=content)
            if obj_checkout_form_designer:
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

    def test_field_content(self, logger):

        section_data_content = self.get_section_data('custom_paragraph_field_content')
        for content in section_data_content:
            field_type = content['custom_field_type']
            case_type = content['custom_custom_value_type']
            field_name = content['custom_field_name']
            field_label = None
            case_id = content['id']
            test_case_title = content['title']
            content = "Hlooo"
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            res_checkout_form_designer, message = obj_checkout_form_designer.add_label(field_label, case_type, self.section_type, self.action_type, field_type=field_type, field_name=field_name, field_content=content)
            if obj_checkout_form_designer:
                if case_type in ['empty', 'invalid']:
                    result, status = "Passed", 1
                else:
                    # Check for checkout page for added field
                    obj_checkout_page = CheckoutPage(self.driver)
                    self.get_url(os.environ.get('WCFEF_CHECKOUT_PAGE_URL'))
                    result_checkout, message = obj_checkout_page.check_content(field_name, case_type, self.section_type, content)
                    if (result_checkout):
                        result, status = "Passed", 1
                    else:
                        result, status = "Failed", 5
            else:
                result, status = "Failed", 5
            self.print_message(test_case_title, status,  [field_name, field_type],
                                                              message, result, logger, case_id)


    def test_field_class(self, logger):

        section_data_field_class = self.get_section_data('custom_paragraph_field_class')
        for field_class in section_data_field_class:
            field_type = self.obj_base_page.clean_data(field_class['custom_field_type'])
            field_name = self.obj_base_page.strip_data(field_class['custom_field_name'])
            field_class_value = self.obj_base_page.strip_data(field_class['custom_field_class'])
            case_id = field_class['id']
            test_case_title = field_class['title']
            content = "Hlooo"
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            res_checkout_form_designer, message = obj_checkout_form_designer.add_field_class(field_class_value, self.section_type, self.action_type, field_type=field_type, field_name=field_name, field_content=content)
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
            self.print_message(test_case_title, status,  [field_name, field_class_value], message,
                                                           result, logger, case_id)

    def test_enable_field(self, logger):

        section_data_enable_field = self.get_section_data('custom_paragraph_enable_field')
        for enable_field in section_data_enable_field:
            field_type = self.obj_base_page.clean_data(enable_field['custom_field_type'])
            field_name = self.obj_base_page.strip_data(enable_field['custom_field_name'])
            case_type = self.obj_base_page.clean_data(enable_field['custom_custom_value_type'])
            case_id = enable_field['id']
            test_case_title = enable_field['title']
            content = "Hlooo"
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            res_checkout_form_designer, message = obj_checkout_form_designer.add_field_enable(case_type, self.section_type, self.action_type, field_type=field_type, field_name=field_name, field_content=content)
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

        section_data_label = self.get_section_data('custom_paragraph_create_field')
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
            content = "Hlooo"
            case_type = 'valid'
            case_id = label['id']
            test_case_title = label['title']
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            res_checkout_form_designer, message = obj_checkout_form_designer.add_label(field_label, case_type, self.section_type, self.action_type, field_type=field_type, field_name=field_name, field_content=content)
            if (res_checkout_form_designer):
                # Check for checkout page for added field
                obj_checkout_page = CheckoutPage(self.driver)
                self.get_url(os.environ.get('WCFEF_CHECKOUT_PAGE_URL'))
                result_checkout, message = obj_checkout_page.edit_field(field_name, field_label, self.section_type, first_name, last_name, company, country, street_address, apartment, town, state, post_code, phone, email, billing_field_input=field_input, field_type=field_type)
                if (result_checkout):
                    result, status = "Passed", 1
                else:
                    result, status = "Failed", 5
            else:
                result, status = "Failed", 5
            self.print_message(test_case_title, status,  [field_input, field_label, field_name, field_type], message,
                                                           result, logger, case_id)

    @classmethod
    def tearDownClass(cls):
        print("Custom Paragragh Completed")
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
