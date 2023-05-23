=== WCFE-FREE Automation ===

How to run?

After cloning the project from bit-bucket;
-> Open the project folder in terminal.
-> Create the virtual environment using commands : 'python3 -m venv env' (if didn't worked use, py -m venv env, python -m venv env).
  * This will create the env directory if it doesn’t exist,
    and also create directories inside it containing a copy of the Python interpreter and various supporting files.
  * This step is only needed for running the project for the first time.
-> Then activate it by : 'source env/bin/activate' (in mac os), 'env\Scripts\activate.bat' (in windows), '. env/bin/activate' (in linux).
-> Then Install the packages in requirement.txt, using command : 'pip install -r requirements.txt'.
  * requirements.txt contains the list of all packages which are needed for running the automation.
  * The above command will install all the packages in the virtual environment created in the previous step.
-> create .env file and save the datas by referring env_sample.txt in project folder.
-> Run the main file using the command : 'python3 main.py'(if not worked use, py main.py, python main.py).

=== .env File Description ===

WEP_LOGIN_URL               : Url to the plugin product options tab in the plugin installed site.
WEP_USERNAME                : Username to the site
WEP_PASSWORD                : Password to the site
WEP_PRODUCT_PAGE_URL        : Url to the any simple product page
WEP_CART_PAGE_URL           : Url to the cart page
WEP_CHECKOUT_PAGE_URL       : Url to the checkout page
WEP_MY_ACCOUNT_ORDERS_URL   : Url to the myaccount orders page
WEP_WOOCOMMERCE_ORDERS_URL  : Url to the admin orders page
WEP_TESTRAIL_URL            : Url to the testrail.
WEP_CLIENT_USER             : Username to the testrail.
WEP_CLIENT_PASS             : Password to the testrail.
WEP_MY_ACCOUNT              : Url to the myaccount orders page
WEP_ADVANCED_SETTINGS_URL   : Url to advanced settings tab page
WEP_SHOP_PAGE_URL           : Url to shop page
TESTING_SITE                : Site url
EDIT_ADDRESS_BILLING        : Url to edit billing address
EDIT_ADDRESS_SHIPPING       : Url to edit shipping address


NOTE:
-> Live site or local can be used for automation testing.
-> Disable terms and conditions in checkout page.
-> Plugin must be installed
-> If you want to run the code in non headless mode, ie, view the automation process
    * Comment the code in each file in test folder :-
        # cls.driver = webdriver.Chrome(ChromeDriverManager().install())
    * And uncomment the code in each file :-
        options.add_argument('--headless')
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

-> Ensure that the plugin is installed, before starting testing.

ABOUT:
-> Here we have used POM model.
-> Every call to each test is done from main file.
-> Every file in tests folder contains code for each section in testrail, ie, each functions.
-> It contains call to the functions in pages folder.
-> The files in pages folder contains actions in every pages like checkout, cart etc.
-> We used sqlitedict to store data from testrail and results after testing :- in case, the automation is broken,
    immediately call function in close testrun -> add_results_testrail(), ie, it saves result data in testrail
    and continue or can be continue automation by changing some codes:
    comment below lines:
          """For creating new Test run in testrail """
          CreateTestRun.setUpClass()
          obj_create_test_run = CreateTestRun()
          run_id = obj_create_test_run.test_add_test_run()
          CreateTestRun.tearDownClass()
          ----------------------------------
          obj_base_test.store_section_data()

          obj_base_test.delete_result()
          ----------------------------------
          run_id = # Current run id
          
-> Prerequisites of the site:
  - Terms and conditions option from woocommerce must be avoided.
  - Must ship to all locations.
  - Shipping zone must be added eg:- Free Shipping.
