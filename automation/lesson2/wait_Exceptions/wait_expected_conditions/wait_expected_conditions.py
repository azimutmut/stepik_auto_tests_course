
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID,"price"), '$100'))
    button1 = browser.find_element(By.ID, 'book').click()

    x_input = browser.find_element(By.ID, 'input_value').text
    x = x_input
    x = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(x)
    input1.click()

    button2= browser.find_element(By.ID, 'solve').click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()


