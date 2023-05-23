import unittest
from pages.checkoutformdesigner import CheckoutFormDesigner
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
from tests.createtestrun import CreateTestRun
from pages.loginpage import LoginWordPress
from pages.myaccount import MyAccount
from pages.productpage import ProductPage
from pages.checkoutpage import CheckoutPage
from pages.thankyoupage import ThankYouPage
from tests.basetest import BaseTest
from pages.basepage import BasePage
from pages.adminorderpage import AdminOrderPage
from pages.cartpage import CartPage
from section_id import section_id
from dotenv import load_dotenv
import time
import sys
from pages.testrailpage import TestRailPage
sys.path.append('/Users/zennode/PycharmProjects/WCFE-Free-new')
load_dotenv()

class BillingCustomCheckboxGroup(unittest.TestCase, BaseTest):
    """ For testing all tests within billing custom checkboxgroup testcases
    Calls to all the actions in each pages are done here
    """
    def __init__(self):
        # self.__init__()
        # self.run_id = CreateTestRun.run_id
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
        self.field_name('billing_custom_checkboxgroup_field_name', logger)
        # section_data_name = self.get_section_data('billing_custom_checkboxgroup_field_name')
        # for name in section_data_name:
        #     field_type = self.obj_base_page.clean_data(name['custom_field_type'])
        #     case_type = self.obj_base_page.clean_data(name['custom_custom_value_type'])
        #     field_name = self.obj_base_page.strip_data(name['custom_field_name'])
        #     case_id = name['id']
        #     test_case_title = name['title']
        #     obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
        #     self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
        #     res_checkout_form_designer, message = obj_checkout_form_designer.add_name(field_name, field_type,
        #                                                                                   case_type, self.section_type)
        #     if (res_checkout_form_designer):
        #         if case_type in ['empty', 'invalid']:
        #             result, status = "Passed", 1
        #         else:
        #             # Check for checkout page for added field
        #             obj_checkout_page = CheckoutPage(self.driver)
        #             self.get_url(os.environ.get('WCFEF_CHECKOUT_PAGE_URL'))
        #             result_checkout, message = obj_checkout_page.check_name(field_name, case_type,
        #                                                                         self.section_type, field_type)
        #             if (result_checkout):
        #                 result, status = "Passed", 1
        #             else:
        #                 result, status = "Failed", 5
        #     else:
        #         result, status = "Failed", 5
        #     self.print_message(test_case_title, status,  [field_name, field_type],
        #                                                             message, result, logger, case_id)

    def test_field_label(self, logger):
        self.field_label('billing_custom_checkboxgroup_field_label', logger, section_type=self.section_type, action_type=self.action_type)

        # section_data_label = self.get_section_data('billing_custom_checkboxgroup_field_label')
        # for label in section_data_label:
        #     field_type = self.obj_base_page.clean_data(label['custom_field_type'])
        #     field_label = self.obj_base_page.strip_data(label['custom_field_label'])
        #     case_type = self.obj_base_page.clean_data(label['custom_custom_value_type'])
        #     field_name = self.obj_base_page.strip_data(label['custom_field_name'])
        #     case_id = label['id']
        #     test_case_title = label['title']
        #     obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
        #     self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
        #     res_checkout_form_designer, message = obj_checkout_form_designer.add_label(field_label, case_type,
        #                                                                                    self.section_type,
        #                                                                                    self.action_type,
        #                                                                                    field_type=field_type,
        #                                                                                    field_name=field_name)
        #     if (res_checkout_form_designer):
        #         if case_type == "without fieldname":
        #             result, status = "Passed", 1
        #         else:
        #             # Check for checkout page for added field
        #             obj_checkout_page = CheckoutPage(self.driver)
        #             self.get_url(os.environ.get('WCFEF_CHECKOUT_PAGE_URL'))
        #             result_checkout, message = obj_checkout_page.check_label(field_label, field_name, case_type,
        #                                                                          self.section_type, self.action_type)
        #             if (result_checkout):
        #                 result, status = "Passed", 1
        #             else:
        #                 result, status = "Failed", 5
        #     else:
        #         result, status = "Failed", 5
        #     self.print_message(test_case_title, status,  [field_name, field_type],
        #                                                             message, result, logger, case_id)

    def test_field_default_value(self, logger):

        section_data_default_value = self.get_section_data('billing_custom_checkboxgroup_field_default_value')
        for default_values in section_data_default_value:
            default_value = self.obj_base_page.strip_data(default_values['custom_field_default_value'])
            case_type = self.obj_base_page.clean_data(default_values['custom_custom_value_type'])
            field_type = self.obj_base_page.strip_data(default_values['custom_field_type'])
            field_name = self.obj_base_page.strip_data(default_values['custom_field_name'])
            option_value_one = self.obj_base_page.strip_data(default_values['custom_option_value_one'])
            option_text_one = self.obj_base_page.strip_data(default_values['custom_option_text_one'])
            option_value_two = self.obj_base_page.strip_data(default_values['custom_option_value_two'])
            option_text_two = self.obj_base_page.strip_data(default_values['custom_option_text_two'])
            option_value_three = self.obj_base_page.strip_data(default_values['custom_option_value_three'])
            option_text_three = self.obj_base_page.strip_data(default_values['custom_option_text_three'])
            case_id = default_values['id']
            test_case_title = default_values['title']
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            res_checkout_form_designer, message = obj_checkout_form_designer.add_default_value(default_value, self.action_type, case_type, self.section_type, field_type=field_type, field_name=field_name, option_value_one=option_value_one, option_text_one=option_text_one, option_value_two=option_value_two, option_text_two=option_text_two, option_value_three=option_value_three, option_text_three=option_text_three)
            # print(res_checkout_form_designer)
            if (res_checkout_form_designer):
                if case_type in ["without fieldname", "invalid"]:
                    result, status = "Passed", 1
                else:
                    obj_my_account_page = MyAccount(self.driver)
                    self.get_url(os.environ.get('WCFEF_MY_ACCOUNT'))
                    obj_my_account_page.logout()

                    obj_product_page = ProductPage(self.driver)
                    self.get_url(os.environ.get('WCFEF_PRODUCT_PAGE_URL'))
                    obj_product_page.add_to_cart()
                    # Check for checkout page for added field
                    obj_checkout_page = CheckoutPage(self.driver)
                    self.get_url(os.environ.get('WCFEF_CHECKOUT_PAGE_URL'))
                    result_checkout, message = obj_checkout_page.check_default_value(field_name, default_value, case_type, self.section_type, self.action_type, field_type=field_type)
                    # print(result_checkout)
                    if (result_checkout):
                        result, status = "Passed", 1
                        self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
                        username = os.environ.get('WCFEF_USERNAME')
                        password = os.environ.get('WCFEF_PASSWORD')

                        login = LoginWordPress(self.driver)
                        login.login_wordpress_dashboard(username, password)
                    else:
                        result, status = "Failed", 5
                        self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
                        username = os.environ.get('WCFEF_USERNAME')
                        password = os.environ.get('WCFEF_PASSWORD')

                        login = LoginWordPress(self.driver)
                        login.login_wordpress_dashboard(username, password)
            else:
                result, status = "Failed", 5
            self.print_message(test_case_title, status, [field_name, field_type, default_value],
                                                                    message, result, logger, case_id)

    def test_field_class(self, logger):

        section_data_field_class = self.get_section_data('billing_custom_checkboxgroup_field_class')
        for field_class in section_data_field_class:
            field_type = self.obj_base_page.clean_data(field_class['custom_field_type'])
            field_name = self.obj_base_page.strip_data(field_class['custom_field_name'])
            field_class_value = self.obj_base_page.strip_data(field_class['custom_field_class'])
            case_id = field_class['id']
            test_case_title = field_class['title']
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            res_checkout_form_designer, message = obj_checkout_form_designer.add_field_class(field_class_value, self.section_type, self.action_type, field_type=field_type, field_name=field_name)
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

    def test_required(self, logger):

        section_data_required = self.get_section_data('billing_custom_checkboxgroup_required')
        for required in section_data_required:
            field_type = self.obj_base_page.clean_data(required['custom_field_type'])
            field_name = self.obj_base_page.strip_data(required['custom_field_name'])
            field_label = self.obj_base_page.strip_data(required['custom_field_label'])
            test_case_type = self.obj_base_page.clean_data(required['custom_custom_value_type'])
            case_id = required['id']
            field_input = self.obj_base_page.strip_data(required['custom_field_input_value'])
            option_value_one = self.obj_base_page.strip_data(required['custom_option_value_one'])
            option_text_one = self.obj_base_page.strip_data(required['custom_option_text_one'])
            option_value_two = self.obj_base_page.strip_data(required['custom_option_value_two'])
            option_text_two = self.obj_base_page.strip_data(required['custom_option_text_two'])
            option_value_three = self.obj_base_page.strip_data(required['custom_option_value_three'])
            option_text_three = self.obj_base_page.strip_data(required['custom_option_text_three'])
            test_case_title = required['title']
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            res_checkout_form_designer, message = obj_checkout_form_designer.add_required(field_name, field_label, test_case_type, self.section_type, self.action_type, field_type=field_type, option_value_one=option_value_one, option_text_one=option_text_one, option_value_two=option_value_two,
            option_text_two=option_text_two, option_value_three=option_value_three, option_text_three=option_text_three)
            obj_product_page = ProductPage(self.driver)
            self.get_url(os.environ.get('WCFEF_PRODUCT_PAGE_URL'))
            obj_product_page.add_to_cart()
            if (res_checkout_form_designer):
                # Check for checkout page for added field
                obj_checkout_page = CheckoutPage(self.driver)
                self.get_url(os.environ.get('WCFEF_CHECKOUT_PAGE_URL'))
                result_checkout, message = obj_checkout_page.check_required(field_name, self.section_type, test_case_type, self.action_type, field_type=field_type, field_input=field_input)
                if (result_checkout):
                    result, status = "Passed", 1
                else:
                    result, status = "Failed", 5
            else:
                result, status = "Failed", 5
            self.print_message(test_case_title, status,  [field_name, field_label],
                                                                    message,
                                                                    result, logger, case_id)

    def test_enable_field(self, logger):

        section_data_enable_field = self.get_section_data('billing_custom_checkboxgroup_enable_field')
        for enable_field in section_data_enable_field:
            field_type = self.obj_base_page.clean_data(enable_field['custom_field_type'])
            field_name = self.obj_base_page.strip_data(enable_field['custom_field_name'])
            case_type = self.obj_base_page.clean_data(enable_field['custom_custom_value_type'])
            case_id = enable_field['id']
            test_case_title = enable_field['title']
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            res_checkout_form_designer, message = obj_checkout_form_designer.add_field_enable(case_type,
                                                                                                  self.section_type,
                                                                                                  self.action_type,
                                                                                                  field_type=field_type,
                                                                                                  field_name=field_name)

            if (res_checkout_form_designer):
                # Check for checkout page for added field
                obj_checkout_page = CheckoutPage(self.driver)
                self.get_url(os.environ.get('WCFEF_CHECKOUT_PAGE_URL'))
                result_checkout, message = obj_checkout_page.check_field_enable(field_name, case_type,
                                                                                    self.section_type,
                                                                                    field_type=field_type)
                if (result_checkout):
                    result, status = "Passed", 1
                else:
                    result, status = "Failed", 5
            else:
                result, status = "Failed", 5
            self.print_message(test_case_title, status,  [field_name, field_type],
                                                                    message,
                                                                    result, logger, case_id)

    def test_display_order(self, logger):

        section_data_display_order = self.get_section_data('billing_custom_checkboxgroup_display_order')
        for display_order in section_data_display_order:
            field_type = self.obj_base_page.clean_data(display_order['custom_field_type'])
            field_name = self.obj_base_page.strip_data(display_order['custom_field_name'])
            field_label = self.obj_base_page.strip_data(display_order['custom_field_label'])
            case_type = self.obj_base_page.clean_data(display_order['custom_custom_value_type'])
            field_input = self.obj_base_page.strip_data(display_order['custom_field_input_value'])
            option_value_one = self.obj_base_page.strip_data(display_order['custom_option_value_one'])
            option_text_one = self.obj_base_page.strip_data(display_order['custom_option_text_one'])
            option_value_two = self.obj_base_page.strip_data(display_order['custom_option_value_two'])
            option_text_two = self.obj_base_page.strip_data(display_order['custom_option_text_two'])
            option_value_three = self.obj_base_page.strip_data(display_order['custom_option_value_three'])
            option_text_three = self.obj_base_page.strip_data(display_order['custom_option_text_three'])
            case_id = display_order['id']
            test_case_title = display_order['title']
            obj_product_page = ProductPage(self.driver)
            self.get_url(os.environ.get('WCFEF_PRODUCT_PAGE_URL'))
            obj_product_page.add_to_cart()
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            res_checkout_form_designer, message = obj_checkout_form_designer.add_display_order(field_type, field_name, field_label, case_type, self.section_type, option_value_one=option_value_one, option_text_one=option_text_one, option_value_two=option_value_two, option_text_two=option_text_two, option_value_three=option_value_three, option_text_three=option_text_three)
            if (res_checkout_form_designer):
                # Check for checkout page for added field
                obj_checkout_page = CheckoutPage(self.driver)
                self.get_url(os.environ.get('WCFEF_CHECKOUT_PAGE_URL'))
                result_checkout, message = obj_checkout_page.place_order(field_name, self.section_type, field_type, field_input=field_input)
                if (result_checkout):
                    obj_thank_you_page = ThankYouPage(self.driver)
                    result_thank_you, message = obj_thank_you_page.check_order_page(field_label, field_input, case_type)
                    if (result_thank_you):
                        result, status = "Passed", 1
                    else:
                        result, status = "Failed", 5
                else:
                    result, status = "Failed", 5
            else:
                result, status = "Failed", 5
            self.print_message(test_case_title, status,
                                                                    [field_name, field_type, field_input, field_label],
                                                                    message,
                                                                    result, logger, case_id)

    def test_create_field(self, logger):
        section_data_label = self.get_section_data('billing_custom_checkboxgroup_create_field')
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
            field_type = label['custom_field_type']
            field_name = label['custom_field_name']
            field_label = label['custom_field_label'] if ((label['custom_field_label'] == "") or (label['custom_field_label'] is None)) else label['custom_field_label'].strip()
            field_input = label['custom_field_input_value']
            option_value_one = label['custom_option_value_one']
            option_text_one = label['custom_option_text_one']
            option_value_two = label['custom_option_value_two']
            option_text_two = label['custom_option_text_two']
            option_value_three = label['custom_option_value_three']
            option_text_three = label['custom_option_text_three']
            case_type = 'valid'
            case_id = label['id']
            test_case_title = label['title']
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            res_checkout_form_designer, message = obj_checkout_form_designer.add_label(field_label, case_type, self.section_type, self.action_type, field_type=field_type, field_name=field_name, option_value_one=option_value_one, option_text_one=option_text_one, option_value_two=option_value_two, option_text_two=option_text_two, option_value_three=option_value_three, option_text_three=option_text_three)
            if (res_checkout_form_designer):
                # Check for checkout page for added field
                obj_checkout_page = CheckoutPage(self.driver)
                self.get_url(os.environ.get('WCFEF_CHECKOUT_PAGE_URL'))
                result_checkout, message = obj_checkout_page.edit_field(field_name, field_label, self.section_type, first_name, last_name, company, country, street_address, apartment, town, state, post_code, phone, email, billing_field_input=field_input, field_type=field_type)
                if (result_checkout):
                    # time.sleep(3)
                    obj_thank_you_page = ThankYouPage(self.driver)
                    result_thank_you, message = obj_thank_you_page.edit_field(field_input, self.section_type, self.action_type, field_label=field_label)
                    if (result_thank_you):
                        obj_admin_order_page = AdminOrderPage(self.driver)
                        self.get_url(os.environ.get('WCFEF_WOOCOMMERCE_ORDERS_URL'))
                        result_admin_order, message = obj_admin_order_page.edit_field(field_input, field_name, self.section_type, self.action_type, field_label=field_label)
                        if (result_admin_order):
                            result, status = "Passed", 1
                            # obj_testrail.pass_testrail(self.run_id, case_id, message)
                            self.print_message(test_case_title, status,
                                                                                [field_input, field_label, field_name,
                                                                                 field_type],
                                                                                message, result, logger, case_id)
                        else:
                            result, status = "Failed", 5
                            # obj_testrail.fail_testrail(self.run_id, case_id, message)
                            self.print_message(test_case_title, status,
                                                                                [field_input, field_label, field_name,
                                                                                 field_type],
                                                                                message, result, logger, case_id)
                    else:
                        result, status = "Failed", 5
                        # obj_testrail.fail_testrail(self.run_id, case_id, message)
                        self.print_message(test_case_title, status,
                                                                            [field_input, field_label, field_name,
                                                                             field_type],
                                                                            message,
                                                                            result, logger, case_id)
                else:
                    result, status = "Failed", 5
                    # obj_testrail.fail_testrail(self.run_id, case_id, message)
                    self.print_message(test_case_title, status,
                                                                        [field_input, field_label, field_name,
                                                                         field_type],
                                                                        message,
                                                                        result, logger, case_id)
            else:
                result, status = "Failed", 5
                # obj_testrail.fail_testrail(self.run_id, case_id, message)
                self.print_message(test_case_title, status,
                                                                    [field_input, field_label, field_name,
                                                                     field_type],
                                                                    message,
                                                                    result, logger, case_id)


    @classmethod
    def tearDownClass(cls):
        print("Custom CheckboxGroup Completed")
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
