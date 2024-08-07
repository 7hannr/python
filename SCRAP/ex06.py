import requests
from bs4 import BeautifulSoup
import re

def create_soup(query,page):
  url ='https://search.shopping.naver.com/search/all?query={}'.format(query)
  headers={
  "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
  "Accept-Language":"ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"
  }
  res = requests.get(url,headers=headers)
  soup = BeautifulSoup(res.text,'lxml')
  return soup

soup=create_soup('노트북')
content=soup.find('div',attrs={'id':'content'})
es=soup.find_all('div',attrs={'class':'adProduct_item__1zC9h'})
print(len(es))