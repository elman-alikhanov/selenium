import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

textarea = ("xpath","//textarea[@id='code']")
link = ("xpath","//a[@class='top-level-entry menu-link' and text()='Blog']")

driver.get("https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/General_embedding_technologies")
driver.switch_to.frame("frame_active_learning_classic_embedding_uses")
time.sleep(3)
driver.find_element(*textarea).send_keys("Test")
time.sleep(3)
driver.switch_to.default_content()
driver.find_element(*link).click()
time.sleep(3)