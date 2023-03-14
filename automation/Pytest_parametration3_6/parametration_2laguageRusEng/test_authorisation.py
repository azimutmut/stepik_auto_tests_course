# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# @pytest.mark.parametrize('language', ["ru", "en-gb"])
# def test_guest_should_see_login_link(browser, language):
#     link = f"https://stepik.org/lesson/236895/step/1{language}/"
#     browser.get(link)
#     browser.find_element(By.ID, "ember33").click()
#
#


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
link = "https://stepik.org/lesson/236895/step/1"

@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    def test_a(self, browser):
        browser.get(link)
        # time.sleep(20)
        browser.implicitly_wait(10)
        browser.find_element(By.ID, "ember33").click()
        time.sleep(2)
        browser.find_element(By.ID, "id_login_email").send_keys("azimutmut@gmail.com")
        time.sleep(2)
        browser.find_element(By.ID, "id_login_password").send_keys("azamat3345")
        time.sleep(2)
        browser.find_element(By.XPATH, "//*[@id='login_form']/button").click()
        # time.sleep(50)
        browser.implicitly_wait(10)
        time.sleep(2)

        a= str(math.log(int(time.time())))
        browser.find_element(By.XPATH, '//*[@id="ember94"]')\
        .send_keys(a)
        time.sleep(2)
        browser.find_element(By.XPATH, '//*[@id="ember79"]/div/section/div/div[1]/div[4]/button').click()
        time.sleep(1000)
        # time.sleep(2)

        # welcome_text_elt = browser.find_element(By.XPATH, "smart-hints__hint")
        # welcome_text = welcome_text_elt.text
        # assert "Correct!" == welcome_text
        # time.sleep(100000)



    # def test_guest_should_see_basket_link_on_the_main_page(self, browser):
    #     browser.get(link)
    #     browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
    #
    # @pytest.mark.xfail
    # def test_guest_should_see_search_button_on_the_main_page(self, browser):
    #     browser.get(link)
    #     browser.find_element(By.CSS_SELECTOR, "button.favorite")