
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    input_value= browser.find_element(By.ID, 'input_value')
    x= input_value.text
    x= calc(x)

    input1= browser.find_element(By.ID, 'answer')
    input1.click()
    input1.send_keys(x)

    checkboxx= browser.find_element(By.ID, 'robotCheckbox').click()


    input = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input.click()

    botton= browser.find_element(By.CSS_SELECTOR, 'button.btn')
    botton.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()