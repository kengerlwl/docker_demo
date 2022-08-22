from get_driver import *

Driver = Driver()
driver = Driver.get_from_local()

try:

    driver.get('https://www.baidu.com')
    driver.maximize_window()
    driver.find_element_by_id("kw").send_keys("test")
    driver.find_element_by_id("su").click()

    print(driver.page_source)
except Exception as e:
    driver.quit()
    raise e

driver.quit()