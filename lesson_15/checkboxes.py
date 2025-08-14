import time
import os
import pickle
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

# checkbox_1 = ("xpath","(//input[@type='checkbox'])[1]")

# driver.get("https://the-internet.herokuapp.com/checkboxes")
# time.sleep(3)
# print(driver.find_element(*checkbox_1).get_attribute("checked"))
# driver.find_element(*checkbox_1).click()
# print(driver.find_element(*checkbox_1).get_attribute("checked"))
# time.sleep(3)

# print(driver.find_element(*checkbox_1).is_selected())
# driver.find_element(*checkbox_1).click()
# print(driver.find_element(*checkbox_1).is_selected())
# time.sleep(3)

# checkbox_status = ("xpath","(//input[@id='tree-node-home'])")
# checkbox_action = ("xpath","(//span[@class='rct-checkbox'])")

# driver.get("https://demoqa.com/checkbox")
# print(driver.find_element(*checkbox_status).is_selected())
# driver.find_element(*checkbox_action).click()
# print(driver.find_element(*checkbox_status).is_selected())

# time.sleep(3)

element_one = ("xpath", "//li[text()='Cras justo odio']")

driver.get("https://demoqa.com/selectable")

before = driver.find_element(*element_one).get_attribute("class")
print(before)
driver.find_element(*element_one).click()
after = driver.find_element(*element_one).get_attribute("class")
print(after)

if "active" in after:
    print("All right")

time.sleep(3)