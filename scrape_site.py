import time
import csv


def scrape_page(driver):
    adress = driver.find_element_by_class_name('title').get_attribute('innerText')
    area = driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/div/div/div[2]/div/table/tbody/tr[2]/td[2]').get_attribute('innerText')
    sold_price = driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/div/div/div[1]/div/table/tbody/tr[8]/td[2]').get_attribute('innerText')
    sold_date = driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/div/div/div[1]/div/table/tbody/tr[8]/td[1]').get_attribute('innerText')
    build_year = driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/div/div/div[2]/div/table/tbody/tr[7]/td[2]').get_attribute('innerText') 

    with open('data.csv','a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([adress,area,sold_price,sold_date, build_year])


        
    


