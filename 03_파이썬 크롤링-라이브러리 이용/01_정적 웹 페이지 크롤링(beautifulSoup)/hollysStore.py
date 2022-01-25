# -*- coding: euc-kr -*-
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

result = []

for page in range(1,55):
	Hollys_url = "https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=%d&sido=&gugun=&store=" % (page)
	## print(Hollys_url)

	html = urllib.request.urlopen(Hollys_url)
	soupHollys = BeautifulSoup(html, 'html.parser')
	tag_tbody = soupHollys.find('tbody')

	for store in tag_tbody.find_all('tr'):
		if len(store) <= 3:
			break
		store_td = store.find_all('td')
		store_name = store_td[1].string
		store_local = store_td[0].string
		store_address = store_td[3].string
		store_phone = store_td[5].string
		# print([store_name] + [store_local] + [store_address] + [store_phone])
		result.append([store_name] + [store_local] + [store_address] + [store_phone])

columns = ['Name', 'Local', 'Address', 'Phone']
df = pd.DataFrame(result, columns = columns)
## print(df)
df.to_csv('./전국 할리스커피 매장 상세 정보.csv', encoding='euc-kr', mode='w', index=True)