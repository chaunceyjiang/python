from selenium import webdriver
driver=webdriver.Chrome(r"C:\Python\phantomjs\bin\chromedriver.exe")
driver.get("http://home.51cto.com/index")
driver.find_element_by_id("loginform-username").send_keys("xxxxxx")
driver.find_element_by_id("loginform-password").send_keys("xxxxxx")
driver.find_element_by_name("login-button").click()
driver.get("http://down.51cto.com/credits")
driver.find_element_by_id("jsGetCredit").click()
driver.quit()
