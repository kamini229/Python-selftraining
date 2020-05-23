from selenium import webdriver

class FindByLinkText():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        elementByLink = driver.find_element_by_link_text("Login")

        if elementByLink is not None:
            print("We found an element by Link Text")

        elementByartialLinkText = driver.find_element_by_partial_link_text("Pract")

        if elementByartialLinkText is not None:
            print("We found an element by partial link text")

ff = FindByLinkText()
ff.test()