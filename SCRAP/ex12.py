from selenium import webdriver
import time
options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
browser=webdriver.Chrome(options=options)
browser.maximize_window()

query='재현'
url='https://www.google.com/search?q={}&sca_esv=0938baf10882972d\
  &udm=2&biw=1920&bih=953&sxsrf=ADLYWIKTpc--Ns14KRfb6lTslBhtYQO8Zw%3A1722991594620\
  &ei=6sOyZsjJJZeMvr0Pz6zfuQU&ved=0ahUKEwjI5srv0-GHAxUXhq8BHU_WN1cQ4dUDCBE&uact=5&oq=%EC%9E%AC%ED%98%84\
  &gs_lp=Egxnd3Mtd2l6LXNlcnAiBuyerO2YhDIEECMYJzIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEiAB1AAWLYDcAF4AJABAZgBYKABzAOqAQE1uAEDyAEA-AEBmAIEoAK5AsICCBAAGIAEGLEDmAMAkgcDMi4yoAeuGQ&sclient=gws-wiz-serp'.format(query)
browser.get(url)

prev_height = browser.execute_script('return document.body.scrollHeight')
while True:
  browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
  time.sleep(2)
  curr_height = browser.execute_script('return document.body.scrollHeight')
  if prev_height == curr_height:
    print('스크롤완료!')
    break
  prev_height = curr_height

from bs4 import BeautifulSoup
import re
soup = BeautifulSoup(browser.page_source, 'lxml')

with open('data/image.html', 'w', encoding='utf-8') as file:
  file.write(soup.prettify())

es = soup.find_all('div', attrs={'class':re.compile('^eA0Zlc')})
print(len(es))
for index, e in enumerate(es):
  title = e.find('div', attrs={'class':'toI8Rb OSrXXb'})
  image = e.find('img')['src']
  print(index+1, title.get_text())
  print(image)
  print('-' * 50)