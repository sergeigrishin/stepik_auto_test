import os
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def create_driver():
    chrome_options = Options()

    # Базовые настройки
    chrome_options.add_argument("--window-size=1280,720")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    # Убираем явное упоминание Selenium в User-Agent
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # Настройка загрузок
    download_path = os.path.join(os.getcwd(), "downloads")
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    prefs = {
        "download.default_directory": download_path,
        "safebrowsing.enabled": True
    }
    chrome_options.add_experimental_option("prefs", prefs)

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)


def run_test():
    driver = create_driver()
    # Уменьшаем частоту опроса (poll_frequency), чтобы не нагружать процессор
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5)

    try:
        logger.info("Открытие страницы...")
        driver.get("https://omayo.blogspot.com")

        # Скриншоты лучше сохранять в отдельную папку
        driver.save_screenshot("main_page.png")

        # 1. Проверка исчезновения
        wait.until(EC.invisibility_of_element_located((By.ID, "deletesuccess")))

        # 2. Ожидание текста
        delayed_text = wait.until(EC.visibility_of_element_located((By.ID, "delayedText")))
        logger.info(f"Найден текст: {delayed_text.text}")

        # 3. Работа с кнопкой
        timer_locator = (By.ID, "timerButton")
        btn = wait.until(EC.element_to_be_clickable(timer_locator))
        btn.click()
        logger.info("Кнопка нажата")

        # 4. Проверка деактивации
        wait.until_not(EC.element_to_be_clickable(timer_locator))
        logger.info("Тест успешно завершен: кнопка заблокирована.")

    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
        driver.save_screenshot("error_state.png")
        raise  # Пробрасываем ошибку дальше для корректного статуса теста
    finally:
        driver.quit()
        logger.info("Драйвер закрыт.")


if __name__ == "__main__":
    run_test()