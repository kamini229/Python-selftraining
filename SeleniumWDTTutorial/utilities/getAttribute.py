from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class getAttribute():

    def test(self):
        baseUrl ="https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        element = driver.find_element_by_id("name")
        result = element.get_attribute("class")


        print("Text on element is: " + result)
        time.sleep(1)
        driver.quit()

ff = getAttribute()
ff.test()
