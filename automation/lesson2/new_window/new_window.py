from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(3)
    button= browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

    # browser.switch_to.window('Redirect page')
    first_window = browser.window_handles[0]    #основное окно
    page = browser.window_handles[1]            #даем имя на новое окно
    browser.switch_to.window(page)              #переключаемся на новое окно
    time.sleep(2)
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



