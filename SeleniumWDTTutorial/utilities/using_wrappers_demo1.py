from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.handyWrappers import HandyWrapper
import time

class UsingWrappers():

    def test(self):
        baseUrl ="https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrapper(driver)
        driver.get(baseUrl)

        testField1  = hw.getElement("name")
        testField.send_keys("Test")
        time.sleep(2)
        testField2 = hw.getElement("//input[@id='nam]", locatorType="xpath")

ff = UsingWrappers()
ff.test()
