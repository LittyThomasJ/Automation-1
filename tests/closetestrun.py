import unittest
from pages.testrailpage import TestRailPage
from tests.createtestrun import CreateTestRun
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import sys
from tests.basetest import *
sys.path.append('/Users/zennode/PycharmProjects/WCFE-Free-new')

class CloseTestRun(CreateTestRun, unittest.TestCase):
    def __init__(self, run_id):
        super().__init__()
        self.run_id = run_id
        # self.run_id = CreateTestRun.run_id

    def test_close_test_run(self):
        # driver = self.driver
        obj_testrail = TestRailPage()
        obj_testrail.close_testrail_test_run(self.run_id)
        print("Test_run closed")

    def add_results_testrail(self):
        obj_testrail = TestRailPage()
        obj_testrail.add_result_for_all(self.run_id)


if __name__ == '__main__':
    unittest.main()
