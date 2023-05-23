from selenium.webdriver.common.by import By

class ShopPage:
    """ All the actions done in shop page is done here"""

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_url):
        element = self.driver.find_element(By.XPATH, product_url)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        
