from selenium.webdriver.common.by import By
#import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_button_add_to_basket(browser):
    browser.get(link)
    #time.sleep(10)
    
    button_basket = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button_basket is not None, "basket button did't found"

    