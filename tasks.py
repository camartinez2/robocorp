from RPA.Browser.Selenium import Selenium
from selenium import webdriver

browser = Selenium()
url = "http://ebill.facturaenlinea.co/Login.aspx"
url_bill = "http://ebill.facturaenlinea.co/Contenido/Facturas/Edicion.aspx"
user = "camtechadmin"
password = "wzo@1rjtln$o192r"
screenshot_filename = "output/screenshot.png"
driver = webdriver.Chrome('/Users/camtech/Desktop/chromedriver')

def open_the_website(url: str):
    driver.get(url)

def log_in(user: str, password: str):
    element = driver.find_element_by_id('ctl00_ContentPlaceHolder1_Login2_UserName')
    element.send_keys(user)
    #input_field = "id:ctl00_ContentPlaceHolder1_Login2_UserName"
    #browser.input_text(input_field, user)
    #input_field = "id:ctl00_ContentPlaceHolder1_Login2_Password"
    #browser.input_text(input_field, password)
    #browser.press_keys(input_field, "ENTER")
    #login_form = driver.find_element_by_link_text('../../imagenes/MenuLateral/menu_cargarFactura.png')
    #actions = ActionChains(driver)
    #actions.click(login_form)
    #actions.perform()

def store_screenshot(filename: str):
    driver.screenshot(filename=filename)


# Define a main() function that calls the other functions in order:
def main():
    try:
        open_the_website(url)
        log_in(user, password)
        store_screenshot(screenshot_filename)
    finally:
        driver.close_all_browsers()

# Call the main() function, checking that we are running as a stand-alone script:
if __name__ == "__main__":
    main()
