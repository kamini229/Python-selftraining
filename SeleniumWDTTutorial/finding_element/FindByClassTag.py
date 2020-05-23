from selenium import webdriver

class FindByClassTag():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        elementByClassName = driver.find_element_by_class_name("displayed-class")
        elementByClassName.send_keys("Testing the element")

        if elementByClassName is not None:
            print("We found an element by Class Name")

        elementByTagName = driver.find_element_by_tag_name("h1")
        text = elementByTagName.text

        if elementByTagName is not None:
            print("We found an element by Tag Name and the text name is " + text)

        driver.close()

ff = FindByClassTag()
ff.test()