# CHECKBOX RADIOBUTTONS

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #input3= browser.find_element(By.ID, "answer")
    # def calc(x):
    #     return str(math.log(abs(12 * math.sin(int(x)))))
    # x_element = browser.find_element(By.ID, "#answer")
    # x = x_element.text
    # y = calc(x)
    # x_element.send_keys("x")
    import math
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element(By.ID, "input_value")
    x= x_element.text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
    time.sleep(1)
    option1.click()

    option2= browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    option2.click()

    option3= browser.find_element(By.CSS_SELECTOR, "button.btn")
    option3.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()