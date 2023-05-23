class Locators():

    #Login page locators

    username_textbox_id = "user_login"
    password_textbox_id = "user_pass"
    submit_button_id = "wp-submit"


    reset_fields = "//input[@name='reset_fields']"
    save_close_button = "//*[@id='thwcfd_field_form_pp']/div/div/div/div/div/footer/div/button/span"
    edit_label_button = "//table[contains(@class,'thwcfd_field_form_tab_general_placeholder thwcfd_pp_table')]/tbody[1]/tr[1]/td[3]/input[1]"
    placeholder_xpath = "//table[contains(@class,'thwcfd_field_form_tab_general_placeholder thwcfd_pp_table')]/tbody[1]/tr[2]/td[3]/input[1]"
    place_order = "//*[@id=\"place_order\"]"
    default_value_xpath_additional = '//*[@id="thwcfd_field_form"]/div/div/table[2]/tbody/tr[3]/td[3]/textarea'
    default_value_xpath = "(//input[@name='i_default'])[1]"
    field_class_name = 'i_class'
    field_validation_xpath = '//*[@id="thwcfd_field_form"]/div/div/table[2]/tbody/tr[5]/td[3]/select'
    disable_field_xpath = '//*[@id="a_fenabled"]'
    shipping_fields = "Shipping Fields"
    additional_fields_text = "Additional Fields"
    add_field_xpath = '//*[@id="thwcfd_checkout_fields"]/thead/tr[1]/th[1]/button[1]'
    field_type_xpath = "//select[@name='i_type']"
    field_name_xpath = "//input[@name='i_name']"
    display_order_xpath = "(//input[@name='i_show_in_order'])[1]"
    advanced_settings_xpath = "//a[normalize-space()='Advanced Settings']"
    label_override_xpath = '//*[@id="a_fenable_label_override"]'
    class_override_xpath = "//input[@id='a_fenable_class_override']"
    placeholder_override_xpath = "//input[@id='a_fenable_placeholder_override']"
    required_override_xpath = "//input[@id='a_fenable_required_override']"
    priority_override_xpath = "//input[@id='a_fenable_priority_override']"
    reset_advanced_settings = "//input[@name='reset_settings']"
    save_changes_xpath = "//input[@value='Save changes']"
    required_xpath = "(//input[@name='i_required'])[1]"


    add_option_two_xpath = "(//a[@title='Add new option'][normalize-space()='+'])[1]"
    add_option_three_xpath = "(//a[@title='Add new option'][normalize-space()='+'])[2]"
    option_value_one_xpath = "(//input[@placeholder='Option Value'])[1]"
    option_value_two_xpath = "(//input[@placeholder='Option Value'])[2]"
    option_value_three_xpath = "(//input[@placeholder='Option Value'])[3]"
    option_text_one_xpath = "(//input[@placeholder='Option Text'])[1]"
    option_text_two_xpath = "(//input[@placeholder='Option Text'])[2]"
    option_text_three_xpath = "(//input[@placeholder='Option Text'])[3]"

    """ AdminOrderPage """
    billing_order_data_xpath = '//*[@id="order_data"]/div[1]/div[2]/div[1]/p[1]'
    order_data_xpath = '//*[@id="order_data"]/div[1]/div[3]/div[1]/p[1]'
    admin_order_class_name_xpath = "order-view"

    """ Cart page"""
    table_class_name_xpath = "woocommerce-cart-form__contents"
    cart_row_xpath = "cart_item"
    cart_delete_xpath = "//table[contains(@class,'shop_table shop_table_responsive')]/tbody[1]/tr[1]/td[1]/a[1]"

    """ Checkout Form Designer """
    error_msg_noti_xpath = "//div[@class='err_msgs']"
    check_label_xpath = '//*[@id="thwcfd_checkout_fields"]/tbody/tr[12]/td[5]'
    check_placeholder_xpath = '//*[@id="thwcfd_checkout_fields"]/tbody/tr[12]/td[6]'
    check_placeholder_xpath = '//*[@id="thwcfd_checkout_fields"]/tbody/tr[12]/td[6]'
    saved_notification_xpath = "//p[text()='Your changes were saved.']"
    name_required_xpath = "//div[text()='Name is required']"

    """ Checkout page """
    shipping_checkbox = "ship-to-different-address-checkbox"
    label_xpath = "/html[1]/body[1]/div[2]/div[2]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/form[2]/div[1]/div[1]/div[1]/div[1]/p[12]/label[1]"
    placeholder_default_checkbox_xpath = '//*[@id="ship-to-different-address-checkbox"]'
    # place_order = 'place_order'

    """ Myaccount Page """
    logout_xpath = "//li[@class='woocommerce-MyAccount-navigation-link woocommerce-MyAccount-navigation-link--customer-logout']//a[1]"

    """ Thankyou page """
    shipping_address_xpath = "//h2[text()='Shipping address']/following-sibling::address"
    billing_address_xpath = "//h2[text()='Billing address']/following-sibling::address"
