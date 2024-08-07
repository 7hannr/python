from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
browser = webdriver.Chrome(options=options)
browser.maximize_window()

def wait_until(xpath):
  WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

browser.get('https://flight.naver.com/')
e = browser.find_element(By.XPATH, '//button[text()="가는 날"]')
e.click()

#이번달(28) 클릭
xpath = '//b[text()="28"]'
wait_until(xpath)
es = browser.find_elements(By.XPATH, xpath)
es[0].click()

xpath = '//b[text()="30"]'
wait_until(xpath)
es = browser.find_elements(By.XPATH, xpath)
es[0].click()

#도착버튼클릭
xpath = '//b[text()="도착"]'
wait_until(xpath)
e = browser.find_element(By.XPATH, xpath)
e.click()

#장소
xpath = '//button[text()="일본"]'
wait_until(xpath)
e = browser.find_element(By.XPATH, xpath)
e.click()

#공항
xpath = '//i[contains(text(),"TYO")]'
wait_until(xpath)
e = browser.find_element(By.XPATH, xpath)
e.click()

xpath = '//span[contains(text(), "검색")]'
wait_until(xpath)

#항공권검색
e = browser.find_element(By.XPATH, xpath)
e.click()

first = '//*[@id="__next"]/div/main/div[4]/div/div[2]/div[2]'
wait_until(first)

#검색목록
es = browser.find_element(By.CLASS_NAME,'domestic_Flight__8bR_b')
for e in es:
  print(e.text)
  print('-'*50)
print("전체검색수:",len(es))

browser.quit()