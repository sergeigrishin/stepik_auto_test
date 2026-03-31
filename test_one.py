from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestUnit(unittest.TestCase):
    def test_one(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)

        link = "https://suninjuly.github.io/registration1.html"
        browser.get(link)

        user_name = browser.find_element(By.TAG_NAME, "input")
        user_name.send_keys("Ivan")

        last_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        last_name.send_keys("Petrov")

        user_email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        user_email.send_keys("mienail@mail.net")

        user_phone = browser.find_element(By.XPATH, "//input[@placeholder='Input your phone:']")
        user_phone.send_keys("Petrov@gmail.com")

        user_address = browser.find_element(By.XPATH, "//input[@placeholder='Input your address:']")
        user_address.send_keys("г. Москва, ул.Большака, д.21")

        button = browser.find_element(By.TAG_NAME, "button")
        button.click()

        reg = browser.find_element(By.CLASS_NAME, "container").text
        self.assertEqual(reg, 'Congratulations! You have successfully registered!', 'Ошибка')

    def test_two(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)

        link = "https://suninjuly.github.io/registration2.html"
        browser.get(link)

        user_name = browser.find_element(By.TAG_NAME, "input")
        user_name.send_keys("Ivan")

        last_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        last_name.send_keys("Petrov")

        user_email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        user_email.send_keys("mienail@mail.net")

        user_phone = browser.find_element(By.XPATH, "//input[@placeholder='Input your phone:']")
        user_phone.send_keys("Petrov@gmail.com")

        user_address = browser.find_element(By.XPATH, "//input[@placeholder='Input your address:']")
        user_address.send_keys("г. Москва, ул.Большака, д.21")

        button = browser.find_element(By.TAG_NAME, "button")
        button.click()

        reg = browser.find_element(By.CLASS_NAME, "container").text
        self.assertEqual(reg, 'Congratulations! You have successfully registered!', 'Ошибка')





if __name__ == '__main__':
    unittest.main()