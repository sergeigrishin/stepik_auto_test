import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import *

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/explicit_wait2.html")

try:
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element(By.ID, "book").click()

    x_element = browser.find_element(By.ID, "input_value")
    x_value = x_element.text  # Здесь должно быть только число, например "24"

    result = str(log(abs(12 * sin(int(x_value)))))

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(result)

    browser.find_element(By.ID, "solve").click()
    time.sleep(10)
for i in range(4):
    print(1)
finally:
    browser.quit()

