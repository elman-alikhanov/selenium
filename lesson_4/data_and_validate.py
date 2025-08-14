import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Запуск браузера
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://modern05.ru/")

url = driver.current_url
print("Page URL:" , url)
assert url == "https://modern05.ru/", "Invalid URL"

current_title = driver.title
print("Current page title: " , current_title)
assert current_title == "Modern05 – интернет-магазин сантехники и керамической плитки в Махачкале", "Incorrect page title"

soucer_code = driver.page_source
print("Page source:", soucer_code)

time.sleep(3)