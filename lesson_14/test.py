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

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://modern05.ru/catalog/id/117003/")

try:
    # Ждём появления попапа
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "marketing-popup__text")))
    
    # Ждём, пока кнопка "Принимаю" станет кликабельной (ищем по всему документу)
    accept_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.btn.btn-default[data-marketing-action='btn1']")))
    
    # Кликаем по кнопке
    accept_button.click()
    
    # Ждём, пока попап скроется
    wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "marketing-popup__text")))

except Exception as e:
    print("Попап cookie не появился или кнопка не найдена:", e)

button_cart = ("xpath","//button[@data-action='basket']")
driver.find_element(*button_cart).click()

time.sleep(5)

# Путь к директории, где лежит сам скрипт
script_dir = os.path.dirname(os.path.abspath(__file__))

# Путь к папке cookies рядом со скриптом
cookies_dir = os.path.join(script_dir, "cookies")

if not os.path.exists(cookies_dir):
    os.makedirs(cookies_dir)

pickle.dump(driver.get_cookies(), open(os.path.join(cookies_dir, "cookies.pkl"), "wb"))

time.sleep(5)

driver.delete_all_cookies()

driver.refresh()

cookies = pickle.load(open(os.path.join(cookies_dir, "cookies.pkl"), "rb"))

for cookie in cookies:
    try:
        driver.add_cookie(cookie)
    except Exception as e:
        print(f"Ошибка при добавлении куки {cookie.get('name')}: {e}")

time.sleep(5)

driver.refresh()

time.sleep(5)