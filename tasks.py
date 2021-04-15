from RPA.Browser.Selenium import Selenium
from selenium import webdriver

url = "http://ebill.facturaenlinea.co/Login.aspx"
user = "camtechadmin"
password = "wzo@1rjtln$o192r"
screenshot_filename = "output/screenshot.png"
driver = webdriver.Chrome('/Users/camtech/Desktop/chromedriver')

def open_the_website(url: str):
    driver.get(url)

def log_in(user: str, password: str):
    element = driver.find_element_by_id('ctl00_ContentPlaceHolder1_Login2_UserName')
    element.send_keys(user)
    element = driver.find_element_by_id('ctl00_ContentPlaceHolder1_Login2_Password')
    element.send_keys(password)
    driver.find_element_by_id("ctl00_ContentPlaceHolder1_Login2_LoginButton").click()
    login_form = driver.find_element_by_id('ctl00_ContentPlaceHolder2_AccordionPane1_content_Image10')
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
        store_screenshot(screenshot_filename)
    finally:
        driver.close()

# Call the main() function, checking that we are running as a stand-alone script:
if __name__ == "__main__":
    main()
