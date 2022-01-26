# -*- coding: euc-kr -*-
from bs4 import BeautifulSoup
from selenium import webdriver
import time

wd = webdriver.Chrome('./webDriver/chromedriver')
wd.get("https://www.coffeebeankorea.com/store/store.asp")
wd.execute_script("storePop2(1)")

time.sleep(10)
html = wd.page_source
# print("html 출력 : ", html)
soupCB1 = BeautifulSoup(html, 'html.parser')
# print(soupCB1.prettify())

# 매장 이름 정보
store_name_h2 = soupCB1.select("div.store_txt>h2")
store_name = store_name_h2[0].string
print("매장 이름정보 : ", store_name)

store_info = soupCB1.select("div.store_txt > table.store_table > tbody > tr > td")

## 매장 주소 정보
store_address_list = list(store_info[2])
store_address = store_address_list[0]
print("매장 위치정보 : ", store_address)

## 매장 전화 번호 
store_phone = store_info[3].string
print("매장 전화번호 : ", store_phone)