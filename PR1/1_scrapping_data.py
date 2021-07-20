from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("chromedriver")
company = []
ltp = []
prev_prize = []
changes_rupee = []
volume = []
driver.get("https://www.financialexpress.com/market/stock-market/nse-top-gainers/")
store = driver.page_source
soup = BeautifulSoup(store,features="html.parser")
table = soup.find('div',attrs={'class':'dataTables_wrapper no-footer'})

data = []
row_data = []
for i, item in enumerate(table.find_all('td',attrs={'class':'td-box align-right' })):
    if i%3==0 and i!=0:
        data.append(row_data)
        row_data=[]
    row_data.append(item.text)

for d in data:
    ltp.append(d[0])
    prev_prize.append(d[1])
    volume.append(d[2])
i=0
for com in table.find_all('td',attrs={'class':'td-box align-left'}):
    i = i + 1
    if(i<=len(ltp)):
        company.append(com.text)

data = pd.DataFrame({'Company':company,
                     'LTP':ltp,
                     'Prev. Prize':prev_prize,
                     'Volume':volume})
data.to_csv('nse-top-gainers.csv')