# NoSuchElementException - нет такого вообще
# StaleElementReferenceException -  был элемент да сплыл
# ElementNotVisibleException - видишь элемент? И я не вижу, а он есть

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)
    smth= browser.find_element(By.ID, "button")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()



