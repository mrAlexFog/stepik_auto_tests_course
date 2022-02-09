import time, os
from math import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def selenium_lesson_226():

    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/execute_script.html')

    try:

        # считываем переменную, проводим вычисления
        x_unknown = browser.find_element_by_xpath('//div[contains(@class, "form-group")]/descendant::span[contains(@id, "input_value")]').text
        print(x_unknown)
        x = log(abs(12 * sin(int(x_unknown))))
        # ввести ответ в поле
        x_input = browser.find_element_by_xpath('//input[contains(@id, "answer")]')
        x_input.send_keys(x)
        # ищем я робот
        robot_checkbox = browser.find_element_by_xpath('//input[contains(@id, "robotCheckbox")]')
        robot_checkbox.click()
        # ищем роботы рулят
        robot_rule = browser.find_element_by_xpath('//input[contains(@id, "robotsRule")]')
        browser.execute_script("return arguments[0].scrollIntoView(true);", robot_rule)
        robot_rule.click()
        # ищем Submit (скрол)
        button = browser.find_element_by_xpath('//button[text()= "Submit"]')
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()

    except:
        print('Ошибка выполнения')

    finally:
        time.sleep(30)
        browser.quit()

def selenium_lesson_228():

    bromser = webdriver.Chrome()
    bromser.get('http://suninjuly.github.io/file_input.html')

    try:

        firstname = bromser.find_element_by_xpath('//input[contains(@name, "firstname")]')
        firstname.send_keys('Alex')
        lastname = bromser.find_element_by_xpath('//input[contains(@name, "lastname")]')
        lastname.send_keys('Tomonov')
        email = bromser.find_element_by_xpath('//input[contains(@name, "email")]')
        email.send_keys('stepik@mail.ru')

        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'file.txt')

        choose_file_to_upload = bromser.find_element_by_xpath('//input[contains(@id, "file")]')
        choose_file_to_upload.send_keys(file_path)

        button = bromser.find_element_by_xpath('//button[contains(@type, "submit")]')
        button.click()

    except:
        print('Ошибка выполнения')
        
    finally:
        time.sleep(30)
        bromser.quit()

def selenium_lesson_234():

    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')

    try:
        button = browser.find_element_by_xpath('//button[contains(@type, "submit")]')
        button.click()
        confirm = browser.switch_to.alert
        confirm.accept()

        x = browser.find_element_by_xpath('//span[contains(@id, "input_value")]').text
        print(x)
        x_calc = log(abs(12 * sin(int(x))))
        print(x_calc)

        input = browser.find_element_by_xpath('//input[contains(@name, "text")]')
        input.send_keys(x_calc)

        button2 = browser.find_element_by_xpath('//button[contains(@type, "submit")]')
        button2.click()
    
    except:
        print('Ошибка выполнения')

    finally:
        print()
        print('Искомый текст', browser.switch_to.alert.text.split()[-1])
        print()
        browser.quit()

def selenium_lesson_236():

    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    try:
        clic_one = browser.find_element_by_xpath('//button[contains(@type, "submit")]')
        clic_one.click()       

        window_two = browser.window_handles[1]                                                  # создаем имя новой вкладке
        browser.switch_to.window(window_two)                                                    # просим браузер работать в новой вкладке

        x = browser.find_element_by_xpath('//span[contains(@id, "input_value")]').text          # находим х элемент
        x_calc = log(abs(12 * sin(int(x))))                                                     # расчет

        input_sub = browser.find_element_by_xpath('//input[contains(@class, "form-control")]')  # находим понель ввода
        input_sub.send_keys(x_calc)                                                             # вводим раститанный элемент

        button = browser.find_element_by_xpath('//button[contains(@type, "submit")]')           # находим элемент submit
        button.click()                                                                          # жмем на элемент submit

    finally:
        print()
        print('Искомый текст', browser.switch_to.alert.text.split()[-1])
        print()
        browser.quit()

def selenium_lesson_246():

    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/cats.html')

    try:
        button = browser.find_element_by_id("button")
        button.click()

    finally:
        time.sleep(30)
        browser.quit()

def selenium_lesson_248():

    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    browser.implicitly_wait(5)

    try:
        
        WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
        browser.find_element_by_xpath('//button[contains(@id, "book")]').click()

        browser.execute_script("window.scrollBy(0, 500);")

        x = browser.find_element_by_xpath('//span[contains(@id, "input_value")]').text
        x_clac = log(abs(12 * sin(int(x))))

        form_control = browser.find_element_by_xpath('//input[contains(@id, "answer")]')
        form_control.send_keys(x_clac)

        subClick = browser.find_element_by_xpath('//button[contains(@type, "submit")]')
        subClick.click()
    
    finally:
        print()
        print('Искомый текст', browser.switch_to.alert.text.split()[-1])
        print()
        time.sleep(30)
        browser.quit()

selenium_lesson_248()