import requests
from bs4 import BeautifulSoup
import re
import csv

#시가총액 top100
def create_soup(page):
  url='https://finance.naver.com/sise/sise_market_sum.naver?&page={}'.format(page)
  res = requests.get(url)
  soup=BeautifulSoup(res.text,"lxml")
  return soup

file = open('data/코스피시가총액1~100.csv','w',encoding='utf-8',newline="")
writer=csv.writer(file)
title='N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE'.split('\t')
writer.writerow(title)

for i in range(1,3):
  soup = create_soup(i)
  es=soup.find('table',attrs={'class':'type_2'}).find_all('tr')
  for e in es:
    columns=e.find_all('td')
    if len(columns)<=1:
      continue
    data =[re.sub('\n|\t|상승|하락|보합','',col.get_text()) for col in columns]
    print(data)
    writer.writerow(data)