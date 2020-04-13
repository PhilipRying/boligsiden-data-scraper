# Boligsiden data scraper
## WARNING - THIS LIBRARY IS MEANT FOR EDUCATIONAL PURPOSES ONLY, SCRAPING DATA CAN BE ILLEGAL. 

### Installation
Required libraries are the following and can all be installed via pip. 

    time
    csv
    selenium
   You will also need a webdriver. Chrome webdriver can be installed here. For windows place the .exe file in the same folder as you are running `navigate.py` from.  Remmember to install same version of chrome webdriver as the one on your machine. 
   [See link for chrome webdriver](https://chromedriver.chromium.org/downloads)
You can also use other webdrivers but youl need to change `navigate.py` to `driver = webdriver.xxx()`. 

### Running navigate
To run navigate use

    import navigate
    navigate.navigate_site(postal_code)
 You can also specify which specific element to start scraping from *This can be useful if it chrashes midwise*. 

navigate_site(postal, sitenumber, pageelem)
*Default will be 1 for sitenumber and 1 for pagelem if not specified*

### Data collection

Data will be stored in `data.csv`
Every time the scraper scrapes data it will add the data in a new row. Therefore previous collected data needs to be removed. *todo*
