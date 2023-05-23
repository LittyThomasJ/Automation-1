import unittest
from pages.checkoutformdesigner import CheckoutFormDesigner
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
from tests.createtestrun import CreateTestRun
from pages.loginpage import LoginWordPress
from tests.basetest import BaseTest
from pages.myaccount import MyAccount
from pages.productpage import ProductPage
from pages.checkoutpage import CheckoutPage
from pages.thankyoupage import ThankYouPage
from pages.editbillingaddresspage import EditBillingPage
from pages.adminorderpage import AdminOrderPage
from pages.cartpage import CartPage
from section_id import section_id
from dotenv import load_dotenv
import time
from pages.testrailpage import TestRailPage
from pages.basepage import BasePage
import sys
sys.path.append('/Users/zennode/PycharmProjects/WCFE-Free-new')
load_dotenv()


class BillingPhone(unittest.TestCase, BaseTest):
    """ For testing all tests within billing phone testcases
    Calls to all the actions in each pages are done here
    """
    def __init__(self):
        self.row = 10
        self.field_name = 'billing_phone'
        self.section_type = 'billing'
        self.action_type = "edit"

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
    # For testing
    def test_field_label(self, logger):
        self.field_label('billing_phone_field_label', logger, section_type=self.section_type, action_type=self.action_type, row=self.row, field_name=self.field_name)

        # section_data_label = self.get_section_data('billing_phone_field_label')
        # for label in section_data_label:
        #
        #     field_label = self.obj_base_page.strip_data(label['custom_field_label'])
        #     case_type = self.obj_base_page.clean_data(label['custom_custom_value_type'])
        #     case_id = label['id']
        #     test_case_title = label['title']
        #     obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
        #     self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
        #     res_checkout_form_designer, message = obj_checkout_form_designer.add_label(field_label, case_type, self.section_type, self.action_type, row=self.row)
        #     if (res_checkout_form_designer):
        #         # Check for checkout page for added field
        #         obj_checkout_page = CheckoutPage(self.driver)
        #         self.get_url(os.environ.get('WCFEF_CHECKOUT_PAGE_URL'))
        #         result_checkout, message = obj_checkout_page.check_label(field_label, self.field_name, case_type, self.section_type, self.action_type)
        #         if (result_checkout):
        #             result, status = "Passed", 1
        #         else:
        #             result, status = "Failed", 5
        #     else:
        #         result, status = "Failed", 5
        #     self.print_message(test_case_title, status,  [self.field_name, field_label], message, result, logger, case_id)

    def test_field_placeholder(self, logger):

        section_data_placeholder = self.get_section_data('billing_phone_field_placeholder')
        for placeholder in section_data_placeholder:

            field_placeholder = self.obj_base_page.strip_data(placeholder['custom_field_place_holder'])
            case_type = self.obj_base_page.clean_data(placeholder['custom_custom_value_type'])
            case_id = placeholder['id']
            test_case_title = placeholder['title']
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            res_checkout_form_designer, message = obj_checkout_form_designer.add_placeholder(field_placeholder, case_type, self.section_type, self.action_type, row=self.row)
            if (res_checkout_form_designer):
                obj_my_account_page = MyAccount(self.driver)
                self.get_url(os.environ.get('WCFEF_MY_ACCOUNT'))
                obj_my_account_page.logout()
                obj_product_page = ProductPage(self.driver)
                self.get_url(os.environ.get('WCFEF_PRODUCT_PAGE_URL'))
                obj_product_page.add_to_cart()
                # Check for checkout page for added field
                obj_checkout_page = CheckoutPage(self.driver)
                self.get_url(os.environ.get('WCFEF_CHECKOUT_PAGE_URL'))
                result_checkout, message = obj_checkout_page.check_placeholder(self.field_name, field_placeholder, case_type, self.section_type)
                if (result_checkout):
                    result, status = "Passed", 1
                    self.print_message(test_case_title, status,  [self.field_name, field_placeholder], message, result, logger, case_id)
                    self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
                    username = os.environ.get('WCFEF_USERNAME')
                    password = os.environ.get('WCFEF_PASSWORD')
                    login = LoginWordPress(self.driver)
                    login.login_wordpress_dashboard(username, password)
                else:
                    result, status = "Failed", 5
                    self.print_message(test_case_title, status,  [self.field_name, field_placeholder], message, result, logger, case_id)
                    self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
                    username = os.environ.get('WCFEF_USERNAME')
                    password = os.environ.get('WCFEF_PASSWORD')
                    login = LoginWordPress(self.driver)
                    login.login_wordpress_dashboard(username, password)
            else:
                result, status = "Failed", 5
                self.print_message(test_case_title, status,  [self.field_name, field_placeholder], message, result, logger, case_id)

    def test_field_default_value(self, logger):

        section_data_default_value = self.get_section_data('billing_phone_field_default_value')
        for default_values in section_data_default_value:
            default_value = self.obj_base_page.strip_data(default_values['custom_field_default_value'])
            case_type = self.obj_base_page.clean_data(default_values['custom_custom_value_type'])
            case_id = default_values['id']
            test_case_title = default_values['title']
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            res_checkout_form_designer, message = obj_checkout_form_designer.add_default_value(default_value, self.action_type, case_type, self.section_type, row=self.row)
            if (res_checkout_form_designer):
                obj_my_account_page = MyAccount(self.driver)
                self.get_url(os.environ.get('WCFEF_MY_ACCOUNT'))
                obj_my_account_page.logout()
                obj_product_page = ProductPage(self.driver)
                self.get_url(os.environ.get('WCFEF_PRODUCT_PAGE_URL'))
                obj_product_page.add_to_cart()
                # Check for checkout page for added field
                obj_checkout_page = CheckoutPage(self.driver)
                self.get_url(os.environ.get('WCFEF_CHECKOUT_PAGE_URL'))
                result_checkout, message = obj_checkout_page.check_default_value(self.field_name, default_value, case_type, self.section_type, self.action_type)
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
            self.print_message(test_case_title, status,  [self.field_name, default_value], message, result, logger, case_id)

    def test_field_class(self, logger):

        section_data_field_class = self.get_section_data('billing_phone_field_class')
        for field_class in section_data_field_class:
            field_class_value = self.obj_base_page.strip_data(field_class['custom_field_class'])
            case_id = field_class['id']
            test_case_title = field_class['title']
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            res_checkout_form_designer, message = obj_checkout_form_designer.add_field_class(field_class_value, self.section_type, self.action_type, row=self.row)
            if (res_checkout_form_designer):
                # Check for checkout page for added field
                obj_checkout_page = CheckoutPage(self.driver)
                self.get_url(os.environ.get('WCFEF_CHECKOUT_PAGE_URL'))
                result_checkout, message = obj_checkout_page.check_field_class(self.field_name, field_class_value, self.section_type)
                if (result_checkout):
                    result, status = "Passed", 1
                else:
                    result, status = "Failed", 5
            else:
                result, status = "Failed", 5
            self.print_message(test_case_title, status,  [self.field_name, field_class_value], message, result, logger, case_id)

    def test_number_validation(self, logger):
        section_data_number_val = self.get_section_data('billing_phone_number_validation')
        for number_val in section_data_number_val:
            field_input = self.obj_base_page.strip_data(number_val['custom_field_input_value'])
            case_type = self.obj_base_page.clean_data(number_val['custom_custom_value_type'])
            validation_type = "number"
            case_id = number_val['id']
            test_case_title = number_val['title']
            obj_cart_page = CartPage(self.driver)
            self.get_url(os.environ.get('WCFEF_CART_PAGE_URL'))
            obj_cart_page.clear_cart()
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            res_checkout_form_designer, message = obj_checkout_form_designer.add_field_validation(validation_type, self.section_type, self.field_name, self.action_type, row=self.row)
            if (res_checkout_form_designer):
                obj_product_page = ProductPage(self.driver)
                self.get_url(os.environ.get('WCFEF_PRODUCT_PAGE_URL'))
                obj_product_page.add_to_cart()
                # Check for checkout page for added field
                obj_checkout_page = CheckoutPage(self.driver)
                self.get_url(os.environ.get('WCFEF_CHECKOUT_PAGE_URL'))
                result_checkout, message = obj_checkout_page.check_field_validation(self.field_name, field_input, case_type, validation_type, self.section_type)
                if (result_checkout):
                    result, status = "Passed", 1
                else:
                    result, status = "Failed", 5
            else:
                result, status = "Failed", 5
            self.print_message(test_case_title, status,  [self.field_name, field_input], message, result, logger, case_id)

    def test_required(self, logger):

        section_data_required = self.get_section_data('billing_phone_required')
        for required in section_data_required:
            field_label = self.obj_base_page.strip_data(required['custom_field_label'])
            test_case_type = self.obj_base_page.clean_data(required['custom_custom_value_type'])
            case_id = required['id']
            field_input = self.obj_base_page.strip_data(required['custom_field_input_value'])
            test_case_title = required['title']
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            res_checkout_form_designer, message = obj_checkout_form_designer.add_required(self.field_name, field_label, test_case_type, self.section_type, self.action_type, row=self.row)
            obj_product_page = ProductPage(self.driver)
            self.get_url(os.environ.get('WCFEF_PRODUCT_PAGE_URL'))
            obj_product_page.add_to_cart()
            if (res_checkout_form_designer):
                # Check for checkout page for added field
                obj_checkout_page = CheckoutPage(self.driver)
                self.get_url(os.environ.get('WCFEF_CHECKOUT_PAGE_URL'))
                result_checkout, message = obj_checkout_page.check_required(self.field_name, self.section_type, test_case_type, self.action_type, field_input=field_input)
                if (result_checkout):
                    result, status = "Passed", 1
                else:
                    result, status = "Failed", 5
            else:
                result, status = "Failed", 5
            self.print_message(test_case_title, status,  [self.field_name, field_label], message, result, logger, case_id)

    def test_phone_validation(self, logger):

        section_data_phone_val = self.get_section_data('billing_phone_phone_validation')
        for phone_val in section_data_phone_val:
            field_input = self.obj_base_page.strip_data(phone_val['custom_field_input_value'])
            case_type = self.obj_base_page.clean_data(phone_val['custom_custom_value_type'])
            validation_type = "phone"
            case_id = phone_val['id']
            test_case_title = phone_val['title']
            obj_cart_page = CartPage(self.driver)
            self.get_url(os.environ.get('WCFEF_CART_PAGE_URL'))
            obj_cart_page.clear_cart()
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            res_checkout_form_designer, message = obj_checkout_form_designer.add_field_validation(validation_type, self.section_type, self.field_name, self.action_type, row=self.row)
            if (res_checkout_form_designer):
                obj_product_page = ProductPage(self.driver)
                self.get_url(os.environ.get('WCFEF_PRODUCT_PAGE_URL'))
                obj_product_page.add_to_cart()
                # Check for checkout page for added field
                obj_checkout_page = CheckoutPage(self.driver)
                self.get_url(os.environ.get('WCFEF_CHECKOUT_PAGE_URL'))
                result_checkout, message = obj_checkout_page.check_field_validation(self.field_name, field_input, case_type, validation_type, self.section_type)
                if (result_checkout):
                    result, status = "Passed", 1
                else:
                    result, status = "Failed", 5
            else:
                result, status = "Failed", 5
            self.print_message(test_case_title, status,  [self.field_name, field_input], message, result, logger, case_id)

    def test_enable_field(self, logger):

        section_data_enable_field = self.get_section_data('billing_phone_enable_field')
        for enable_field in section_data_enable_field:
            case_type = self.obj_base_page.strip_data(enable_field['custom_custom_value_type'])
            case_id = enable_field['id']
            test_case_title = enable_field['title']
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            res_checkout_form_designer, message = obj_checkout_form_designer.add_field_enable(case_type, self.section_type, self.action_type,  self.row)
            if (res_checkout_form_designer):
                # Check for checkout page for added field
                obj_checkout_page = CheckoutPage(self.driver)
                self.get_url(os.environ.get('WCFEF_CHECKOUT_PAGE_URL'))
                result_checkout, message = obj_checkout_page.check_field_enable(self.field_name, case_type, self.section_type)
                if (result_checkout):
                    result, status = "Passed", 1

                else:
                    result, status = "Failed", 5
            else:
                result, status = "Failed", 5
            self.print_message(test_case_title, status,  [self.field_name], message, result, logger, case_id)

    def test_edit_field(self, logger):

        section_data_label = self.get_section_data('billing_phone_edit_field')
        for label in section_data_label:

            first_name = 'jijo'
            company = 'zenn'
            street_address = "chakkaalakkal"
            last_name = "p"
            state = "KL"
            country = "IN"
            apartment = "kkk"
            town = "manjeri"
            post_code = "687896"
            email = "litty4ever@gmail.com"
            field_label = self.obj_base_page.strip_data(label['custom_field_label'])
            phone = self.obj_base_page.strip_data(label['custom_field_input_value'])
            case_type = self.obj_base_page.clean_data(label['custom_custom_value_type'])
            case_id = label['id']
            test_case_title = label['title']
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            res_checkout_form_designer, message = obj_checkout_form_designer.add_label(field_label, case_type,
                                                                              self.section_type, self.action_type, self.row)
            if (res_checkout_form_designer):
                # Check for checkout page for added field
                obj_checkout_page = CheckoutPage(self.driver)
                self.get_url(os.environ.get('WCFEF_CHECKOUT_PAGE_URL'))
                result_checkout, message = obj_checkout_page.edit_field(self.field_name, field_label, self.section_type, first_name, last_name, company, country, street_address, apartment, town, state, post_code, phone, email)
                if (result_checkout):
                    # time.sleep(3)
                    obj_thank_you_page = ThankYouPage(self.driver)
                    result_thank_you, message = obj_thank_you_page.edit_field(phone, self.section_type, self.action_type)
                    if (result_thank_you):
                        obj_edit_billing_address = EditBillingPage(self.driver)
                        if self.section_type == "billing":
                            self.get_url(os.environ.get('WCFEF_EDIT_ADDRESS_BILLING'))
                        else:
                            self.get_url(os.environ.get('WCFEF_EDIT_ADDRESS_SHIPPING'))

                        result_edit_billing_address, message = obj_edit_billing_address.check_edit_billing_address(self.field_name, phone)
                        if (result_edit_billing_address):
                            obj_admin_order_page = AdminOrderPage(self.driver)
                            self.get_url(os.environ.get('WCFEF_WOOCOMMERCE_ORDERS_URL'))
                            result_admin_order, message_five = obj_admin_order_page.edit_field(phone, self.field_name, self.section_type, self.action_type)
                            if (result_admin_order):
                                result, status = "Passed", 1
                            else:
                                result, status = "Failed", 5
                        else:
                            result, status = "Failed", 5
                    else:
                        result, status = "Failed", 5
                else:
                    result, status = "Failed", 5
            else:
                result, status = "Failed", 5
            self.print_message(test_case_title, status,  [post_code, field_label], message, result, logger, case_id)

    @classmethod
    def tearDownClass(cls):
        print("Billing Phone Completed")
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
