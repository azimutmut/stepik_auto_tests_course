from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    button1= browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    alert = browser.switch_to.alert
    alert.accept()

    x_input= browser.find_element(By.ID, 'input_value').text
    x=x_input
    x= calc(x)

    input1= browser.find_element(By.ID, 'answer')
    input1.send_keys(x)
    input1.click()

    button2= browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
