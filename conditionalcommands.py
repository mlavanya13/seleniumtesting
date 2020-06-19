from selenium import webdriver
driver = webdriver.Chrome("D:\selenium\driver\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
user_ele = driver.find_element_by_name("userName")
print(user_ele.is_displayed())
print(user_ele.is_enabled())
pwd_ele = driver.find_element_by_name("userName")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())

user_ele.send_keys("mercury")
pwd_ele.send_keys("mercury")
driver.find_element_by_name("login").click()

driver.quit()