# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import unittest
# import time
# class TestAbs(unittest.TestCase):
#     def test_name1(self):
#         link = "http://suninjuly.github.io/registration2.html"
#         browser = webdriver.Chrome()
#         browser.get(link)
#         input1 = browser.find_element(By.CLASS_NAME, "first")
#         input1.send_keys("Aza")
#         input2= browser.find_element(By.CLASS_NAME, "second")
#         input2.send_keys("Mat")
#         input3= browser.find_element(By.CLASS_NAME, "third")
#         input3.send_keys("azamat@gmail.mars")
#         button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#         time.sleep(4)
#         button.click()
#         time.sleep(1)
#         welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#         welcome_text = welcome_text_elt.text
#         self.assertEqual( "Congratulations! You have successfully registered!", welcome_text)
#         browser.quit()
#     def test_name2(self):
#         link = "http://suninjuly.github.io/registration2.html"
#         browser = webdriver.Chrome()
#         browser.get(link)
#
#         input3 = browser.find_element(By.ID, "form-control.first")
#         input3.send_keys("azamat@gmail.mars")
#         input2 = browser.find_element(By.CLASS_NAME, "form-control.third")
#         input2.send_keys("azamat@gmail.mars")
#         # Отправляем заполненную форму
#         button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#         time.sleep(2)
#         button.click()
#
#         # Проверяем, что смогли зарегистрироваться
#         # ждем загрузки страницы
#         time.sleep(1)
#
#         # находим элемент, содержащий текст
#         welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#         # записываем в переменную welcome_text текст из элемента welcome_text_elt
#         welcome_text = welcome_text_elt.text
#
#         # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#         self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
#         browser.quit()
# # finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     # time.sleep(2)
# if __name__=="__main":
#     unittest.main()


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

class TestRegistr(unittest.TestCase):
    def test_registr1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        # для ожидания прогрузки сервера:
        browser.implicitly_wait(5)
        # для загрузки страницы:
        browser.get(link)
        # для заполнения страницы:
        input1 = browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
        input1.send_keys("Evgeny")
        input2 = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
        input2.send_keys("Karamyshev")
        input3 = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
        input3.send_keys("karamnot@icloud.com")
        # для нажатия кнопки:
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # для поиска текста:
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registr2(self):
        link = " http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        # для ожидания прогрузки сервера:
        browser.implicitly_wait(5)
        # для загрузки страницы:
        browser.get(link)
        # для заполнения страницы:
        input1 = browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
        input1.send_keys("Evgeny")
        input2 = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
        input2.send_keys("Karamyshev")
        input3 = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
        input3.send_keys("karamnot@icloud.com")
        # для нажатия кнопки:
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # для поиска текста:
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__":
    unittest.main()