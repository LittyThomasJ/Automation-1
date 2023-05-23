from tests.createtestrun import CreateTestRun
from tests.closetestrun import CloseTestRun
from tests.billingfirstnametest import BillingFirstName
from tests.billinglastnametest import BillingLastName
from tests.billingcompanytest import BillingCompany
from tests.billingcountrytest import BillingCountry
from tests.billingaddressone import BillingAddressOne
from tests.billingaddresstwo import BillingAddressTwo
from tests.billingcityone import BillingCity
from tests.billingpostcode import BillingPostCode
from tests.billingphonetest import BillingPhone
from tests.billingemailtest import BillingEmail
from tests.shippingfirstnametest import ShippingFirstName
from tests.shippinglastnametest import ShippingLastName
from tests.shippingcompanytest import ShippingCompany
from tests.shippingcountrytest import ShippingCountry
from tests.shppingaddressonetest import ShippingAddressOne
from tests.shippingaddresstwotest import ShippingAddressTwo
from tests.shippingcitytest import ShippingCity
from tests.shippingpostcodetest import ShippingPostCode
from tests.billingcustomtext import BillingCustomText
from tests.ordercommentstest import OrderComments
from tests.billingcustompassword import BillingCustomPassword
from tests.billingcustomemail import BillingCustomEmail
from tests.billingcustomphone import BillingCustomPhone
from tests.billingcustomtextarea import BillingCustomTextarea
from tests.billingcustomselect import BillingCustomSelect
from tests.billingcustomradio import BillingCustomRadio
from tests.billingcustomhidden import BillingCustomHidden
from tests.advancedbillingoverride import AdvancedBillingOverride
from tests.billingstate import BillingState
from tests.shippingstate import ShippingState
from tests.billingcustommultiselect import BillingCustomMultiselect
from tests.billingcustomnumber import BillingCustomNumber
from tests.billingcustomcheckbox import BillingCustomCheckbox
from tests.billingcustomcheckboxgroup import BillingCustomCheckboxGroup
from tests.billingcustomheading import BillingCustomHeading
from tests.customdatetimelocal import CustomDateTimeLocal
from tests.customdate import CustomDate
from tests.custommonth import CustomMonth
from tests.customtime import CustomTime
from tests.customweek import CustomWeek
from tests.customurl import CustomUrl
from tests.customparagraph import CustomParagraph
from tests.basetest import BaseTest
import os
import chime
import traceback
from dotenv import load_dotenv
load_dotenv()

