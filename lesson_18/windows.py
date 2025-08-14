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

options = Options()
options.add_argument("--window-size=1920,1080")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

for_business_button_locator = ("xpath","//a[text()=' For Business ']")
start_free_button_locator = ("xpath","//a[contains(., 'Start for Free')]")

driver.get("https://hyperskill.org/courses")
time.sleep(5)

# print(driver.current_window_handle)

# print(driver.window_handles)

driver.find_element(*for_business_button_locator).click()
time.sleep(3)

tabs = driver.window_handles
driver.switch_to.window(tabs[1])

driver.find_element(*start_free_button_locator).click()
time.sleep(3)