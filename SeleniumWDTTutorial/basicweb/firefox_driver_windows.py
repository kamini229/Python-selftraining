from selenium import webdriver

class RunFFTests():
    def testMethod(self):
        # Instantiate the FF Browser command
        driver = webdriver.Firefox()
        # Open the provided URL
        driver.get("https://www.letskodeit.com")

ff = RunFFTests()
ff.testMethod()