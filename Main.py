from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def check_qr():
    print("Please scan the QR code")
    pass


def check_loading_screen():
    print("Please wait...")
    try:
        WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.CLASS_NAME, "_3cZ5X")))
    except TimeoutException:
        print("Timeout")


if __name__ == "__main__":
    path = input("Chromedriver path (leave empty if it is in the same directory): ")
    if path == '':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Chrome(executable_path=path)
    driver.get("https://web.whatsapp.com/")
    check_loading_screen()
    driver.quit()
