import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
action = ActionChains(driver)

left_click_button = ("xpath", "//button[@id='leftClick']")
double_click_button = ("xpath", "//button[@id='doubleClick']")
right_click_button = ("xpath", "//button[@id='rightClick']")
hover_button = ("xpath", "//button[@id='colorChangeOnHover']")


driver.get("https://testkru.com/Elements/Buttons")

left_button = driver.find_element(*left_click_button)
double_button = driver.find_element(*double_click_button)
right_button = driver.find_element(*right_click_button)
hover = driver.find_element(*hover_button)

time.sleep(3)

# action.click(left_button).perform()
# action.double_click(double_button).perform()
# action.context_click(right_button).perform()

# action.click(left_button).pause(2).double_click(double_button).pause(2).context_click(right_button).perform()

action.move_to_element(hover).perform()

time.sleep(3)