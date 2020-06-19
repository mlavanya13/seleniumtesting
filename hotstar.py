from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

driver = webdriver.Chrome("D:\selenium\driver\chromedriver.exe")
driver.get("https://www.hotstar.com/in")

'''driver.find_element_by_id('searchFeild').send_keys('movies')
driver.find_element_by_name("q").send_keys("selenium")
driver.find_element_by_link_text("premium").click()
driver.find_element_by_css_selector("#searchField").send_keys("sports")
driver.find_element_by_partial_link_text("premium").click()'''
driver.find_element_by_xpath("//div [@class='signIn']").click()
driver.find_element_by_link_text("email-or-fb-signin").click()
driver.find_element_by_name("emailID").send_keys("lavanya.mandalapu@gmail.com")

