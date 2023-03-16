import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pytest



class TestRegistr(unittest.TestCase):
    def test_registr2(self):
        link = "https://stepik.org/lesson/236895/step/1"
        browser = webdriver.Chrome()
        # для ожидания прогрузки сервера:
        browser.implicitly_wait(5)

        # для загрузки страницы:
        browser.get(link)
        # для заполнения страницы:
        browser.find_element(By.ID, "ember33").click()
        time.sleep(2)
        browser.find_element(By.ID, "id_login_email").send_keys("azimutmut@gmail.com")
        time.sleep(2)
        browser.find_element(By.ID, "id_login_password").send_keys("azamat3345")
        time.sleep(2)
        browser.find_element(By.XPATH, "//*[@id='login_form']/button").click()
        # time.sleep(50)
        browser.implicitly_wait(15)


        a = str(math.log(int(time.time())))
        input1= browser.find_element(By.ID, 'ember94').send_keys(a)
        time.sleep(2)

        browser.find_element(By.XPATH, '//*[@id="ember79"]/div/section/div/div[1]/div[4]/button').click()
        time.sleep(2)
        #
        # welcome_text_elt = browser.find_element(By.XPATH, "//*[@id='ember94']/p")
        # welcome_text = welcome_text_elt.text
        # self.assertEqual("Correct!", welcome_text)
        time.sleep(100)
        browser.quit()


if __name__ == "__main__":
    unittest.main()