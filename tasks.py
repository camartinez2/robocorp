from RPA.Browser.Selenium import Selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

url = "http://192.168.225.63:12121"
urlbill = "http://192.168.225.63:12121/create_invoice.php"
user = "registro@baulphp.com"
password = "12345"
screenshot_filename = "output/screenshot.png"
driver = webdriver.Chrome('/Users/camtech/Desktop/chromedriver')

def open_the_website(url: str):
    driver.get(url)

def log_in(user: str, password: str):
    form_name = driver.find_element_by_id('email')
    form_name.send_keys(user)
    form_passwd = driver.find_element_by_id('password')
    form_passwd.send_keys(password)
    form_login = driver.find_element_by_id("login")
    time.sleep(2)
    form_login.click()
    time.sleep(2)
    #link_bill = driver.find_element_by_id('create_invoice')
    #link_bill.click()

def store_screenshot(filename: str):
    time.sleep(10)
    driver.save_screenshot(filename)
    time.sleep(10)

# Define a main() function that calls the other functions in order:
def main():
    try:
        open_the_website(url)
        log_in(user, password)
        #store_screenshot(screenshot_filename)
    finally:
        store_screenshot(screenshot_filename)
        #driver.close()

# Call the main() function, checking that we are running as a stand-alone script:
if __name__ == "__main__":
    main()
