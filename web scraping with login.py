#from xlsxwriter.utility import xl_rowcol_to_cell
#import re
#import requests
#import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
import time
from pandas import DataFrame
option = webdriver.ChromeOptions()
#option.add_argument('headless')
#driver.maximize_window()
driver.minimize_window()
#PATH= "C:/data/chromedriver.exe"
#driver= webdriver.Chrome(PATH, options=option)

LOGIN_URL = ""
URL = "" #url to scrape
#URL2= "https://prtg.infokom.id:8443/controls/sensoroverviewsmalldata.htm?id=3206"
username = "" #username
password = "" #passowrd

driver.get(LOGIN_URL)
driver.find_element_by_id("#namefieldid").send_keys(username)
driver.find_element_by_id("#namefieldpassword").send_keys(password)
driver.find_element_by_xpath("//button[@class='#namebuttonid']").click()
time.sleep(2)

driver.get(URL)
soup = bs(driver.page_source, 'lxml')

datasets = []

data = soup.find_all('div', {'class': 'overviewsmalldata'})

for item in data:
        data = {
             '#name': item.find('#list_item', {'#class': '#detail'}).text,
             '#name': item.find('#list_item', {'#class': '#detail'}).text,
             '#name': item.find('#list_item', {'#class': '#detail'}).text
}
        datasets.append(data)

#export
df = DataFrame(datasets)
df.to_excel('(path).xlsx', index=False, sheet_name="#name")
time.sleep(2)
driver.quit()