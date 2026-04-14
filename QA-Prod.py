from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os

# 1. Настройка опций
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1280,800")

# 2. Правильная инициализация (ОДИН РАЗ)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

prefs = {
    "downloand.default_directory": f"{os.getcwd()}/downloads" #сменить директория для скачавания
}
options.add_experimental_option()

link = "https://the-internet.herokuapp.com/status_codes"

try:
    # 3. Используем переменную 'driver' вместо 'webdriver'
    driver.get(link)
    # Используем By.XPATH для надежности
    my_elements = driver.find_elements(By.XPATH, "//li/a")

    # Создаем список ссылок, так как после клика и возврата элементы могут "протухнуть" (StaleElementReferenceException)
    hrefs = [elem.get_attribute("href") for elem in my_elements]

    for href in hrefs:
        driver.get(href)
        sleep(1) # Пауза, чтобы рассмотреть страницу
        driver.back()

finally:
    # 4. Закрываем браузер
    driver.quit()