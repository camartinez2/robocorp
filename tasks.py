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

def create_bill ():
    driver.get(urlbill)
    time.sleep(2)
    companyName = "Cecilia Cardenas"
    address = "Calle 12 # 24 - 12"
    notes = "Se realiza el cobro a la fecha"
    productCode_1 = "RD412"
    productName_1 = "Radiografias"
    quantity_1 = "3"
    price_1 = "123000"
    taxRate = "12"
    create_bill_client(companyName, address, notes)
    create_bill_product(productCode_1, productName_1, quantity_1, price_1)
    create_bill_taxes(taxRate)
    time.sleep(2)
    form_save = driver.find_element_by_name("invoice_btn")
    form_save.click()

def create_bill_client(companyName: str, address: str, notes: str):
    time.sleep(2)
    form_passwd = driver.find_element_by_id('companyName')
    form_passwd.send_keys(companyName)
    form_passwd = driver.find_element_by_id('address')
    form_passwd.send_keys(address)
    form_passwd = driver.find_element_by_id('notes')
    form_passwd.send_keys(notes)

def create_bill_product(productCode_1: str, productName_1: str, quantity_1: str, price_1: str):
    form_passwd = driver.find_element_by_id('productCode_1')
    form_passwd.send_keys(productCode_1)
    form_passwd = driver.find_element_by_id('productName_1')
    form_passwd.send_keys(productName_1)
    form_passwd = driver.find_element_by_id('quantity_1')
    form_passwd.send_keys(quantity_1)
    form_passwd = driver.find_element_by_id('price_1')
    form_passwd.send_keys(price_1)

def create_bill_taxes(taxRate: str):
    form_passwd = driver.find_element_by_id('taxRate')
    form_passwd.send_keys(taxRate)

def store_screenshot(filename: str):
    time.sleep(3)
    driver.save_screenshot(filename)
    time.sleep(3)

# Define a main() function that calls the other functions in order:
def main():
    try:
        open_the_website(url)
        log_in(user, password)
        create_bill ()
        store_screenshot(screenshot_filename)
    finally:
        driver.close()

# Call the main() function, checking that we are running as a stand-alone script:
if __name__ == "__main__":
    main()
