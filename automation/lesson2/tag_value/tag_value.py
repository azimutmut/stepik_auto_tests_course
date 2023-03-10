from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

try:
    import math
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1= browser.find_element(By.ID, 'num1').text
    x= int(num1)

    num2= browser.find_element(By.ID, 'num2').text
    y= int(num2)

    c= x+y
    c= str(c)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(c)  # ищем элемент с текстом "Python"











    # # Считываем x
    # x_element = browser.find_element(By.ID, "num1")
    # x = (x_element.text)
    # x = int(x)
    #
    # # Считываем x1
    # x_element1 = browser.find_element(By.ID, "num2")
    # x1 = (x_element1.text)
    # x1 = int(x1)
    #
    # # Считаем сумму
    # y = x + x1
    # y = str(y)
    #
    # # Выбираем нужный ответ
    # select = Select(browser.find_element(By.TAG_NAME, "select"))
    # select.select_by_value(y)

    # Нажимаем Submit
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()


