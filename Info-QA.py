from selenium import webdriver #подключение
from selenium.webdriver.common.by import By #подключение

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


