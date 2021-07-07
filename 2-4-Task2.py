from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(12)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# browser.text_to_be_present_in_element((By.ID, "здесь пишем ID"), "здесь текст")
# browser.text_to_be_present_in_element((By.ID, "price"), "$100")
button = browser.find_element_by_id("book")
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

button.click()
def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

button = browser.find_element_by_id("solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# alert1 = browser.switch_to.alert
# x = alert.text
find_text = browser.find_element_by_id("input_value")
x=find_text.text
print(x)
y = calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)
button.click()
# button = browser.find_element_by_id("book")
# button.click()
# output1 = browser.find_element_by_id("price")
# if output1.text == "$95":
# 	button = browser.find_element_by_id("book")
# 	button.click()
# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()

# не забываем оставить пустую строку в конце файла





