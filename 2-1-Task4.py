import math
import time
from selenium import webdriver

link = ' http://suninjuly.github.io/math.html'

browser = webdriver.Chrome()
browser.get(link)

people_radio = browser.find_element_by_id("peopleRule")
people_checked = people_radio.get_attribute("checked")
#people_checked = people_radio.get_attribute("unchecked")
print("value of people radio: ", people_checked)
assert people_checked is not None, "People radio is not selected by default"

robots_radio = browser.find_element_by_id("robotsRule")
robots_checked = robots_radio.get_attribute("checked")
print("value of robots radio: ", robots_checked)

assert robots_checked is not None, "People radio is not selected by default"

# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()

# не забываем оставить пустую строку в конце файла