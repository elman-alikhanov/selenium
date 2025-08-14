import time


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #вызываем expected_conditions как EC для сокращения кода

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 20, poll_frequency=1)

driver.get("https://the-internet.herokuapp.com/dynamic_controls")

remove_button  = ("xpath", "//button[text()='Remove']")

driver.find_element(*remove_button).click()

wait.until(EC.invisibility_of_element_located(remove_button))

print("ALL RIGHT")

enable_button = ("xpath", "//button[text()='Enable']")
text_field = ("xpath", "//input[@type='text']")

wait.until(EC.element_to_be_clickable(enable_button)).click()
time.sleep(2)
wait.until(EC.element_to_be_clickable(text_field)).send_keys("HELLO")
time.sleep(2)
wait.until(EC.text_to_be_present_in_element_value(text_field, "HELLO"))
time.sleep(2)

print("ALL RIGHT")