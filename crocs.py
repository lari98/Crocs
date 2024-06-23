import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

from selenium import webdriver
url= "https://www.crocs.com/c/women"

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation'])
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
options.add_argument("--remote-debugging-port=9222")
driver = webdriver.Chrome('F:/chromedriver',options=options)
driver.get(url)
time.sleep(6)
pageSource = driver.page_source
soup = BeautifulSoup(pageSource, 'html.parser')
conte = soup.find_all('li',class_='cx-productcard-list-item cx_col-6 cx_col-md-4 cx_col-xl-3 sized') 

wshoes = []

for items in conte:
    
    try:
        pid = items.select_one('div',class_='cx-productcard cx-brand-font cx-copy text-center lastAdded sized')['data-pid']
    except:
        pid=''
        #ptitle=items.find('h3',class_ ='cx-productcard-head')
        #prtitle=ptitle.find('img',class_ ='cx-productcard-photo img-responsive')
    title= items.find('div',class_ = 'cx-productcard-name text-gray-dark').text
    try:
        divrating =items.find('div',class_ ='cx-productcard-rating')

        rating=divrating.find('span',class_='sr-only').text
        

    except:
        rating=''
    
    try:
        reviewcount=items.find('div',class_='cx-ratings-reviewcount').text
    except:
        reviewcount=''
    try:
        pprice= items.find('span',class_ ='cx-price-current-low')
        price=pprice.find('span',class_='cx-price-value').text
    except:
        price=''


    try:
        
        links=items.find('a')['href']
    except:
        links=''
    try:

        badge=items.find('span',class_='cx-productcard-snipe-label').text
    except:
        badge=''

    print(pid,badge,title,rating,reviewcount,price,links)
    Crocs={
           'product_id': pid,
           'productname':title,
           'badge': badge,
           'Price':price,
           'rating':rating,
           'reviewcount':reviewcount,
           'links': links
    }
    wshoes.append(Crocs)
df = pd.DataFrame(wshoes)
print(df.head())
df.to_csv('D:/WCrocs.csv')