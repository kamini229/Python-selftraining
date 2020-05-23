from selenium import webdriver
import time

class RadioButtonAndCheckbox():

    def test(self):
        baseUrl ="https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        bmwRadiobtn = driver.find_element_by_id("bmwradio")
        bmwRadiobtn.click()

        time.sleep(2)

        benzRadiobtn = driver.find_element_by_id("benzradio")
        benzRadiobtn.click()

        time.sleep(2)

        bmwCheckbox = driver.find_element_by_id("bmwcheck")
        bmwCheckbox.click()

        time.sleep(2)

        print("BMW radio button is selected? :" + str(bmwRadiobtn.is_selected()))
        print("Benz radio button is selected? :" + str(benzRadiobtn.is_selected()))
        print("BMW Checkbox is selected? :" + str(bmwCheckbox.is_selected()))

ff = RadioButtonAndCheckbox()
ff.test()