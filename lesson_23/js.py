import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from scrolls import Scrolls

driver = webdriver.Chrome()
action = ActionChains(driver)
scrolls = Scrolls(driver, action)

driver.get("https://seiyria.com/bootstrap-slider/")

# driver.execute_script("alert('Hello')")

# TITLE_LOCATOR = ("xpath", "//h3[text()='Example 2: ']")
# TITLE = driver.find_element(*TITLE_LOCATOR)

# action.scroll_to_element(TITLE).perform()

TITLE_LOCATOR = ("xpath", "//h3[text()='Example 2: ']")
TITLE = driver.find_element(*TITLE_LOCATOR)

scrolls.scroll_to_element(TITLE)

# scrolls.scroll_to_bottom()

time.sleep(5)