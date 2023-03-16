
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import math
link = "https://stepik.org/lesson/236895/step/1"
link1 = 'https://stepik.org/lesson/236895/step/1'
link2 = 'https://stepik.org/lesson/236896/step/1'
link3 = 'https://stepik.org/lesson/236897/step/1'
link4 = 'https://stepik.org/lesson/236898/step/1'
link5 = 'https://stepik.org/lesson/236899/step/1'
link6 = 'https://stepik.org/lesson/236903/step/1'
link7 = 'https://stepik.org/lesson/236904/step/1'
link8 = 'https://stepik.org/lesson/236905/step/1'

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()

    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    def test_a(self, browser):
        browser.get(link8)
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
        time.sleep(4)
        browser.find_element(By.XPATH, '//textarea[@placeholder="Напишите ваш ответ здесь..."]').send_keys(a)
        time.sleep(2)
        browser.find_element(By.CLASS_NAME, 'submit-submission').click()
        time.sleep(5)
        welcome_text_elt = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
        welcome_text = welcome_text_elt.text
        assert("Correct!"== welcome_text)
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()

    # import time
    # import math
    #
    # import pytest
    # from selenium import webdriver
    # from selenium.webdriver.common.by import By
    # from selenium.webdriver.support.wait import WebDriverWait
    # from selenium.webdriver.support import expected_conditions as EC
    #
    # result = ''
    #
    #
    # @pytest.fixture(scope="function")
    # def browser():
    #     print("\nstart browser for test..")
    #     browser = webdriver.Chrome()
    #     yield browser
    #     print("\nquit browser..")
    #     browser.quit()
    #     print(f"\n{result=}")
    #     print("You can also find the result in the file result.txt")
    #
    #
    # @pytest.mark.parametrize('num', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
    # def test_guest_should_see_login_link(browser, num):
    #     link = f"https://stepik.org/lesson/{num}/step/1"
    #     browser.get(link)
    #     answer = math.log(int(time.time()))
    #     text_input = WebDriverWait(browser, 10).until(
    #         EC.presence_of_element_located((By.TAG_NAME, "textarea")))
    #     text_input.send_keys(answer)
    #     browser.find_element(By.CLASS_NAME, "submit-submission").click()
    #     response = WebDriverWait(browser, 10).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
    #     feedback = response.text
    #     if feedback != 'Correct!':
    #         global result
    #         result += feedback
    #         with open('result.txt', 'w') as f:
    #             f.write(result)
    #     assert feedback == 'Correct!'
