import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from selenium import webdriver
import time
import unittest
from sampleprojects.POMprojectDemo.pages.loginpage import LoginPage
from sampleprojects.POMprojectDemo.pages.homepage import HomePage
import HtmlTestRunner




class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("D:\selenium\driver\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    def test_login_valid(self):
        driver = self.driver

        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_Logout()

    def test_login_invalid(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin1")
        login.enter_password("admin123")
        login.click_login()
        msg=driver.find_element_by_xpath(" ").text
        self.assertEqual (msg,"Csrf token validation failed12")



        ''' self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        self.driver.find_element_by_id("welcome").click()
        self.driver.find_element_by_link_text("Logout").click()'''
        time.sleep(2)
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/mchan/PycharmProjects/seleniumtesting/reports"))




'''driver = webdriver.Chrome("D:\selenium\driver\chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
driver.find_element_by_id("welcome").click()
driver.find_element_by_link_text("Logout").click()
time.sleep(2)
driver.close()
driver.quit()
print("Test Completed")'''
