from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path= r"C:\Users\AMatmusaev\Documents\selenium\python\chromedriver_win32\chromedriver.exe")

link = "http://suninjuly.github.io/huge_form.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    a = browser.find_elements(By.TAG_NAME, "input")
    for element in a:
        element.send_keys("Мой ответ")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    driver.quit()

