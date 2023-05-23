from pages.productpage import ProductPage
from pages.cartpage import CartPage
import logging
from dotenv import load_dotenv
import datetime
import os, time
from pages.checkoutformdesigner import CheckoutFormDesigner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.basepage import BasePage
from section_id import section_id
from pages.testrailpage import TestRailPage
from tests.createtestrun import CreateTestRun
from sqlitedict import SqliteDict
import json
from sys import stdout
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.loginpage import LoginWordPress
from pages.checkoutpage import CheckoutPage
from pages.thankyoupage import ThankYouPage
from pages.adminorderpage import AdminOrderPage
from pages.myaccount import MyAccount

load_dotenv()


class BaseTest():

    def test_preparation(self):
        obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
        obj_checkout_form_designer.reset_field()
        obj_checkout_form_designer.enable_priority()

        obj_cart_page = CartPage(self.driver)
        self.get_url(os.environ.get('WCFEF_CART_PAGE_URL'))
        obj_cart_page.clear_cart()

        obj_product_page = ProductPage(self.driver)
        self.get_url(os.environ.get('WCFEF_PRODUCT_PAGE_URL'))
        obj_product_page.add_to_cart()

    def delete_logging_report(self, current_path):
        folder = 'reports'
        path = current_path + '/' + folder
        # Check whether the specified path exists or not
        isExist = os.path.exists(path)
        if not isExist:
            # Create a new directory because it does not exist
            os.makedirs(path)
        for f in os.listdir('reports/'):
            os.remove(os.path.join('reports/', f))

    def create_logging_report(self, run_id, current_path):

        logging.basicConfig(filename="reports/" + str(run_id) + "wcfe-report.log",
                            filemode='w')

        logger = logging.getLogger("requests")
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(stdout)
        return logger

    def log_section_gap(self, logger, section_name):
        logger.info("  ")
        logger.info("------------"+section_name+"----------------")

    def print_message(self, title, status, values, message, result, logger, case_id):
        print_message = 'Result : ', result if result else "", ', Title : ', title if title else "", ', Values : ', values if values else "", ', Message : ', message if message else ""
        logger.info(print_message)

        ################################################
        #### SQLDICT
        db = SqliteDict("CFE.db", tablename="cfe", autocommit=True)
        res = []
        val = {"case_id": case_id, "status_id": status, "comment": message}

        flag = False
        for key, item in db.items():
            if "Results" in key:
            	flag = True
            	break
        if flag:
            value = json.loads(db["Results"])
            if val in value:
                pass
            else:
                value.append(val)
            db["Results"] = json.dumps(value)
        else:
            res.append(val)
            db["Results"] = json.dumps(res)

    def create_env_variables(self):
        os.environ['WCFEF_LOGIN_URL'] = os.environ.get('WCFEF_SITE') + "wp-admin/admin.php?page=checkout_form_designer"
        os.environ['WCFEF_PRODUCT_PAGE_URL'] = os.environ.get('WCFEF_SITE') + "product/" + os.environ.get('WCFEF_PRODUCT_NAME')
        os.environ['WCFEF_CART_PAGE_URL'] = os.environ.get('WCFEF_SITE') + "cart/"
        os.environ['WCFEF_CHECKOUT_PAGE_URL'] = os.environ.get('WCFEF_SITE') + "checkout/"
        os.environ['WCFEF_MY_ACCOUNT'] = os.environ.get('WCFEF_SITE') + "my-account/"
        os.environ['WCFEF_MY_ACCOUNT_ORDERS_URL'] = os.environ.get('WCFEF_MY_ACCOUNT') + "orders/"
        os.environ['WCFEF_WOOCOMMERCE_ORDERS_URL'] = os.environ.get('WCFEF_SITE') + "wp-admin/edit.php?post_type=shop_order"
        os.environ['WCFEF_ADVANCED_SETTINGS_URL'] = os.environ.get('WCFEF_SITE') + "wp-admin/edit.php?post_type=product&page=thWCFEF_extra_product_options&tab=advanced_settings"
        os.environ['WCFEF_SHOP_PAGE_URL'] = os.environ.get('WCFEF_MY_ACCOUNT') + "shop/"
        os.environ['WCFEF_EDIT_ADDRESS_BILLING'] = os.environ.get('WCFEF_MY_ACCOUNT') + "edit-address/billing/"
        os.environ['WCFEF_EDIT_ADDRESS_SHIPPING'] = os.environ.get('WCFEF_MY_ACCOUNT') + "edit-address/shipping/"

    def get_url(self, url):
        obj_base_page = BasePage(self.driver)
        try:
            obj_base_page.wait_page_load()
            self.driver.get(url)
        except:
            self.driver.refresh()
            self.driver.get(url)
        obj_base_page.wait_page_load()

    def store_section_data(self):
        print("Wait until the testrail data to be stored")
        db = SqliteDict("CFE.db", tablename="cfe", autocommit=True)
        for i  in section_id:
            for value in section_id[i]:
                obj_testrail = TestRailPage()
                section_data = obj_testrail.get_section_data(section_id[i][value])
                db[str(i) +'_'+ str(value)] = json.dumps(section_data)

    def get_section_data(self, section_name):
        db = SqliteDict("CFE.db", tablename="cfe", autocommit=True)

        flag = False
        for key, item in db.items():
            if section_name in key:
            	flag = True
            	break
        if flag:
            get_val = db[section_name]
            if get_val:
                values = json.loads(get_val)
                return values

    def delete_result(self):
        db = SqliteDict("CFE.db", tablename="cfe", autocommit=True)
        flag = False
        for key, item in db.items():
            if "Results" in key:
            	flag = True
            	break
        if flag:
            del db["Results"]

    def field_name(self, section_name, logger):
        section_data_name = self.get_section_data(section_name)
        for name in section_data_name:
            obj_base_page = BasePage(self.driver)
            field_type = obj_base_page.clean_data(name['custom_field_type'])
            case_type = obj_base_page.clean_data(name['custom_custom_value_type'])
            field_name = obj_base_page.strip_data(name['custom_field_name'])
            field_label = self.obj_base_page.strip_data(name['custom_field_label'])
            print(field_label)
            case_id = name['id']
            test_case_title = name['title']
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            if field_type == "paragraph":
                res_checkout_form_designer, message = obj_checkout_form_designer.add_name(field_name, field_type,
                                                                                                  case_type, self.section_type, field_content=field_label)
            else:
                res_checkout_form_designer, message = obj_checkout_form_designer.add_name(field_name, field_type,
                                                                                          case_type, self.section_type, field_label=field_label)
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

    def field_label(self, section_name, logger, section_type="", action_type="", row="", field_name=""):


        section_data_label = self.get_section_data(section_name)
        for label in section_data_label:
            field_type = self.obj_base_page.clean_data(label['custom_field_type'])
            field_label = self.obj_base_page.strip_data(label['custom_field_label'])
            case_type = self.obj_base_page.clean_data(label['custom_custom_value_type'])
            field_name = self.obj_base_page.strip_data(label['custom_field_name'])
            case_id = label['id']
            test_case_title = label['title']
            obj_checkout_form_designer = CheckoutFormDesigner(self.driver)
            self.get_url(os.environ.get('WCFEF_LOGIN_URL'))
            if action_type == "edit":
                res_checkout_form_designer, message = obj_checkout_form_designer.add_label(field_label, case_type, self.section_type, self.action_type, row=self.row)
            else:
                res_checkout_form_designer, message = obj_checkout_form_designer.add_label(field_label, case_type,
                                                                                               self.section_type,
                                                                                               self.action_type,
                                                                                               field_type=field_type,
                                                                                               field_name=field_name)
            if (res_checkout_form_designer):
                if case_type == "without fieldname":
                    result, status = "Passed", 1
                    self.print_message(test_case_title, status,  [field_name, field_type, field_label],
                                                                 message, result, logger, case_id)
                else:
                    # Check for checkout page for added field
                    obj_checkout_page = CheckoutPage(self.driver)
                    self.get_url(os.environ.get('WCFEF_CHECKOUT_PAGE_URL'))
                    if action_type == "edit":
                        result_checkout, message = obj_checkout_page.check_label(field_label, self.field_name, case_type, self.section_type, self.action_type)
                    else:
                        result_checkout, message = obj_checkout_page.check_label(field_label, field_name, case_type,
                                                                                     self.section_type, self.action_type, field_type=field_type)
                    if (result_checkout):
                        result, status = "Passed", 1
                    else:
                        result, status = "Failed", 5
            else:
                result, status = "Failed", 5
            self.print_message(test_case_title, status,  [field_name, field_type],
                                                             message, result, logger, case_id)
