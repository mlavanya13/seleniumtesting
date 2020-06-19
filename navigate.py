import time

from selenium import webdriver

driver = webdriver.Chrome("D:\selenium\driver\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
print(driver.title)
time.sleep(5)
driver.get("http://www.pavantestingtools.com/")

print(driver.title)
time.sleep(5)
driver.back()
print(driver.title)
time.sleep(5)
driver.forward()
print(driver.title)
driver.quit()