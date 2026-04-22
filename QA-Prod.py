import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# 1. Настройки
chrome_options = webdriver.ChromeOptions()
download_path = os.path.join(os.getcwd(), "download")
if not os.path.exists(download_path):
    os.makedirs(download_path)

prefs = {"download.default_directory": download_path}
chrome_options.add_experimental_option("prefs", prefs)

service = Service(executable_path=ChromeDriverManager().install())
driver: WebDriver = webdriver.Chrome(options=chrome_options, service=service)
wait = WebDriverWait(driver, 30, 1)

try:
    driver.get("https://omayo.blogspot.com")

    # Проверка исчезновения (пройдет сразу, если элемента нет)
    wait.until(EC.invisibility_of_element_located((By.ID, "deletesuccess")))

    # Ждем появления текста
    wait.until(EC.visibility_of_element_located((By.ID, "delayedText")))

    # Ждем кликабельности кнопки и сохраняем её в переменную
    timer_btn_locator = (By.ID, "timerButton")
    timer_button = wait.until(EC.element_to_be_clickable(timer_btn_locator))

    # Кликаем по уже найденному элементу
    timer_button.click()

    # Ждем, пока эта же кнопка станет неактивной
    wait.until_not(EC.element_to_be_clickable(timer_btn_locator))
    print("Тест успешно завершен: кнопка заблокирована.")

except Exception as e:
    print(f"Ошибка в тесте: {e}")

finally:
    driver.quit()