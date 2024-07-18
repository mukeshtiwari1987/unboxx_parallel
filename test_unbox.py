import logging
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

LOGGER = logging.getLogger(__name__)
base_url = "https://ssdevconsole-ui.unbxd.io/"
page_title = "Unbxd - Search Dashboard"

class TestExamples(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver  = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def test_demo_netcore(self):
        try:
            driver = self.driver
            driver.get(base_url)
            LOGGER.info("Driver Session ID: " + driver.session_id)
            LOGGER.info("Current URL is: " + driver.current_url)
            email_input = driver.find_element(By.XPATH, "//input[@id='userEmail']")
            email_input.send_keys("ssoregression@yopmail.com")
            password_input = driver.find_element(By.XPATH, "//input[@id='password']")
            password_input.send_keys("password")
            driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
            get_title = driver.title
            assert page_title in get_title
        finally:
            LOGGER.info("Execution finished for Driver Session ID: " + driver.session_id)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
