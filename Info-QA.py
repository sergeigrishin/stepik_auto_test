import os

from selenium import webdriver #подключение
from selenium.webdriver.common.by import By #подключение
class Student:
    browser = webdriver.Chrome()
    browser.get('https://stepik.org/lesson/666225/step/1?unit=664214')

    PAGE_URL = browser.current_url # Получаем текущий URL-адрес в переменную
    print(PAGE_URL) # Выводим значение переменной


    PAGE_TITLE = browser.title # Записываем значение title в переменную page_title
    print("Title страницы: ", PAGE_TITLE) # Выводим значение переменной на экран

    PAGE_SOURCE = browser.page_source # Записываем в переменную всю веб-страницу
    print(PAGE_SOURCE) # Печатаем HTML-код в терминал

    #Поиск элементов XPath
    #//div[@class=’table’] - по классу
    #//employee[@id=’2’] - по id
    #//employee[@id=’1’]/name[text()=’David’] - по тексту
    #//name[text()=’John’] - по тексту

    #//элемент [содержит (@атрибут, ‘значение содержимого’) ]
    #<button class="btn btn-white">Join</button>
    #// button[contains(@class, 'btn')]
    #//button[contains(text(), 'Join')]


    #Загрузка файла (если загрузка файла реализована через button - значит где-то точно есть input)
    #import os element.send_keys(os.path.join(os.getcwd(), "picture.jpg")) - для загрузки файла из  любой операционки
    browser.find_element("https://ya.ru").send_keys(f"{os.getcwd()}/doanloads/name_file.txt")



    #element_to_be_clickable(locator) - Ожидает видимости элемента и его кликабельности (возможности кликнуть).
    #visibility_of_element_located(locator) - Ожидание проверки того, что элемент присутствует в DOM и виден визуально. Видимость означает, что элемент не только отображается но также имеет высоту и ширину, которые больше 0.
    #invisibility_of_element_located(locator) - Ожидание проверки того, является ли элемент невидимым или он исчез из DOM.
    #text_to_be_present_in_element(locator, text) - Ожидание наличия нужного текста в элементе.


class Example:
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


