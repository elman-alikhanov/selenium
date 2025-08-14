import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

# Запуск браузера
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://modern05.ru/")

time.sleep(5)

# print(len(driver.find_elements("class name","header-menu__link")))
driver.find_elements("class name","header-menu__link")[5].click()

time.sleep(5)