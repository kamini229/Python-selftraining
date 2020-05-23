from selenium import webdriver
from time import sleep

def test_documentation_link():
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/")
    sleep(4)
    driver.find_element_by_link_text("Downloads").click()

    sleep(4)
    documentation = driver.find_element_by_link_text("documentation")
    documentation.click()

test_documentation_link()