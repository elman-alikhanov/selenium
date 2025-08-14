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

yes_radio_status = ("xpath", "//input[@id='yesRadio']")
yes_radio_action = ("xpath", "//label[@for='yesRadio']")

no_radio_status = ("xpath", "//input[@id='noRadio']")
no_radio_action = ("xpath", "//label[@for='noRadio']")

driver.get("https://demoqa.com/radio-button")
print(driver.find_element(*yes_radio_status).is_selected())
driver.find_element(*yes_radio_action).click()
print(driver.find_element(*yes_radio_status).is_selected())
time.sleep(3) 

print(driver.find_element(*no_radio_status).is_enabled())

time.sleep(3)