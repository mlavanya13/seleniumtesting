from selenium import webdriver

driver = webdriver.Chrome("D:\selenium\driver\chromedriver.exe")
driver.get("https://www.edureka.co")
driver.find_element_by_css_selector("#search-input").send_keys("python")

