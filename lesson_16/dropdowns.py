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

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

select_locator = ("xpath","//select[@id='dropdown']")

driver.get("https://the-internet.herokuapp.com/dropdown")

dropdown = Select(driver.find_element(*select_locator))
# time.sleep(3)
# dropdown.select_by_visible_text("Option 1")
# time.sleep(3)

# time.sleep(3)
# dropdown.select_by_value("2")
# time.sleep(3)

# time.sleep(3)
# dropdown.select_by_index("1")
# time.sleep(3)

all_options = dropdown.options
# print(all_options)

# for option in all_options:
#     time.sleep(1)
#     if "Option 1" in option.text:
#         print("The element is in the list")
#     dropdown.select_by_visible_text(option.text)

# for option in all_options:
#     time.sleep(1)
#     dropdown.select_by_index(all_options.index(optionb ))

for option in all_options:
    time.sleep(1)
    dropdown.select_by_value(option.get_attribute("value"))