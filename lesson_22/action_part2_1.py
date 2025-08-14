import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
action = ActionChains(driver)

driver.get("https://tympanus.net/Development/DragDropInteractions/sidebar.html")

# setTimeout(function () {debugger;}, 5000);

GRID_ITEM = ("xpath", "(//div[@class='grid__item'])[3]")
SIDEBAR_ITEM = ("xpath", "(//div[@class='drop-area__item'])[3]")

action.click_and_hold(driver.find_element(*GRID_ITEM)) \
    .pause(1.5) \
    .move_to_element(driver.find_element(*SIDEBAR_ITEM)) \
    .release() \
    .pause(1.5) \
    .perform()

time.sleep(5)