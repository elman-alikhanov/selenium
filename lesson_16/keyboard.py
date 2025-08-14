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
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

# keyboard_input = ("xpath","//input[@id='target']")
# driver.get("https://the-internet.herokuapp.com/key_presses")
# driver.find_element(*keyboard_input).send_keys("fsagagagaga")
# time.sleep(1.5)
# driver.find_element(*keyboard_input).send_keys(Keys.CONTROL + "A")
# time.sleep(1.5)
# driver.find_element(*keyboard_input).send_keys(Keys.BACK_SPACE)
# time.sleep(2)

# select_locator = ("xpath","//input[@id='react-select-3-input']")

# driver.get("https://demoqa.com/select-menu")

# time.sleep(1)

# driver.find_element(*select_locator).send_keys("Ms.")
# driver.find_element(*select_locator).send_keys(Keys.ENTER)

# time.sleep(5)

multiselect_locator = ("xpath","//input[@id='react-select-4-input']")

driver.get("https://demoqa.com/select-menu")

driver.find_element(*multiselect_locator).send_keys("Green")
driver.find_element(*multiselect_locator).send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element(*multiselect_locator).send_keys("Re")
driver.find_element(*multiselect_locator).send_keys(Keys.TAB)


time.sleep(2)