try:
    chime.success()
    """ We used POM model"""
    """ Here we are doing the calls to test """
    obj_base_test = BaseTest()
    obj_base_test.create_env_variables()

    """For creating new Test run in testrail """
    CreateTestRun.setUpClass()
    obj_create_test_run = CreateTestRun()
    run_id = obj_create_test_run.test_add_test_run()
    CreateTestRun.tearDownClass()

    """ For storing testrail data to a database """
    obj_base_test.store_section_data()
    """Delete previous result from datatbase"""
    obj_base_test.delete_result()

    """Call logging to delete previous and create new"""
    current_path = os.getcwd()
    obj_base_test.delete_logging_report(current_path)
    logger = obj_base_test.create_logging_report(run_id, current_path)

    chime.success()
    """ Billing first name """
    BillingFirstName.setUpClass()
    obj_billing_first_name = BillingFirstName()
    obj_billing_first_name.test_preparation()
    obj_base_test.log_section_gap(logger, "Billing First Name :- Label")
    obj_billing_first_name.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Billing First Name :- Placeholder")
    obj_billing_first_name.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Billing First Name :- Default Value")
    obj_billing_first_name.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Billing First Name :- Field Class")
    obj_billing_first_name.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Billing First Name :- Enable Field")
    obj_billing_first_name.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Billing First Name :- Edit Field")
    obj_billing_first_name.test_edit_field(logger)

    obj_base_test.log_section_gap(logger, "Billing First Name :- Required")
    obj_billing_first_name.test_required(logger)
    BillingFirstName.tearDownClass()
    chime.success()

    """ Billing last name """
    BillingLastName.setUpClass()
    obj_billing_last_name = BillingLastName()
    obj_billing_last_name.test_preparation()
    obj_base_test.log_section_gap(logger, "Billing Last Name :- Label")
    obj_billing_last_name.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Billing Last Name :- Placeholder")
    obj_billing_last_name.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Billing Last Name :- Default Value")
    obj_billing_last_name.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Billing Last Name :- Field Class")
    obj_billing_last_name.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Billing Last Name :- Enable Field")
    obj_billing_last_name.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Last Name :- Edit Field")
    obj_billing_last_name.test_edit_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Last Name :- Required")
    obj_billing_last_name.test_required(logger)

    BillingLastName.tearDownClass()
    chime.success()

    """ Billing company """
    BillingCompany.setUpClass()
    obj_billing_company = BillingCompany()
    obj_billing_company.test_preparation()
    obj_base_test.log_section_gap(logger, "Billing Company :- Label")
    obj_billing_company.test_field_label(logger)
    #
    obj_base_test.log_section_gap(logger, "Billing Company :- Placeholder")
    obj_billing_company.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Billing Company :- Default Value")
    obj_billing_company.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Billing Company :- Field class")
    obj_billing_company.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Billing Company :- Enable Field")
    obj_billing_company.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Company :- Edit Field")
    obj_billing_company.test_edit_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Company :- Required")
    obj_billing_company.test_required(logger)
    BillingCompany.tearDownClass()
    chime.success()

    """ Billing country """
    BillingCountry.setUpClass()
    obj_billing_country = BillingCountry()
    obj_billing_country.test_preparation()
    obj_base_test.log_section_gap(logger, "Billing country :- Label")
    obj_billing_country.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Billing country :- Placeholder")
    obj_billing_country.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Billing country :- Default Value")
    obj_billing_country.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Billing country :- Field Class")
    obj_billing_country.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Billing country :- Enable Field")
    obj_billing_country.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Billing country :- Edit Field")
    obj_billing_country.test_edit_field(logger)

    obj_base_test.log_section_gap(logger, "Billing country :- Required")
    obj_billing_country.test_required(logger)
    BillingCountry.tearDownClass()
    chime.success()

    """ Billing Address One """
    BillingAddressOne.setUpClass()
    obj_billing_address_one = BillingAddressOne()
    obj_billing_address_one.test_preparation()
    obj_base_test.log_section_gap(logger, "Billing Address One :- Label")
    obj_billing_address_one.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Billing Address One :- Placeholder")
    obj_billing_address_one.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Billing Address One :- Default value")
    obj_billing_address_one.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Billing Address One :- Field class")
    obj_billing_address_one.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Billing Address One :- Enable Field")
    obj_billing_address_one.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Address One :- Edit Field")
    obj_billing_address_one.test_edit_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Address One :- Required")
    obj_billing_address_one.test_required(logger)
    BillingAddressOne.tearDownClass()
    chime.success()

    """Billing Address Two"""
    BillingAddressTwo.setUpClass()
    obj_billing_address_two = BillingAddressTwo()
    obj_billing_address_two.test_preparation()
    obj_base_test.log_section_gap(logger, "Billing Address Two :- Label")
    obj_billing_address_two.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Billing Address Two :- Placeholder")
    obj_billing_address_two.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Billing Address Two :- Default Value")
    obj_billing_address_two.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Billing Address Two :- Field Class")
    obj_billing_address_two.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Billing Address Two :- Enable Field")
    obj_billing_address_two.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Address Two :- Edit Field")
    obj_billing_address_two.test_edit_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Address Two :- Required")
    obj_billing_address_two.test_required(logger)

    BillingAddressTwo.tearDownClass()
    chime.success()

    """Billing City"""
    BillingCity.setUpClass()
    obj_billing_city = BillingCity()
    obj_billing_city.test_preparation()
    obj_base_test.log_section_gap(logger, "Billing City :- Label")
    obj_billing_city.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Billing City :- Placeholder")
    obj_billing_city.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Billing City :- Default Value")
    obj_billing_city.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Billing City :- Field class")
    obj_billing_city.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Billing City :- Enable Field")
    obj_billing_city.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Billing City :- Edit Field")
    obj_billing_city.test_edit_field(logger)

    obj_base_test.log_section_gap(logger, "Billing City :- Required")
    obj_billing_city.test_required(logger)
    BillingCity.tearDownClass()
    chime.success()

    """Billing State"""
    BillingState.setUpClass()
    obj_billing_state = BillingState()
    obj_billing_state.test_preparation()
    obj_base_test.log_section_gap(logger, "Billing State :- Label")
    obj_billing_state.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Billing State :- Placeholder")
    obj_billing_state.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Billing State :- Default Value")
    obj_billing_state.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Billing State :- Enable Field")
    obj_billing_state.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Billing State :- Field Class")
    obj_billing_state.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Billing State :- Edit Field")
    obj_billing_state.test_edit_field(logger)

    obj_base_test.log_section_gap(logger, "Billing State :- State Validation")
    obj_billing_state.test_state_validation(logger)

    obj_base_test.log_section_gap(logger, "Billing State :- Required")
    obj_billing_state.test_required(logger)
    BillingState.tearDownClass()
    chime.success()

    """ Billing Postcode """
    BillingPostCode.setUpClass()
    obj_billing_postcode = BillingPostCode()
    obj_billing_postcode.test_preparation()
    obj_base_test.log_section_gap(logger, "Billing Postcode :- Label")
    obj_billing_postcode.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Billing Postcode :- Placeholder")
    obj_billing_postcode.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Billing Postcode :- Default value")
    obj_billing_postcode.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Billing Postcode :- Field Class")
    obj_billing_postcode.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Billing Postcode :- Enable Field")
    obj_billing_postcode.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Postcode :- Edit Field")
    obj_billing_postcode.test_edit_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Postcode :- Post Code Validation")
    obj_billing_postcode.test_post_code_validation(logger)

    obj_base_test.log_section_gap(logger, "Billing Postcode :- Number Validation")
    obj_billing_postcode.test_number_validation(logger)

    obj_base_test.log_section_gap(logger, "Billing Postcode :- Required")
    obj_billing_postcode.test_required(logger)
    BillingPostCode.tearDownClass()
    chime.success()

    """ Billing Phone"""
    BillingPhone.setUpClass()
    obj_billing_phone = BillingPhone()
    obj_billing_phone.test_preparation()
    obj_base_test.log_section_gap(logger, "Billing Phone :- Label")
    obj_billing_phone.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Billing Phone :- Placeholder")
    obj_billing_phone.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Billing Default Value :- Placeholder")
    obj_billing_phone.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Billing Phone :- Field Class")
    obj_billing_phone.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Billing Phone :- Enable Field")
    obj_billing_phone.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Phone :- Edit Field")
    obj_billing_phone.test_edit_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Phone :- Required")
    obj_billing_phone.test_required(logger)

    obj_base_test.log_section_gap(logger, "Billing Phone :- Phone Validation")
    obj_billing_phone.test_phone_validation(logger)

    obj_base_test.log_section_gap(logger, "Billing Phone :- Number validation")
    obj_billing_phone.test_number_validation(logger)

    BillingPhone.tearDownClass()
    chime.success()

    """ Billing Email """
    BillingEmail.setUpClass()
    obj_billing_email = BillingEmail()
    obj_billing_email.test_preparation()
    obj_base_test.log_section_gap(logger, "Billing Email :- Label")
    obj_billing_email.test_field_label(logger)
    #
    obj_base_test.log_section_gap(logger, "Billing Placeholder :- Placeholder")
    obj_billing_email.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Billing Email :- Default value")
    obj_billing_email.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Billing Email :- Field Class")
    obj_billing_email.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Billing Email :- Enable Field")
    obj_billing_email.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Email :- Edit field")
    obj_billing_email.test_edit_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Email :- Email Validation")
    obj_billing_email.test_email_validation(logger)

    obj_base_test.log_section_gap(logger, "Billing Email :- Required")
    obj_billing_email.test_required(logger)
    BillingEmail.tearDownClass()
    chime.success()

    """ Shipping First name"""
    ShippingFirstName.setUpClass()
    obj_shipping_first_name = ShippingFirstName()
    obj_shipping_first_name.test_preparation()
    obj_base_test.log_section_gap(logger, "Shipping First name :- Label")
    obj_shipping_first_name.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Shipping First name :- Placeholder")
    obj_shipping_first_name.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Shipping First name :- Default Value")
    obj_shipping_first_name.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Shipping First name :- field class")
    obj_shipping_first_name.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Shipping First name :- Enable Field")
    obj_shipping_first_name.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Shipping First name :- Edit Field")
    obj_shipping_first_name.test_edit_field(logger)

    obj_base_test.log_section_gap(logger, "Shipping First name :- Required")
    obj_shipping_first_name.test_required(logger)
    ShippingFirstName.tearDownClass()
    chime.success()

    """ Shipping Last Name"""
    ShippingLastName.setUpClass()
    obj_shipping_last_name = ShippingLastName()
    obj_shipping_last_name.test_preparation()
    obj_base_test.log_section_gap(logger, "Shipping Last name :- Label")
    obj_shipping_last_name.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Shipping Last name :- Placeholder")
    obj_shipping_last_name.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Shipping Last name :- Default Value")
    obj_shipping_last_name.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Shipping Last name :- Field Class")
    obj_shipping_last_name.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Shipping Last name :- Enable Field")
    obj_shipping_last_name.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Shipping Last name :- Edit field")
    obj_shipping_last_name.test_edit_field(logger)

    obj_base_test.log_section_gap(logger, "Shipping Last name :- Required")
    obj_shipping_last_name.test_required(logger)
    ShippingLastName.tearDownClass()
    chime.success()

    """ Shipping Company"""
    ShippingCompany.setUpClass()
    obj_shipping_company = ShippingCompany()
    obj_shipping_company.test_preparation()
    obj_base_test.log_section_gap(logger, "Shipping Company :- Label")
    obj_shipping_company.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Shipping Company :- Placeholder")
    obj_shipping_company.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Shipping Company :- Default Value")
    obj_shipping_company.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Shipping Company :- Field Class")
    obj_shipping_company.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Shipping Company :- Enable Field")
    obj_shipping_company.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Shipping Company :- Edit field")
    obj_shipping_company.test_edit_field(logger)

    obj_base_test.log_section_gap(logger, "Shipping Company :- Required")
    obj_shipping_company.test_required(logger)
    ShippingCompany.tearDownClass()
    chime.success()

    """ Shipping Country"""
    ShippingCountry.setUpClass()
    obj_shipping_country = ShippingCountry()
    obj_shipping_country.test_preparation()
    obj_base_test.log_section_gap(logger, "Shipping Country :- Label")
    obj_shipping_country.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Shipping Country :- Placeholder")
    obj_shipping_country.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Shipping Country :- Default Value")
    obj_shipping_country.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Shipping Country :- Field Class")
    obj_shipping_country.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Shipping Country :- Enable Field")
    obj_shipping_country.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Shipping Country :- Edit field")
    obj_shipping_country.test_edit_field(logger)

    obj_base_test.log_section_gap(logger, "Shipping Country :- Required")
    obj_shipping_country.test_required(logger)
    ShippingCountry.tearDownClass()
    chime.success()

    """ Shipping Address One"""
    ShippingAddressOne.setUpClass()
    obj_shipping_address_one = ShippingAddressOne()
    obj_shipping_address_one.test_preparation()
    obj_base_test.log_section_gap(logger, "Shipping Address One :- Label")
    obj_shipping_address_one.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Shipping Address One :- Placeholder")
    obj_shipping_address_one.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Shipping Address One :- Default Value")
    obj_shipping_address_one.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Shipping Address One :- Field Class")
    obj_shipping_address_one.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Shipping Address One :- Enable Field")
    obj_shipping_address_one.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Shipping Address One :- Edit field")
    obj_shipping_address_one.test_edit_field(logger)

    obj_base_test.log_section_gap(logger, "Shipping Address One :- Required")
    obj_shipping_address_one.test_required(logger)
    ShippingAddressOne.tearDownClass()
    chime.success()

    """ Shipping Address Two """
    ShippingAddressTwo.setUpClass()
    obj_shipping_address_two = ShippingAddressTwo()
    obj_shipping_address_two.test_preparation()
    obj_base_test.log_section_gap(logger, "Shipping Address Two :- Label")
    obj_shipping_address_two.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Shipping Address Two :- Placeholder")
    obj_shipping_address_two.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Shipping Address Two :- Default Value")
    obj_shipping_address_two.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Shipping Address Two :- Field Class")
    obj_shipping_address_two.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Shipping Address Two :- Enable Field")
    obj_shipping_address_two.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Shipping Address Two :- Edit field")
    obj_shipping_address_two.test_edit_field(logger)

    obj_base_test.log_section_gap(logger, "Shipping Address Two :- Required")
    obj_shipping_address_two.test_required(logger)
    ShippingAddressTwo.tearDownClass()
    chime.success()

    """ Shipping city"""
    ShippingCity.setUpClass()
    obj_shipping_city = ShippingCity()
    obj_shipping_city.test_preparation()

    obj_base_test.log_section_gap(logger, "Shipping city :- Label")
    obj_shipping_city.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Shipping city :- Placeholder")
    obj_shipping_city.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Shipping city :- Default Value")
    obj_shipping_city.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Shipping city :- Field Class")
    obj_shipping_city.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Shipping city :- Enable Field")
    obj_shipping_city.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Shipping city :- Edit field")
    obj_shipping_city.test_edit_field(logger)

    obj_base_test.log_section_gap(logger, "Shipping city :- Required")
    obj_shipping_city.test_required(logger)

    ShippingCity.tearDownClass()
    chime.success()

    """Shipping State"""
    ShippingState.setUpClass()
    obj_shipping_state = ShippingState()
    obj_shipping_state.test_preparation()
    obj_base_test.log_section_gap(logger, "Shipping State :- Label")
    obj_shipping_state.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Shipping State :- Placeholder")
    obj_shipping_state.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Shipping State :- Default Value")
    obj_shipping_state.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Shipping State :- Enable Field")
    obj_shipping_state.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Shipping State :- Field Class")
    obj_shipping_state.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Shipping State :- Edit field")
    obj_shipping_state.test_edit_field(logger)

    obj_base_test.log_section_gap(logger, "Shipping State :- State Validation")
    obj_shipping_state.test_state_validation(logger)

    obj_base_test.log_section_gap(logger, "Shipping State :- Required")
    obj_shipping_state.test_required(logger)
    ShippingState.tearDownClass()
    chime.success()

    """ Shipping Post code"""
    ShippingPostCode.setUpClass()
    obj_shipping_post_code = ShippingPostCode()
    obj_shipping_post_code.test_preparation()
    obj_base_test.log_section_gap(logger, "Shipping Post code :- Label")
    obj_shipping_post_code.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Shipping Post code :- Placeholder")
    obj_shipping_post_code.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Shipping Post code :- Default Value")
    obj_shipping_post_code.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Shipping Post code :- Field Class")
    obj_shipping_post_code.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Shipping Post code :- Enable Field")
    obj_shipping_post_code.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Shipping Post code :- Edit field")
    obj_shipping_post_code.test_edit_field(logger)

    obj_base_test.log_section_gap(logger, "Shipping Post code :- Post code Validation")
    obj_shipping_post_code.test_post_code_validation(logger)

    obj_base_test.log_section_gap(logger, "Shipping Post code :- Number Validation")
    obj_shipping_post_code.test_number_validation(logger)

    obj_base_test.log_section_gap(logger, "Shipping Post code :- Required")
    obj_shipping_post_code.test_required(logger)
    ShippingPostCode.tearDownClass()
    chime.success()

    """ Additional Fields Order Comments """
    OrderComments.setUpClass()
    obj_order_comments = OrderComments()
    obj_order_comments.test_preparation()
    obj_base_test.log_section_gap(logger, "Additional Fields Order Comments :- Label")
    obj_order_comments.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Additional Fields Order Comments :- Placeholder")
    obj_order_comments.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Additional Fields Order Comments :- Default Value")
    obj_order_comments.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Additional Fields Order Comments :- Field Class")
    obj_order_comments.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Additional Fields Order Comments :- Enable Field")
    obj_order_comments.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Additional Fields Order Comments :- Edit field")
    obj_order_comments.test_edit_field(logger)

    obj_base_test.log_section_gap(logger, "Additional Fields Order Comments :- Email Validation")
    obj_order_comments.test_email_validation(logger)

    obj_base_test.log_section_gap(logger, "Additional Fields Order Comments :- Phone Validation")
    obj_order_comments.test_phone_validation(logger)

    obj_base_test.log_section_gap(logger, "Additional Fields Order Comments :- Number Validation")
    obj_order_comments.test_number_validation(logger)

    obj_base_test.log_section_gap(logger, "Additional Fields Order Comments :- Required")
    obj_order_comments.test_required(logger)
    OrderComments.tearDownClass()
    chime.success()

    """ Billing Custom Text Field """
    BillingCustomText.setUpClass()
    obj_custom_text = BillingCustomText()
    obj_custom_text.test_preparation()
    obj_base_test.log_section_gap(logger, "Billing Custom Text Field :- Name")
    obj_custom_text.test_field_name(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Text Field :- Label")
    obj_custom_text.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Text Field :- Placeholder")
    obj_custom_text.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Text Field :- Default Value")
    obj_custom_text.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Text Field :- Field Class")
    obj_custom_text.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Text Field :- Enable Field")
    obj_custom_text.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Text Field :- Create field")
    obj_custom_text.test_create_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Text Field :- Email Validation")
    obj_custom_text.test_email_validation(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Text Field :- Phone Validation")
    obj_custom_text.test_phone_validation(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Text Field :- Postcode Validation")
    obj_custom_text.test_post_code_validation(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Text Field :- Number Validation")
    obj_custom_text.test_number_validation(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Text Field :- State Validation")
    obj_custom_text.test_state_validation(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Text Field :- Display Order")
    obj_custom_text.test_display_order(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Text Field :- Required")
    obj_custom_text.test_required(logger)
    BillingCustomText.tearDownClass()
    chime.success()

    """ Custom Password Field """
    BillingCustomPassword.setUpClass()
    obj_custom_password = BillingCustomPassword()
    obj_custom_password.test_preparation()
    obj_base_test.log_section_gap(logger, "Billing Custom Password Field :- Name")
    obj_custom_password.test_field_name(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Password Field :- Label")
    obj_custom_password.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Password Field :- Placeholder")
    obj_custom_password.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Password Field :- Field Class")
    obj_custom_password.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Password Field :- Enable Field")
    obj_custom_password.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Password Field :- Create field")
    obj_custom_password.test_create_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Password Field :- Number Validation")
    obj_custom_password.test_number_validation(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Password Field :- Display Order")
    obj_custom_password.test_display_order(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Password Field :- Required")
    obj_custom_password.test_required(logger)
    BillingCustomPassword.tearDownClass()
    chime.success()

    """ Custom Email field"""
    BillingCustomEmail.setUpClass()
    obj_custom_email = BillingCustomEmail()
    obj_custom_email.test_preparation()
    obj_base_test.log_section_gap(logger, "Billing Custom Email Field :- Name")
    obj_custom_email.test_field_name(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Email Field :- Label")
    obj_custom_email.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Email Field :- Placeholder")
    obj_custom_email.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Email Field :- Default Value")
    obj_custom_email.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Email Field :- Field Class")
    obj_custom_email.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Email Field :- Enable Field")
    obj_custom_email.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Email Field :- Create field")
    obj_custom_email.test_create_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Email Field :- Display Order")
    obj_custom_email.test_display_order(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Email Field :- Email Validation")
    obj_custom_email.test_email_validation(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Email Field :- Required")
    obj_custom_email.test_required(logger)
    BillingCustomEmail.tearDownClass()
    chime.success()

    """ Custom Phone Field"""
    BillingCustomPhone.setUpClass()
    obj_billing_custom_phone = BillingCustomPhone()
    obj_billing_custom_phone.test_preparation()
    obj_base_test.log_section_gap(logger, "Billing Custom Phone Field :- Label")
    obj_billing_custom_phone.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Phone Field :- Placeholder")
    obj_billing_custom_phone.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Phone Field :- Default Value")
    obj_billing_custom_phone.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Phone Field :- Field Class")
    obj_billing_custom_phone.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Phone Field :- Enable Field")
    obj_billing_custom_phone.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Phone Field :- Name")
    obj_billing_custom_phone.test_field_name(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Phone Field :- Create field")
    obj_billing_custom_phone.test_create_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Phone Field :- Number Validation")
    obj_billing_custom_phone.test_number_validation(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Phone Field :- Phone Validation")
    obj_billing_custom_phone.test_phone_validation(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Phone Field :- Display Order")
    obj_billing_custom_phone.test_display_order(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Phone Field :- Required")
    obj_billing_custom_phone.test_required(logger)
    BillingCustomPhone.tearDownClass()
    chime.success()

    """ Custom Textarea Field"""
    BillingCustomTextarea.setUpClass()
    obj_custom_textarea = BillingCustomTextarea()
    obj_custom_textarea.test_preparation()
    obj_base_test.log_section_gap(logger, "Billing Custom Textarea Field :- Label")
    obj_custom_textarea.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Textarea Field :- Placeholder")
    obj_custom_textarea.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Textarea Field :- Default Value")
    obj_custom_textarea.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Textarea Field :- Field Class")
    obj_custom_textarea.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Textarea Field :- Enable Field")
    obj_custom_textarea.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Textarea Field :- Name")
    obj_custom_textarea.test_field_name(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Textarea Field :- Create field")
    obj_custom_textarea.test_create_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Textarea Field :- Display Order")
    obj_custom_textarea.test_display_order(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Textarea Field :- Required")
    obj_custom_textarea.test_required(logger)
    BillingCustomTextarea.tearDownClass()
    chime.success()

    """ Custom Select Field """
    BillingCustomSelect.setUpClass()
    obj_custom_select = BillingCustomSelect()
    obj_custom_select.test_preparation()
    obj_base_test.log_section_gap(logger, "Billing Custom Select Field :- Label")
    obj_custom_select.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Select Field :- Placeholder")
    obj_custom_select.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Select Field :- Default Value")
    obj_custom_select.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Select Field :- Field Class")
    obj_custom_select.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Select Field :- Enable Field")
    obj_custom_select.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Select Field :- Name")
    obj_custom_select.test_field_name(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Select Field :- Create field")
    obj_custom_select.test_create_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Select Field :- Display Order")
    obj_custom_select.test_display_order(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Select Field :- Required")
    obj_custom_select.test_required(logger)
    BillingCustomSelect.tearDownClass()
    chime.success()

    """ Custom Radio Field """
    BillingCustomRadio.setUpClass()
    obj_custom_radio = BillingCustomRadio()
    obj_custom_radio.test_preparation()

    obj_base_test.log_section_gap(logger, "Billing Custom Radio Field :- Name")
    obj_custom_radio.test_field_name(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Radio Field :- Label")
    obj_custom_radio.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Radio Field :- Default Value")
    obj_custom_radio.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Radio Field :- Field Class")
    obj_custom_radio.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Radio Field :- Enable Field")
    obj_custom_radio.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Radio Field :- Create field")
    obj_custom_radio.test_create_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Radio Field :- Display Order")
    obj_custom_radio.test_display_order(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Radio Field :- Required")
    obj_custom_radio.test_required(logger)
    BillingCustomRadio.tearDownClass()
    chime.success()

    """ Custom Hidden Field """
    BillingCustomHidden.setUpClass()
    obj_custom_hidden = BillingCustomHidden()
    obj_custom_hidden.test_preparation()
    obj_base_test.log_section_gap(logger, "Billing Custom Hidden Field :- Name")
    obj_custom_hidden.test_field_name(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Hidden Field :- Label")
    obj_custom_hidden.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Hidden Field :- Field Class")
    obj_custom_hidden.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Hidden Field :- Enable Field")
    obj_custom_hidden.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Hidden Field :- Default Value")
    obj_custom_hidden.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Hidden Field :- Create field")
    obj_custom_hidden.test_create_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Hidden Field :- Display Order")
    obj_custom_hidden.test_display_order(logger)
    BillingCustomHidden.tearDownClass()
    chime.success()

    """ Custom Multiselect Field """
    BillingCustomMultiselect.setUpClass()
    obj_custom_multiselect = BillingCustomMultiselect()
    obj_custom_multiselect.test_preparation()
    obj_base_test.log_section_gap(logger, "Billing Custom Multiselect Field :- Name")
    obj_custom_multiselect.test_field_name(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Multiselect Field :- Label")
    obj_custom_multiselect.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Multiselect Field :- Placeholder")
    obj_custom_multiselect.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Multiselect Field :- Default Value")
    obj_custom_multiselect.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Multiselect Field :- Field Class")
    obj_custom_multiselect.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Multiselect Field :- Enable Field")
    obj_custom_multiselect.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Multiselect Field :- Create field")
    obj_custom_multiselect.test_create_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Multiselect Field :- Display Order")
    obj_custom_multiselect.test_display_order(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Multiselect Field :- Required")
    obj_custom_multiselect.test_required(logger)
    BillingCustomMultiselect.tearDownClass()
    chime.success()

    """ Custom Number Field """
    BillingCustomNumber.setUpClass()
    obj_custom_number = BillingCustomNumber()
    obj_custom_number.test_preparation()
    obj_base_test.log_section_gap(logger, "Billing Custom Number Field :- Name")
    obj_custom_number.test_field_name(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Number Field :- Label")
    obj_custom_number.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Number Field :- Placeholder")
    obj_custom_number.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Number Field :- Default Value")
    obj_custom_number.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Number Field :- Field Class")
    obj_custom_number.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Number Field :- Enable Field")
    obj_custom_number.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Number Field :- Create field")
    obj_custom_number.test_create_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Number Field :- Required")
    obj_custom_number.test_required(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Number Field :- Display Order")
    obj_custom_number.test_display_order(logger)
    BillingCustomNumber.tearDownClass()
    chime.success()

    """ Custom Checkbox Field """
    BillingCustomCheckbox.setUpClass()
    obj_custom_checkbox = BillingCustomCheckbox()
    obj_custom_checkbox.test_preparation()
    obj_base_test.log_section_gap(logger, "Billing Custom Checkbox Field :- Name")
    obj_custom_checkbox.test_field_name(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Checkbox Field :- Label")
    obj_custom_checkbox.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Checkbox Field :- Field Class")
    obj_custom_checkbox.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Checkbox Field :- Enable Field")
    obj_custom_checkbox.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Checkbox Field :- Create field")
    obj_custom_checkbox.test_create_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Checkbox Field :- Required")
    obj_custom_checkbox.test_required(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Checkbox Field :- Display Order")
    obj_custom_checkbox.test_display_order(logger)
    BillingCustomCheckbox.tearDownClass()
    chime.success()

    """ Billing Custom CheckboxGroup """
    BillingCustomCheckboxGroup.setUpClass()
    obj_custom_checkbox_group = BillingCustomCheckboxGroup()
    obj_custom_checkbox_group.test_preparation()
    obj_base_test.log_section_gap(logger, "Billing Custom CheckboxGroup Field :- Name")
    obj_custom_checkbox_group.test_field_name(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom CheckboxGroup Field :- Label")
    obj_custom_checkbox_group.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom CheckboxGroup Field :- Default Value")
    obj_custom_checkbox_group.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom CheckboxGroup Field :- Field Class")
    obj_custom_checkbox_group.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom CheckboxGroup Field :- Enable Field")
    obj_custom_checkbox_group.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom CheckboxGroup Field :- Create field")
    obj_custom_checkbox_group.test_create_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom CheckboxGroup Field :- Display Order")
    obj_custom_checkbox_group.test_display_order(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom CheckboxGroup Field :- Required")
    obj_custom_checkbox_group.test_required(logger)
    BillingCustomCheckboxGroup.tearDownClass()
    chime.success()

    """Billing Heading"""
    BillingCustomHeading.setUpClass()
    obj_custom_heading = BillingCustomHeading()
    obj_custom_heading.test_preparation()
    obj_base_test.log_section_gap(logger, "Billing Custom Heading Field :- Name")
    obj_custom_heading.test_field_name(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Heading Field :- Label")
    obj_custom_heading.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Heading Field :- Field Class")
    obj_custom_heading.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Heading Field :- Enable Field")
    obj_custom_heading.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Billing Custom Heading Field :- Create field")
    obj_custom_heading.test_create_field(logger)
    BillingCustomHeading.tearDownClass()
    chime.success()

    """ Custom DateTime Local"""
    CustomDateTimeLocal.setUpClass()
    obj_date_time_local = CustomDateTimeLocal()
    obj_date_time_local.test_preparation()

    obj_base_test.log_section_gap(logger, "Custom Date Time Local :- Name")
    obj_date_time_local.test_field_name(logger)

    obj_base_test.log_section_gap(logger, "Custom Date Time Local :- Label")
    obj_date_time_local.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Custom Date Time Local :- Default Value")
    obj_date_time_local.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Custom Date Time Local :- Field Class")
    obj_date_time_local.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Custom Date Time Local :- Enable Field")
    obj_date_time_local.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Custom Date Time Local :- Create field")
    obj_date_time_local.test_create_field(logger)

    obj_base_test.log_section_gap(logger, "Custom Date Time Local :- Required")
    obj_date_time_local.test_required(logger)

    obj_base_test.log_section_gap(logger, "Custom Date Time Local :- Display Order")
    obj_date_time_local.test_display_order(logger)
    #
    CustomDateTimeLocal.tearDownClass()
    chime.success()

    """ Custom Date """
    CustomDate.setUpClass()
    obj_date = CustomDate()
    obj_date.test_preparation()

    obj_base_test.log_section_gap(logger, "Custom Date :- Name")
    obj_date.test_field_name(logger)

    obj_base_test.log_section_gap(logger, "Custom Date :- Label")
    obj_date.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Custom Date :- Default Value")
    obj_date.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Custom Date :- Field Class")
    obj_date.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Custom Date :- Enable Field")
    obj_date.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Custom Date :- Create field")
    obj_date.test_create_field(logger)

    obj_base_test.log_section_gap(logger, "Custom Date :- Required")
    obj_date.test_required(logger)

    obj_base_test.log_section_gap(logger, "Custom Date :- Display Order")
    obj_date.test_display_order(logger)

    CustomDate.tearDownClass()
    chime.success()

    """ Custom Month """
    CustomMonth.setUpClass()
    obj_month = CustomMonth()
    obj_month.test_preparation()

    obj_base_test.log_section_gap(logger, "Custom Month :- Name")
    obj_month.test_field_name(logger)

    obj_base_test.log_section_gap(logger, "Custom Month :- Label")
    obj_month.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Custom Month :- Default Value")
    obj_month.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Custom Month :- Field Class")
    obj_month.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Custom Month :- Enable Field")
    obj_month.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Custom Month :- Create field")
    obj_month.test_create_field(logger)

    obj_base_test.log_section_gap(logger, "Custom Month :- Required")
    obj_month.test_required(logger)

    obj_base_test.log_section_gap(logger, "Custom Month :- Display Order")
    obj_month.test_display_order(logger)

    CustomMonth.tearDownClass()
    chime.success()

    """ Custom Time """
    CustomTime.setUpClass()
    obj_time = CustomTime()
    obj_time.test_preparation()

    obj_base_test.log_section_gap(logger, "Custom Time :- Name")
    obj_time.test_field_name(logger)

    obj_base_test.log_section_gap(logger, "Custom Time :- Label")
    obj_time.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Custom Time :- Default Value")
    obj_time.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Custom Time :- Field Class")
    obj_time.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Custom Time :- Enable Field")
    obj_time.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Custom Time :- Create field")
    obj_time.test_create_field(logger)

    obj_base_test.log_section_gap(logger, "Custom Time :- Required")
    obj_time.test_required(logger)

    obj_base_test.log_section_gap(logger, "Custom Time :- Display Order")
    obj_time.test_display_order(logger)

    CustomTime.tearDownClass()
    chime.success()

    """ Custom Week """
    CustomWeek.setUpClass()
    obj_week = CustomWeek()
    obj_week.test_preparation()

    obj_base_test.log_section_gap(logger, "Custom Week :- Name")
    obj_week.test_field_name(logger)

    obj_base_test.log_section_gap(logger, "Custom Week :- Label")
    obj_week.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Custom Week :- Default Value")
    obj_week.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Custom Week :- Field Class")
    obj_week.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Custom Week :- Enable Field")
    obj_week.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Custom Week :- Create field")
    obj_week.test_create_field(logger)

    obj_base_test.log_section_gap(logger, "Custom Week :- Required")
    obj_week.test_required(logger)
    #
    obj_base_test.log_section_gap(logger, "Custom Week :- Display Order")
    obj_week.test_display_order(logger)

    CustomWeek.tearDownClass()
    chime.success()

    """ Custom URl """
    CustomUrl.setUpClass()
    obj_url = CustomUrl()
    obj_url.test_preparation()

    obj_base_test.log_section_gap(logger, "Custom URl :- Name")
    obj_url.test_field_name(logger)

    obj_base_test.log_section_gap(logger, "Custom URl :- Label")
    obj_url.test_field_label(logger)

    obj_base_test.log_section_gap(logger, "Custom URl :- Placeholder")
    obj_url.test_field_placeholder(logger)

    obj_base_test.log_section_gap(logger, "Custom URl :- Default Value")
    obj_url.test_field_default_value(logger)

    obj_base_test.log_section_gap(logger, "Custom URl :- Field Class")
    obj_url.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Custom URl :- Enable Field")
    obj_url.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Custom URl :- Create field")
    obj_url.test_create_field(logger)

    obj_base_test.log_section_gap(logger, "Custom URl :- Required")
    obj_url.test_required(logger)

    obj_base_test.log_section_gap(logger, "Custom URl :- Display Order")
    obj_url.test_display_order(logger)

    CustomUrl.tearDownClass()
    chime.success()

    """ Custom Paragragh """
    CustomParagraph.setUpClass()
    obj_paragraph = CustomParagraph()
    obj_paragraph.test_preparation()

    obj_base_test.log_section_gap(logger, "Custom Paragragh :- Name")
    obj_paragraph.test_field_name(logger)

    obj_base_test.log_section_gap(logger, "Custom Paragragh :- Field Content")
    obj_paragraph.test_field_content(logger)

    obj_base_test.log_section_gap(logger, "Custom Paragragh :- Field Class")
    obj_paragraph.test_field_class(logger)

    obj_base_test.log_section_gap(logger, "Custom Paragragh :- Enable Field")
    obj_paragraph.test_enable_field(logger)

    obj_base_test.log_section_gap(logger, "Custom Paragragh :- Create field")
    obj_paragraph.test_create_field(logger)

    CustomParagraph.tearDownClass()
    chime.success()

    """ Billling Override """
    AdvancedBillingOverride.setUpClass()
    obj_billing_override = AdvancedBillingOverride()
    obj_billing_override.test_preparation()
    obj_base_test.log_section_gap(logger, "Billing Override :- Label Override")
    obj_billing_override.test_label_override(logger)

    obj_base_test.log_section_gap(logger, "Billing Override :- Class Override")
    obj_billing_override.test_class_override(logger)

    obj_base_test.log_section_gap(logger, "Billing Override :- Placeholder override")
    obj_billing_override.test_placeholder_override(logger)

    obj_base_test.log_section_gap(logger, "Billing Override :- Required Override")
    obj_billing_override.test_required_override(logger)
    AdvancedBillingOverride.tearDownClass()
    chime.success()


    """For closing the created testrail"""
    CloseTestRun.setUpClass()
    obj_close_test_run = CloseTestRun(run_id)
    obj_close_test_run.add_results_testrail()
    obj_close_test_run.test_close_test_run()
    CloseTestRun.tearDownClass()
############################################################################################
# except KeyboardInterrupt:
    # print("Keyexcept")
    # chime.warning()
    # CloseTestRun.setUpClass()
    # obj_close_test_run = CloseTestRun(run_id)
    # obj_close_test_run.add_results_testrail()
    # CloseTestRun.tearDownClass()
except Exception as e:
    # print("except")
    traceback.print_exc()
    # chime.warning()
    # CloseTestRun.setUpClass()
    # obj_close_test_run = CloseTestRun(run_id)
    # obj_close_test_run.add_results_testrail()
    # CloseTestRun.tearDownClass()
