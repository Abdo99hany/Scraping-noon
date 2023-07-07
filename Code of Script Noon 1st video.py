"""
 This is where the
 required libraries are imported at the beginning of the code. 
 The libraries include requests, BeautifulSoup, pandas, datetime, selenium, 
 and webdriver_manager. These libraries are used throughout the code for web scraping and data manipulation.
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
"""
This is where the Selenium web driver is set up.
The chrome_driver_path variable contains the path to the chromedriver.exe
file on the local machine. The options variable is set up to allow the browser to run in the background. 
The driver variable is then set up as a Chrome web driver instance.
"""

 #  some codes thar make the selenium works 
chrome_driver_path =r'C:\Program Files(x86)\Google\Chrome\Application\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(chrome_driver_path))

basurl = "https://www.noon.com"
productlinks = []
for i in range(1,19):
    r=driver.get(f'https://www.noon.com/egypt-en/electronics-and-mobiles/mobiles-and-accessories/mobiles-20905/?limit=50&page={i}')
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'html')))
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    spans = soup.find_all('div',{'class':'sc-85fbb0c9-7 cuALSM grid'})
    for span in spans:
        links = soup.find_all('a')  
        for link in links:
            if 'href' in link.attrs:
                productlinks.append(basurl + link['href'])
                print(productlinks[-1])

"""
This is where the product links are extracted from the search pages.
The spans variable is set up to find all the HTML elements that contain the product listing.
The links variable is set up to find all the HTML elements that contain the links to the product pages.
the if statement is used to check if the href attribute is present in the link element.
If it is, the product link is appended to the productlinks list and printed to the console.

"""
 

