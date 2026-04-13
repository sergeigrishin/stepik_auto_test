import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

browser = webdriver.Chrome()
browser.get("https://dzen.ru")

br_title = browser.title

print(br_title)


