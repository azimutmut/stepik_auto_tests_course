#GET ATTRIBUTE, ASSERT, CALC(X)

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element=browser.find_element(By.ID, 'treasure')
    x_find = x_element.get_attribute("valuex")
    x = x_find
    y = calc(x)

    input1= browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    checkbox= browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    radio= browser.find_element(By.ID, 'robotsRule')
    robots_checked = radio.get_attribute("checked")
    assert robots_checked is None
    radio.click()

    button_click=browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button_click.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()