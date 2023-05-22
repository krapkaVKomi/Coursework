from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Ініціалізація веб-драйвера (наприклад, для Google Chrome)
driver = webdriver.Chrome()

# Відкриття веб-сторінки
driver.get("https://www.example.com")

# Знаходження елементу на сторінці (наприклад, поле введення)
input_element = driver.find_element_by_name("search")

# Введення значення в поле введення
input_element.send_keys("Hello, World!")

# Відправлення форми (наприклад, натискання клавіші Enter)
input_element.send_keys(Keys.RETURN)

# Очікування завершення завантаження сторінки
driver.implicitly_wait(10)  # Зачекати до 10 секунд

# Перевірка результатів
assert "Результати пошуку" in driver.page_source

# Закриття веб-драйвера та браузера
driver.quit()
