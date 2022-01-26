# -*- coding: euc-kr -*-
from bs4 import BeautifulSoup
from selenium import webdriver
import time

wd = webdriver.Chrome('./webDriver/chromedriver')
wd.get("https://www.coffeebeankorea.com/store/store.asp")
wd.execute_script("storePop2(1)")

time.sleep(10)
html = wd.page_source
# print("html ��� : ", html)
soupCB1 = BeautifulSoup(html, 'html.parser')
# print(soupCB1.prettify())

# ���� �̸� ����
store_name_h2 = soupCB1.select("div.store_txt>h2")
store_name = store_name_h2[0].string
print("���� �̸����� : ", store_name)

store_info = soupCB1.select("div.store_txt > table.store_table > tbody > tr > td")

## ���� �ּ� ����
store_address_list = list(store_info[2])
store_address = store_address_list[0]
print("���� ��ġ���� : ", store_address)

## ���� ��ȭ ��ȣ 
store_phone = store_info[3].string
print("���� ��ȭ��ȣ : ", store_phone)