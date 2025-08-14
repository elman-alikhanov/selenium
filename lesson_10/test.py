import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get("https://kirgu.ru/")

callback_button = driver.find_element('xpath', '//a[@class="h-feadback__phone"]')
callback_button.click();

name_field = driver.find_element('xpath', '//aside[@id="ordercall-popup"]//input[@name="NAME"]')
name_field.send_keys("Тестовый тест")

phone_field = driver.find_element('xpath', '//aside[@id="ordercall-popup"]//input[@type="tel"]')
phone_field.send_keys("8800200600")

checkbox_field = driver.find_element('xpath', '//aside[@id="ordercall-popup"]//input[@id="userTermsAgreementCheckbox-2"]')
if not checkbox_field.is_selected():
    checkbox_field.click()

submit_button = driver.find_element('xpath', '//aside[@id="ordercall-popup"]//div[contains(@class, "ordercall-popup-footer")]//button[contains(@class, "ordercall-popup-btn")]')
submit_button.click()

time.sleep(5)

try:
    success_message = driver.find_element('xpath', '//div[contains(@class, "ordercall-popup-body") and contains(text(), "Спасибо, ваше сообщение отправлено")]')

    print("Заявка успешно отправлена")
except:
    print("Ошибка: заявка не была отправлена")