from RPA.Browser.Selenium import Selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

url = "http://ebill.facturaenlinea.co/Login.aspx"
user = "camtechadmin"
password = "wzo@1rjtln$o192r"
screenshot_filename = "output/screenshot.png"
driver = webdriver.Chrome('/Users/camtech/Desktop/chromedriver')

def open_the_website(url: str):
    driver.get(url)

def log_in(user: str, password: str):
    form_name = driver.find_element_by_id('ctl00_ContentPlaceHolder1_Login2_UserName')
    form_name.send_keys(user)
    form_passwd = driver.find_element_by_id('ctl00_ContentPlaceHolder1_Login2_Password')
    form_passwd.send_keys(password)
    form_login = driver.find_element_by_id("ctl00_ContentPlaceHolder1_Login2_LoginButton")
    form_login.click()
    time.sleep(5)
    link_bill = driver.find_element_by_id('ctl00_ContentPlaceHolder2_AccordionPane1_content_LinkButFactura')
    actions = ActionChains(driver)
    actions.click(login_form)
    actions.perform()

def store_screenshot(filename: str):
    driver.save_screenshot(screenshot_filename)


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
