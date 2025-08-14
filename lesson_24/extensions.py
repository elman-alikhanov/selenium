import os
import time
from selenium import webdriver

options = webdriver.ChromeOptions()

# Получаем абсолютный путь к текущей папке, где лежит скрипт
current_dir = os.path.dirname(os.path.abspath(__file__))

# Формируем путь к расширению
extension_path = os.path.join(current_dir, "extensions", "adblock.crx")

driver = webdriver.Chrome(options=options)

driver.get("https://modern05.ru")

time.sleep(10)