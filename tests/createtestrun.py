import unittest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.testrailpage import TestRailPage
from datetime import datetime
import os
import sys
sys.path.append('/Users/zennode/PycharmProjects/WCFE-Free-new')

class CreateTestRun(unittest.TestCase):
    # run_id = 0

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument('--headless')
        cls.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        cls.driver.set_page_load_timeout(100)

    def test_add_test_run(self):
        driver = self.driver
        create_testrail_test_run = TestRailPage()
        now = datetime.now()
        current_date_time = now.strftime("%d/%m/%Y %H: %M: %S")
        url = os.environ.get('WCFEF_LOGIN_URL')
        n = 3
        groups = url.split('/')
        run_id = create_testrail_test_run.create_testrail_test_run(13, current_date_time + "-" + '/'.join(groups[:n]))
        # CreateTestRun.run_id = create_testrail_test_run.create_testrail_test_run(13, "Text-Advanced test")
        return run_id

    @classmethod
    def tearDownClass(cls):
        print("Testrail")
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
