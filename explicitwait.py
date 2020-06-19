from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("D:\selenium\driver\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()
driver.implicitly_wait(10)
try:
    element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(By.ID, "RESULT_RadioButton-7_0"))

finally:
    driver.quit()
wait = WebDriverWait(driver, 10)
element1 = wait.until(EC.element_to_be_clickable((By.ID, 'RESULT_RadioButton-7_0')))
status = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(status)

