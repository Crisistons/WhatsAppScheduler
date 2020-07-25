from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def check_class_presence(message, class_name, seconds):
    print(message)
    try:
        WebDriverWait(driver, seconds).until(ec.presence_of_element_located((By.CLASS_NAME, class_name)))
    except TimeoutException:
        print("Timeout")


if __name__ == "__main__":
    path = input("Chromedriver path (leave empty if it is in the same directory): ")
    if path == '':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Chrome(executable_path=path)
    driver.get("https://web.whatsapp.com/")
    check_class_presence("Please wait...", "_3cZ5X", 60)
    # Checks if the website has loaded by checking the presence of the WhatsApp Logo Class on the screen
    check_class_presence("Please scan the QR code", "_3xpD_", 180)
    # Checks if the user has scanned the QR code by checking the 'search contacts' label in the logged in WhatsApp
    driver.quit()
