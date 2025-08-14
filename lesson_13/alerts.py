import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://demoqa.com/alerts/")

# alert_button = ("xpath", "//button[@id='alertButton']")
# wait.until(EC.element_to_be_clickable(alert_button)).click()

# alert = wait.until(EC.alert_is_present())

# driver.switch_to.alert

# time.sleep(3)

# alert.accept()

# time.sleep(3)

# part 2

# alert_button2 = ("xpath", "//button[@id='confirmButton']")
# wait.until(EC.element_to_be_clickable(alert_button2)).click()

# alert = wait.until(EC.alert_is_present())

# driver.switch_to.alert

# time.sleep(3)
# print(alert.text)
# alert.dismiss()

# time.sleep(3)

# part 3

alert_button3 = ("xpath", "//button[@id='promtButton']")
wait.until(EC.element_to_be_clickable(alert_button3)).click()

alert = wait.until(EC.alert_is_present())

driver.switch_to.alert

time.sleep(3)

alert.send_keys("Hello World")

time.sleep(3)

alert.accept()

time.sleep(15)