# -*- coding: euc-kr -*-
from bs4 import BeautifulSoup
from selenium import webdriver

import urllib.request
import pandas as pd
import datetime
import time
import json


def KyochonChicken_store(result, jsonResult):
	
	store_name = []
	store_address = []
	store_phone = []

	total = 0

	base = "http://www.kyochon.com/shop/domestic.asp?sido1=1"
	for i in range(1,26):
		parameters = "&sido2=%s&txtsearch=" % i
		kyochon_url = base + parameters

		html = urllib.request.urlopen(kyochon_url)
		soupKyochon = BeautifulSoup(html, 'html.parser')
		
		store_name_list = soupKyochon.select('#section > div.shopSchList > ul.list > li > a > span > strong')		
		for s in store_name_list:
			name = s.string
			store_name.append(name)
			total = total + 1

		store_info_list =soupKyochon.select('#section > div.shopSchList > ul.list > li > a > span > em')
		for s in store_info_list:
			origin_addr = s.contents[0]
			origin_phone = s.contents[4]

			store_addr = origin_addr.strip()
			phone = origin_phone.strip()

			store_address.append(store_addr)
			store_phone.append(phone)
		
	

	for no in range(0,total):
		result.append([store_name[no]] + [store_address[no]] + [store_phone[no]])
		jsonResult.append({'name' : store_name[no], 'address' : store_address[no], 'phone' : store_phone[no]})


def main():
	
	# csv 파일 저장을 위한 리스트 객체
	result = []
	jsonResult = []
	 
	print("Kyochon chicken crawling")
	KyochonChicken_store(result, jsonResult)

	df = pd.DataFrame(result, columns = ('매장 이름', '매장 주소', '전화 번호'))
	df.to_csv('./교촌치킨_서울_매장 현황.csv', index=True, encoding="euc-kr", mode='w')

	with open('교촌치킨_서울_매장현황.json', 'w', encoding='utf-8') as outfile:
		jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii = False)
		outfile.write(jsonFile)

if __name__ == '__main__':
	main()


