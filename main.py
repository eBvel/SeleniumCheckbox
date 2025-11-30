import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(
        ChromeDriverManager().install()
    )
)
base_url = "https://demoqa.com/checkbox"
# Метод открывает указанный URL в текущем окне браузера
driver.get(base_url)
driver.maximize_window()

# Находим и активируем чек-бокс
check_box = driver.find_element(By.XPATH, "//span[@class='rct-checkbox']")
check_box.click()

# Проверяем, что чекбокс активирован (выбран).
assert check_box.is_selected(), "Error: checkbox isn't selected"
print("Check Box is selected")

# Задержка 5 секунд и закрытие браузера
time.sleep(3)
driver.close()
print("\nBrowser is closed")