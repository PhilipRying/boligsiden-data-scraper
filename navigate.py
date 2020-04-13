from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import scrape_site


def navigate_site(postalcode, sitenumber = 1, pageelem = 1):
    driver = webdriver.Chrome()
    driver.get(f'https://www.boligsiden.dk/salgspris/solgt/villa/1/?postnummer={postalcode}')

    time.sleep(10)  

    click_site(pageelem,postalcode,sitenumber,driver)

def click_site(pageelem,postalcode,sitenumber,driver):    
    driver.get(f'https://www.boligsiden.dk/salgspris/solgt/villa/{sitenumber}/?postnummer={postalcode}')
    time.sleep(5)
    try:
        page = driver.find_element_by_xpath(f'/html/body/div[4]/div/div/div/div[3]/div[1]/div[{pageelem}]/div[2]/div[1]/a')
        page.click()
        time.sleep(5)
        scrape_site.scrape_page(driver)
        time.sleep(5)
        click_site(pageelem+1,postalcode,sitenumber,driver)
    except NoSuchElementException:
        try:
            driver.find_element_by_class_name('card__header')  #might be a good idea to find a more unique element on last site page. 
            print('process complete')
            return
        except NoSuchElementException:
            click_site(1,postalcode,sitenumber+1)




