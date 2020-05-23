from selenium import webdriver
from time import sleep

class AutoComplete():

    def test1(self):
        baseUrl = "https://www.southwest.com"
        driver =  webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)


        # send partial data
        cityField = driver.find_element_by_id("LandingAirBookingSearchForm_originationAirportCode")
        cityField.send_keys("New York")
        sleep(3)

        itemToSelect = driver.find_element_by_xpath("//ul[@id='air-city-departure-menu']//li[contains(text(),'NJ - EWR')]")
        itemToSelect.click()

        # Find the item and click


        sleep(3)
        #driver.quit()

ff = AutoComplete()
ff.test1()
