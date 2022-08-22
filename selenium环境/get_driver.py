from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options



class Driver():
    def __init__(self):
        pass

    def get_from_local(self):
        options = Options()
        options.add_argument('--no-sandbox')

        driver = webdriver.Chrome(chrome_options=options)
        return driver

    def get_from_net(self):
        # 我这里是在云端运行
        driver = webdriver.Remote(
            desired_capabilities=DesiredCapabilities.CHROME,
            command_executor="http://110.40.204.239:54444/wd/hub"
        )

        return driver