from selenium import webdriver

driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
driver.implicitly_wait(3)

driver.get('https://google.com')
