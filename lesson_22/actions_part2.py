import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
action = ActionChains(driver)

driver.get("https://the-internet.herokuapp.com/drag_and_drop")

COLLUMN_A = ("xpath", "//div[@id='column-a']")
COLLUMN_B = ("xpath", "//div[@id='column-b']")

A = driver.find_element(*COLLUMN_A)
B = driver.find_element(*COLLUMN_B)

time.sleep(2)

action.drag_and_drop(A, B).perform()

time.sleep(2)