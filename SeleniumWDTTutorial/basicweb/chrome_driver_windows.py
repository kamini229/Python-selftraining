from selenium import webdriver
import os

class ChromeDriverWindows():

    def test(self):
        driverLocation = "C:/Users/Kamini/workspace_python/drivers/chromedriver.exe"
        os.environ["webdriver.chromw.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get("http://www.letskodeit.com")

cc = ChromeDriverWindows()
cc.test()