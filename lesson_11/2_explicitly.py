import time


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #вызываем expected_conditions как EC для сокращения кода

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 20, poll_frequency=1)

driver.get("https://demoqa.com/dynamic-properties")

visible_after_button  = ("xpath", "//button[@id='visibleAfter']")
 
wait.until(EC.visibility_of_element_located(visible_after_button)).click()

print("Clicked the button!")

enable_in_seconds = ("xpath", "//button[@id='enableAfter']")

wait.until(EC.element_to_be_clickable(enable_in_seconds)).click()

print("Clicked the button enable_in_seconds!")