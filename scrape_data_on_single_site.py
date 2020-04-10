from selenium import webdriver
import pandas as pd
import time


driver = webdriver.Chrome()


driver.get('https://www.boligsiden.dk/salgspris/solgt/villa/1/?postnummer=2970')

time.sleep(10)

pagecount = 5  
driver.find_element_by_xpath(f'/html/body/div[4]/div/div/div/div[3]/div[1]/div[{pagecount}]/div[2]/div[1]/a').click()
time.sleep(5)
adress = driver.find_element_by_class_name('title').get_attribute('innerText')



print(adress)
