from RPA.Browser.Selenium import Selenium
from selenium import webdriver

driver = webdriver.Chrome() 

browser = Selenium()
url = "http://ebill.facturaenlinea.co/Login.aspx"
url_bill = "http://ebill.facturaenlinea.co/Contenido/Facturas/Edicion.aspx"
user = "camtechadmin"
password = "wzo@1rjtln$o192r"
screenshot_filename = "output/screenshot.png"


def open_the_website(url: str):
    browser.open_available_browser(url)


def log_in(user: str, password: str):
    input_field = "id:ctl00_ContentPlaceHolder1_Login2_UserName"
    browser.input_text(input_field, user)
    input_field = "id:ctl00_ContentPlaceHolder1_Login2_Password"
    browser.input_text(input_field, password)
    browser.press_keys(input_field, "ENTER")
    #input_field = "id:ctl00_ContentPlaceHolder2_AccordionPane1_content_Image10"
    #input_field.click()
    #browser.open(url_bill)
    click_button_when_visible()


def store_screenshot(filename: str):
    browser.screenshot(filename=filename)


# Define a main() function that calls the other functions in order:
def main():
    try:
        open_the_website(url)
        log_in(user, password)
        store_screenshot(screenshot_filename)
    finally:
        browser.close_all_browsers()

# Call the main() function, checking that we are running as a stand-alone script:
if __name__ == "__main__":
    main()
