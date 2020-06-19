from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("D:\selenium\driver\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()
driver.implicitly_wait(10)
inputboxes = driver.find_elements_by_class_name("text_field")
print(len(inputboxes))
status = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(status)
driver.find_element_by_id("RESULT_RadioButton-7_1")
s1 = driver.find_element_by_id("RESULT_RadioButton-7_1").is_selected()
print(s1)
driver.find_element_by_id("RESULT_CheckBox-8_0").click()
status1 = driver.find_element_by_id("RESULT_CheckBox-8_0").is_selected()
print(status1)
driver.quit()
