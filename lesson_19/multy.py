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

login_field = ("xpath","//input[@type='email']")
password_field = ("xpath","//input[@type='password']")
submit_button = ("xpath","//button[@type='submit']")


driver.get("https://hyperskill.org/login")

# Ждём появления полей и вводим данные
wait.until(EC.presence_of_element_located(login_field)).send_keys("darnok@mail.ru")
wait.until(EC.presence_of_element_located(password_field)).send_keys("qwerty123")
wait.until(EC.element_to_be_clickable(submit_button)).click()

time.sleep(5)

driver_2 = webdriver.Chrome(service=service,options=options)
driver_2.get("https://hyperskill.org/login")
time.sleep(5)
