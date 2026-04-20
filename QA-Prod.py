from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
prefs = {
        "download.default_directory": os.path.join(os.getcwd(), "downloads")
}

chrome_options.add_experimental_option("prefs", prefs)
service = Service(executable_path=ChromeDriverManager().install())
driver: WebDriver = webdriver.Chrome(options=chrome_options, service=service)
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10, poll_frequency=1)

wait.until(EC.visibility_of_element_located())


try:

    driver.get("https://the-internet.herokuapp.com/download")
    files = driver.find_elements(By.XPATH, "//div[@class='example']/a")
    for i in files:
        i.click()

finally:
    driver.quit()

print(files)