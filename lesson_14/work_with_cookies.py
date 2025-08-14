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

driver.get("https://modern05.ru/auth/")

# print(driver.get_cookie("BITRIX_SM_GUEST_ID"))

# print(driver.get_cookies())

# driver.add_cookie({
#     "name": "Example",
#     "value": "testing"
# })

# print(driver.get_cookie("Example"))

# before = driver.get_cookie("BITRIX_SM_SALE_UID")
# print(before)

# driver.delete_cookie("BITRIX_SM_SALE_UID")

# driver.add_cookie({
#     "name": "BITRIX_SM_SALE_UID",
#     "value": "777"
# })


# after = driver.get_cookie("BITRIX_SM_SALE_UID")
# print(after)

# driver.delete_all_cookies()

# time.sleep(30)


# try:
#     # Ждём появления попапа
#     wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "marketing-popup__text")))
    
#     # Ждём, пока кнопка "Принимаю" станет кликабельной (ищем по всему документу)
#     accept_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.btn.btn-default[data-marketing-action='btn1']")))
    
#     # Кликаем по кнопке
#     accept_button.click()
    
#     # Ждём, пока попап скроется
#     wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "marketing-popup__text")))

# except Exception as e:
#     print("Попап cookie не появился или кнопка не найдена:", e)




# login_field = ("xpath","//input[@name='AUTH_PHONE_OR_LOGIN']")
# remember_me = ("xpath","//span[text()='Запомнить меня']")
# accept_field = ("xpath","//span[contains(@class, 'form-checbox__text')]")
# submit_button = ("xpath","//div[contains(@class, 'auth__bottom-btns')]//button[@type='submit' and span[text()='Выслать код']]") 

# driver.find_element(*login_field).send_keys("9882157654")
# driver.find_element(*remember_me).click()
# driver.find_element(*accept_field).click()
# driver.find_element(*submit_button).click()

# # Путь к директории, где лежит сам скрипт
# script_dir = os.path.dirname(os.path.abspath(__file__))

# # Путь к папке cookies рядом со скриптом
# cookies_dir = os.path.join(script_dir, "cookies")

# if not os.path.exists(cookies_dir):
#     os.makedirs(cookies_dir)

# pickle.dump(driver.get_cookies(), open(os.path.join(cookies_dir, "cookies.pkl"), "wb"))

driver.delete_all_cookies()

cookies = pickle.load(open(os.getcwd()+"/cookies/cookies.pkl", "rb"))

for cookie  in cookies:
    driver.add_cookie(cookie)

time.sleep(5)

driver.refresh()

time.sleep(5)