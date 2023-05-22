from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ініціалізація веб-драйвера
driver = webdriver.Chrome()

# Відкриття веб-сторінки
driver.get("https://www.example.com")

# Очікування наявності елемента
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "myElement")))

# Виконання дії зі знайденим елементом
element.click()

# Закриття браузера
driver.quit()
