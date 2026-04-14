from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link  = "https://the-internet.herokuapp.com/status_codes"
browser.get(link)

my_elements = browser.find_elements("xpath", "//li/a")


for elem in my_elements:
    elem.click()
    sleep(2)
    browser.back()
    sleep(2)
