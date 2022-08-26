from get_driver import *
import time
Driver = Driver()
driver = Driver.get_from_net()

try:

    driver.get('https://www.google.com')
    driver.maximize_window()
    driver.find_element_by_id("kw").send_keys("test")
    driver.find_element_by_id("su").click()

    print(driver.page_source)


except Exception as e:

    time.sleep(120)
    driver.quit()
    raise e

time.sleep(120)
driver.quit()