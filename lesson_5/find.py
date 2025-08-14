import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

# Запуск браузера
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://modern05.ru/")

# print(type(driver.find_element("class name", "btn")))

time.sleep(10)

# driver.find_element("id", "scrollToTop").click()

driver.find_element("link text", "Строительная химия").click()

time.sleep(5)