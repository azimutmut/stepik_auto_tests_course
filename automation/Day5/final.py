from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CLASS_NAME, "first")
    input1.send_keys("Aza")
    input2= browser.find_element(By.CLASS_NAME, "second")
    input2.send_keys("Mat")
    input3= browser.find_element(By.CLASS_NAME, "third")
    input3.send_keys("azamat@gmail.mars")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    time.sleep(4)
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    # browser.quit()