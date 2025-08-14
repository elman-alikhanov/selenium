import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://miro.com/index/")

login_button = driver.find_element("xpath","//a[@href='/login/']")
login_button.click()

email_field = driver.find_element("xpath","//input[@id='email']")
email_field.send_keys("elman.alihanov@yandex.ru")

# print(email_field.get_attribute("value"))

time.sleep(5) 

# email_field = driver.find_element("xpath", "//input[@id='email']")
email_field.clear()
email_field.send_keys("darnok@mail.ru")

time.sleep(5)