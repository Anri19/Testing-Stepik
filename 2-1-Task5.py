import math
import time
from selenium import webdriver

link = 'http://suninjuly.github.io/get_attribute.html'

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_css_selector("[src='images/chest.png']")
x = x_element.get_attribute("valuex")
y = calc(x)

#print(y)
input1 = browser.find_element_by_id("answer")
input1.send_keys(y)
option1 = browser.find_element_by_id("robotCheckbox")
option1.click()
option2 = browser.find_element_by_id("robotsRule")
option2.click()
option2 = browser.find_element_by_css_selector("button.btn")
option2.click()
#input2 = browser.find_element_by_name("last_name")
#input2.send_keys("Petrov")

# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()

# не забываем оставить пустую строку в конце файла