from selenium import webdriver
import time


def test_button_existing(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.implicitly_wait(5)
    button1 = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
    assert button1 > 0, "Button doesn't exist!"
