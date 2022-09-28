import time
from selenium import webdriver

driver = webdriver.Firefox(executable_path = './geckodriver')
driver.get("http://www.baidu.com")


time.sleep(5)
driver.quit()