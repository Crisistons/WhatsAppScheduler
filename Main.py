from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time


def check_class_presence(message, class_name, seconds):
    print(message)
    try:
        WebDriverWait(driver, seconds).until(ec.presence_of_element_located((By.CLASS_NAME, class_name)))
    except TimeoutException:
        print("Timeout")


def search_for_contact():
    textbox = driver.find_element_by_xpath("//div[@class='_3FRCZ copyable-text selectable-text']")
    textbox.send_keys(contact_name)


def send_message():
    contact_box = driver.find_element_by_xpath("//div[@class='_2kHpK']")
    contact_box.click()
    contact_text = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    contact_text.send_keys("lol")


if __name__ == "__main__":
    path = input("Chromedriver path (leave empty if it is in the same directory): ")
    contact_name = input("Contact name: ")
    if path == '':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Chrome(executable_path=path)
    driver.get("https://web.whatsapp.com/")
    check_class_presence("Please wait...", "_3cZ5X", 60)
    # Checks if the website has loaded by checking the presence of the WhatsApp Logo Class on the screen
    check_class_presence("Please scan the QR code", "_3xpD_", 180)
    # Checks if the user has scanned the QR code by checking the 'search contacts' label in the logged in WhatsApp
    search_for_contact()
    send_message()
    time.sleep(5)
    driver.quit()
