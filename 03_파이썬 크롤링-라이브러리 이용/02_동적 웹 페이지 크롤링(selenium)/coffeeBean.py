# -*- coding: euc-kr -*-
from bs4 import BeautifulSoup
from selenium import webdriver

import urllib.request
import pandas as pd
import datetime
import time

def CoffeeBean_store(result):
	
	# url �����ϰ� ���� ������̹��� ���� get
	response_url = "https://www.coffeebeankorea.com/store/store.asp"
	wd = webdriver.Chrome('./webDriver/chromedriver')
		
	for store in range(1,51):
		wd.get(response_url)
		time.sleep(1)
		try:
			wd.execute_script("storePop2(%d)" %store)
			time.sleep(1)
			html = wd.page_source

			soupCB2 = BeautifulSoup(html, 'html.parser')

			store_name_h2 = soupCB2.select("div.store_txt > h2")
			print(store_name_h2)
			store_name = store_name_h2[0].string
			print(store_name)

			store_info = soupCB2.select("div.store_txt > table.store_table > tbody > tr > td")
			store_address_list = list(store_info[2])
			store_address = store_address_list[0]

			store_phone = store_info[3].string

			result.append([store_name] + [store_address] + [store_phone])
		except:
			continue
	return

def main():
	result = []
	print("coffeebean store crawling")
	CoffeeBean_store(result)

	df = pd.DataFrame(result, columns = ('Store', 'Address', 'Phone'))
	df.to_csv("./���� 500�� Ŀ�Ǻ� ���� ��Ȳ.csv", encoding="euc-kr", mode = 'w', index=True)

if __name__ == '__main__':
	main()

