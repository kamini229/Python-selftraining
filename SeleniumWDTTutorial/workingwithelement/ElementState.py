from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class ElementState():

    def isEnabled(self):
        baseUrl ="https://www.google.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(20)

        e1 = driver.find_element(By.NAME, "q")
        e1State = e1.is_enabled()
        print("E1 is enabled? "+str(e1State))
        e1.send_keys("letskodeit")

e = ElementState()
e.isEnabled()