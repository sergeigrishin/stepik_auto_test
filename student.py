from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

chrome_options = webdriver.Chrome_Options()
prefs = {
        "download.default_directory": os.path.join(os.getcwd(), "downloads")
}

chrome_options.add_experimental_option("prefs", prefs)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=chrome_options, service=service)

try:
    driver.get("https://demoqa.com/upload-download")

finally:
    driver.quit()
