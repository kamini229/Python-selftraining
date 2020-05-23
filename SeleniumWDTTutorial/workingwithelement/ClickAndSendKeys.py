from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class ClickAndSendkeys():

    def test(self):
        baseUrl ="https://letskodeit.teachable.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(20)

        driver.find_element(By.XPATH, "//a[@class='navbar-link fedora-navbar-link']").click()

        emailField = driver.find_element(By.ID, "user_email")
        emailField.send_keys("test")

        passwordField = driver.find_element(By.ID, "user_password")
        passwordField.send_keys("test")

        sleep(3)

        emailField.clear()

        sleep(3)

        emailField.send_keys("test")

ff = ClickAndSendkeys()
ff.test()