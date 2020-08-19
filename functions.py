from selenium import webdriver
import os
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time


def create_driver_window(headless):
    chrome_options = Options()
    chrome_options.add_argument("user-data-dir=seleniumMB")
    if headless:
        chrome_options.add_argument("--headless")
    GetDriver = webdriver.Chrome(chrome_options=chrome_options)

    return GetDriver


def close_driver_window(driver):
    driver.close()


def find_and_click(driver, xpath):
    object = driver.find_element_by_xpath(xpath)
    object.click()


def try_find_and_click(driver, xpath):
    try:
        Element = driver.find_element_by_xpath(xpath)
        Element.click()
        time.sleep(0.1)
        return True, None
    except:
        return False, "Failed"


def check_element_exists(driver, xpath, waittime):
    try:
        WebDriverWait(driver, waittime).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return True, None
    except:
        return False, "Does not exist"


def check_is_clickable(driver, xpath, waittime):
    try:
        WebDriverWait(driver, waittime).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        return True, None
    except:
        return False, "Not clickable"


def type(driver, xpath, text):
    try:
        element = driver.find_element_by_xpath(xpath)
        element.send_keys(text)
        return True, None
    except:
        return False, "Failed"


def navigate_to_page(driver, url):
    driver.get(url)


def search_for_text(driver, text):
    # Searches for all elements in page with a given text string, returns list of matching elements
    elements = driver.find_elements_by_xpath(".//*[contains(text(),'%s')]" % text)
    return elements

def check_for_and_click_from_list_of_xpaths(driver, xpathlist):
    for paths in xpathlist:
        status, response = check_element_exists(driver, paths, 1)
        if status:
            find_and_click(driver, paths)
            return True, None
    return False, None
