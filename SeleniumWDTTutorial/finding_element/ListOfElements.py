from selenium import webdriver
from selenium.webdriver.common.by import By

class ListofElements():
    baseUrl = "https://letskodeit.teachable.com/pages/practice"
    driver = webdriver.Firefox()
    driver.get(baseUrl)

    elementListByClassName = driver.find_elements_by_class_name("inputs")
    length1 = len(elementListByClassName)

    if elementListByClassName is not None:
        print("Size of the list is " + str(length1))

    elementListNyTagName = driver.find_elements(By.TAG_NAME, "h1")
    length2 = len(elementListNyTagName)

    if elementListNyTagName is not None:
        print("Size of the list is " + str(length2))

    elementListNyTagName = driver.find_elements(By.TAG_NAME, "td")
    length3 = len(elementListNyTagName)

    if elementListNyTagName is not None:
        print("Size of the list is " + str(length3))