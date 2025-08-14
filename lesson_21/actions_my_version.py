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
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
action = ActionChains(driver)
wait = WebDriverWait(driver, 10, poll_frequency=1)

sub_menu_link_locator = ("xpath", "//a[@title='Керамическая плитка']")
mramor_link_locator = ("xpath", "//a[@href='/catalog/metall_xl/']")
product_locator = ("xpath", "//a[contains(., 'Керамогранит LaminamRus Ossido Verde Lux 3.5 LAMF011794 100х296')]")
product_wrapper_locator = ("xpath", "./ancestor::div[contains(@class,'catalog-block__wrapper')]")
add_to_cart_locator = ("xpath", ".//button[contains(@class,'to_cart')]")

driver.get("https://modern05.ru/")

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


sub_menu = driver.find_element(*sub_menu_link_locator)
mramor = driver.find_element(*mramor_link_locator)


action.move_to_element(sub_menu).pause(2).click(mramor).perform()
time.sleep(3)

product = driver.find_element(*product_locator)
product_wrapper = product.find_element(*product_wrapper_locator)

add_to_cart_button = product_wrapper.find_element(*add_to_cart_locator)

add_to_cart_button.click()

time.sleep(5)

driver.get("https://modern05.ru/basket/")

time.sleep(5)

print(f"Товар добавлен в корзину")