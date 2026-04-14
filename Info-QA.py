from selenium import webdriver #подключение
from selenium.webdriver.common.by import By #подключение

browser = webdriver.Chrome()
options = webdriver.ChromeOptions() #создаем опции браузера

options.add_argument("—headless") #—headless запускает браузер в режиме невидимки
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


#➖ Безголовый режим "--headless" - запускает браузер в режиме без графического интерфейса.
#Это позволяет выполнять тесты в фоновом режиме без отображения окна браузера.

#➖ Режим инкогнито "--incognito" - запускает браузер в режиме инкогнито (приватного просмотра).
#Это позволяет тестировать поведение сайта без использования кэша и сохраненных данных.

#➖ Игнорирование ошибок сертификатов "--ignore-certificate-errors" -
#игнорирует ошибки сертификата SSL при загрузке защищенных (HTTPS) страниц.

#➖ Размер окна браузера "--window-size=X,Y" - устанавливает размер окна браузера.
#Можно указать ширину и высоту в пикселях. Например, --window-size=1280,800.

#➖ Отключение кеширования "--disable-cache" - отключает кэширование в браузере.
#Это позволяет загружать каждый ресурс (например, изображения, стили, скрипты) с сервера при каждой загрузке страницы.


# 1. Настройка опций
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1280,800")

# 2. Правильная инициализация (ОДИН РАЗ)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)