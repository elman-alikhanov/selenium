import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

proxy_server = "37.19.220.129:8443"

options = Options()

options.add_argument(f"--proxy-server={proxy_server}")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://2ip.ru")  # 176.120.202.70

time.sleep(10)
