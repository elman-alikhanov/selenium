import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# ---------------- BasePage ----------------
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.action = ActionChains(driver)

    def open(self, url):
        self.driver.get(url)

    def click_when_clickable(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

# ---------------- CategoryPage ----------------
class CategoryPage(BasePage):
    SUB_MENU = ("xpath", "//a[@title='Керамическая плитка']")
    CATEGORY_LINK = ("xpath", "//a[@href='/catalog/metall_xl/']")

    def go_to_category(self):
        sub_menu = self.find_element(self.SUB_MENU)
        category_link = self.find_element(self.CATEGORY_LINK)
        self.action.move_to_element(sub_menu).pause(1).click(category_link).perform()
        print("Перешли в категорию")

    def add_product_to_cart(self, product_name):
        product_locator = ("xpath", f"//a[contains(., '{product_name}')]")
        product_wrapper_locator = ("xpath", "./ancestor::div[contains(@class,'catalog-block__wrapper')]")
        add_to_cart_locator = ("xpath", ".//button[contains(@class,'to_cart')]")

        product = self.find_element(product_locator)
        product_wrapper = product.find_element(*product_wrapper_locator)
        add_button = product_wrapper.find_element(*add_to_cart_locator)
        add_button.click()
        print(f"Товар '{product_name}' добавлен в корзину")

# ---------------- BasketPage ----------------
class BasketPage(BasePage):
    def is_product_in_basket(self, product_name):
        basket_item_locator = ("xpath", f"//a[contains(., '{product_name}')]")
        try:
            self.find_element(basket_item_locator)
            print(f"Товар '{product_name}' успешно отображается в корзине")
            return True
        except:
            print(f"Товар '{product_name}' НЕ найден в корзине")
            return False

# ---------------- Main Script ----------------
if __name__ == "__main__":
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(2)

    try:
        BASE_URL = "https://modern05.ru/"
        PRODUCT_NAME = "Керамогранит LaminamRus Ossido Verde Lux 3.5 LAMF011794 100х296"

        # --- Открываем сайт и закрываем попап cookies ---
        driver.get(BASE_URL)
        try:
            accept_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(("css selector", "span.btn.btn-default[data-marketing-action='btn1']"))
            )
            accept_button.click()
            print("Попап cookie закрыт")
        except:
            print("Попап cookie не появился")

        # --- Работа с категорией и добавление товара ---
        category_page = CategoryPage(driver)
        category_page.go_to_category()
        category_page.add_product_to_cart(PRODUCT_NAME)

        # --- Проверка корзины ---
        basket_page = BasketPage(driver)
        basket_page.open(BASE_URL + "basket/")
        basket_page.is_product_in_basket(PRODUCT_NAME)

        time.sleep(5)

    finally:
        driver.quit()
