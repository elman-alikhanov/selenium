import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service 

chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://the-internet.herokuapp.com/upload")

time.sleep(3)

upload_filed = driver.find_element("xpath", "//input[@type='file']")
upload_filed.send_keys(f"{os.getcwd()}\lesson_10\downloads\Gaming_Q.png")

time.sleep(5)