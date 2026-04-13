import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get('https://the-internet.herokuapp.com/status_codes')

el = browser.find_elements("xpath", "//li")

for i in el:
    element = i
    element.click()
    time.sleep(2)
    browser.back()
