from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Ініціалізація веб-драйвера
driver = webdriver.Chrome()

# Відкриття веб-сторінки з формою
driver.get("https://www.example.com/form")

# Заповнення полів форми
name_input = driver.find_element_by_name("name")
name_input.send_keys("John Doe")

email_input = driver.find_element_by_name("email")
email_input.send_keys("john.doe@example.com")

# Відправка форми
submit_button = driver.find_element_by_xpath("//button[@type='submit']")
submit_button.click()

# Перевірка результату
success_message = driver.find_element_by_class_name("success-message")
assert success_message.text == "Form submitted successfully"

# Закриття браузера
driver.quit()
