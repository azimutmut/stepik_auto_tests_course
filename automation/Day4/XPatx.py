from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path= r"C:\Users\AMatmusaev\Documents\selenium\python\chromedriver_win32\chromedriver.exe")

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)
   #   "//p[text()='hello']"
    input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/input")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "/html/body/div/form/div[3]/input")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.XPATH, "/html/body/div/form/div[4]/input")
    input4.send_keys("Russia")
   # browser.find_element(By.XPATH, "//*[ text()='Submit']").click()
    button= browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    driver.quit()

