import time
import unittest

from selenium import webdriver


class BasePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/All_Driver/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get("https://www.daraz.com.bd/")
        print("Test Started")

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()
        print("Test Complete")
