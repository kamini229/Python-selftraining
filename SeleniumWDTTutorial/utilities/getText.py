from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class getText():

    def test(self):
        baseUrl ="https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        openTabElement = driver.find_element(By.ID, "opentab")
        elementText = openTabElement.text
        print("Text on element is: " + elementText)
        time.sleep(1)
        driver.quit()

ff = getText()
ff.test()
