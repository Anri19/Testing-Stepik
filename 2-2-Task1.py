import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

#link = 'http://suninjuly.github.io/selects1.html'
link = 'http://suninjuly.github.io/selects2.html'

browser = webdriver.Chrome()
browser.get(link)

def calc(x1,x2):
  return str(int(x1)+int(x2))

x_element1 = browser.find_element_by_id("num1")
x1 = x_element1.text

x_element2 = browser.find_element_by_id("num2")
x2 = x_element2.text
y = calc(x1,x2)

print(y)
select1 = Select(browser.find_element_by_tag_name("select"))
select1.select_by_visible_text(y)

button = browser.find_element_by_css_selector("button.btn")
button.click()

# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()

# не забываем оставить пустую строку в конце файла