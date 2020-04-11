import time
import pandas as pd

def scrape_page(driver):
    adress = driver.find_element_by_class_name('title').get_attribute('innerText')
    print(adress)
