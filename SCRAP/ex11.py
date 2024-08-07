import requests
from bs4 import BeautifulSoup
import re

query='재현'
url='https://www.google.com/search?q={}&sca_esv=0938baf10882972d&udm=2&biw=1920&bih=953&sxsrf=ADLYWIKTpc--Ns14KRfb6lTslBhtYQO8Zw%3A1722991594620&ei=6sOyZsjJJZeMvr0Pz6zfuQU&ved=0ahUKEwjI5srv0-GHAxUXhq8BHU_WN1cQ4dUDCBE&uact=5&oq=%EC%9E%AC%ED%98%84&gs_lp=Egxnd3Mtd2l6LXNlcnAiBuyerO2YhDIEECMYJzIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEiAB1AAWLYDcAF4AJABAZgBYKABzAOqAQE1uAEDyAEA-AEBmAIEoAK5AsICCBAAGIAEGLEDmAMAkgcDMi4yoAeuGQ&sclient=gws-wiz-serp'.format(query)
headers={
  "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
  "Accept-Language":"ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"
  }
res=requests.get(url,headers=headers)
soup=BeautifulSoup(res.text,'lxml')

print(res.text)
with open('data/image.html','w',encoding='utf-8')as file:
  file.write(soup.prettify())
  
es=soup.find_all('div',attrs={'class':re.compile('^eA0Zlc')})
print(len(es))
for index, e in enumerate(es):
  title = e.find('div',attrs={'class':'toI8Rb OSrXXb'})
  image=e.find('img')['src']
  
  print(index+1,title.get_text())
  print(image)
  print('-'*50)