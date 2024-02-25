from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

def setup_driver():
    return webdriver.Chrome('path/to/chromedriver')

def open_whatsapp_web(driver):
    driver.get('https://web.whatsapp.com/')
    wait = WebDriverWait(driver, 30)
    wait.until(EC.title_contains("WhatsApp"))

def search_and_open_chat(driver, chat_name):
    search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
    search_box.send_keys(chat_name)

    # Wait for the chat to appear in the search results
    chat_xpath = f'//span[@title="{chat_name}"]'
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, chat_xpath)))

    # Click on the chat
    driver.find_element_by_xpath(chat_xpath).click()

def send_message(driver, message):
    message_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)

def close_browser(driver):
    driver.quit()

def main():
    # Configuration
    chrome_driver_path = 'C:/Users/ASUS/Desktop/projct 1'
    chat_name = input("Enter the chat name: ")
    message = input("Enter the message: ")

    # Logging setup
    logging.basicConfig(filename='whatsapp_bot.log', level=logging.INFO)

    try:
        driver = setup_driver()
        open_whatsapp_web(driver)
        search_and_open_chat(driver, chat_name)
        send_message(driver, message)
        time.sleep(2)  # Optional: Wait for the message to be sent
        logging.info(f"Message sent to {chat_name}: {message}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        close_browser(driver)

if __name__ == "__main__":
    main()
