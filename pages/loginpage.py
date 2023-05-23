import time
from selenium.webdriver.common.by import By
from locators.locators import Locators
from pages.basepage import BasePage
import os
from dotenv import load_dotenv

load_dotenv()


class LoginWordPress:
    """Login wordpress"""
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.submit_button_id = Locators.submit_button_id

    def login_wordpress_dashboard(self, username, password):
        while True:
            current_url = self.driver.current_url
            if current_url == os.environ.get('WCFEF_LOGIN_URL'):
                break
            else:
                # time.sleep(.5)
                obj_base_page = BasePage(self.driver)
                obj_base_page.wait_page_load()
                # time.sleep(.5)
                obj_base_page.send_keys_id(self.username_textbox_id, username)
                # time.sleep(.5)
                obj_base_page.wait_page_load()
                obj_base_page.send_keys_id(self.password_textbox_id, password)
                # time.sleep(.5)
                obj_base_page.wait_page_load()
                obj_base_page.click_button_id(self.submit_button_id)
                obj_base_page.wait_page_load()
                time.sleep(1)



        # self.driver.find_element(By.ID, self.username_textbox_id).clear()
        # self.driver.find_element(By.ID, self.username_textbox_id).send_keys(username)
        # time.sleep(.5)
        # self.driver.find_element(By.ID, self.password_textbox_id).clear()
        # self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)
        # time.sleep(.5)
        # self.driver.find_element(By.ID, self.submit_button_id).click()
