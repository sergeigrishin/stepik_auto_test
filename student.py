import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": os.path.join(os.getcwd(), "download")
}

chrome_options.add_experemental_options("prefs", prefs)
service = Service(executable_path=ChromeDriverManager().install())
driver: WebDriver = webdriver.Chrome(options= chrome_options, service=service)
wait = WebDriverWait(driver, 10, 1)

driver.get("https://omayo.blogspot.com")

try:


finally:
    driver.quit()
