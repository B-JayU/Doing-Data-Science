# -*- coding: euc-kr -*-
import os
import sys
import urllib.request
import urllib.parse

import datetime
import time
import json
import ssl

client_id = "AlVvydFSCIEnHdKcY7V9"
client_secret = "ogCxXsYGZg"

def getRequestUrl(url):
	
	# 실제 url request 요청하는 단계
	req = urllib.request.Request(url)
	
	# header 추가하기 ( client ID, Secret )
	req.add_header("X-Naver-Client-Id", client_id)
	req.add_header("X-Naver-Client-Secret", client_secret)

	try:
        	## context의 역할은???
		## context = ssl._create_unverified_context()
        	## urlopen()의 context 에는 ssl 객체를 넣어주어야 함.
		context = ssl._create_unverified_context()
		response = urllib.request.urlopen(req, context=context)

		if response.getcode() == 200:
			print("[%s] Url Request success" % datetime.datetime.now())
			return response.read().decode('utf-8')
            		## .read() : 받아온 데이터를 바이트형으로 반환 
            		## -> .decode('utf-8') : 이를 'utf-8'로 변환

	except Exception as e:
        ## 예외처리  : 오류사항을 출력하고, 로그 출력
		print(e)
		print("[%s] Error for URL : %s" %(datetime.datetime.now(), url))
		return None


def getNaverSearch(node, srcText, start, display):
	
   	## url을 구성하는 단계
	base = "https://openapi.naver.com/v1/search"
	node = "/%s.json" % node
	parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(srcText), start, display)
	url = base + node + parameters

	## url 요청
	responseDecode = getRequestUrl(url)

	if (responseDecode == None):
		return None
	else:
		return json.loads(responseDecode)

def getPostData(post, jsonResult, cnt):

	# json 파일에 추가할 items의 attribute
	title = post['title']
	description = post['description']
	blogger_link = post['bloggerlink']
	link = post['link']

	# %Y : 전체 연도
	# %m : 해당 년도의 숫자로 표현된 월 (0으로 패딩)
	# %d : 해당 월의 일자 (0으로 패딩)
	# [날짜 데이터 포맷 파싱하기] https://hbase.tistory.com/103
	pDate = datetime.datetime.strptime(post['postdate'], '%Y%m%d')
	pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

	# jsonResult(list)에  dictionary 형태의 데이터를 저장
	# jsonResult 는 dictionary 형태의 데이터를 원소로 갖는 리스트 객체
	jsonResult.append({'cnt':cnt, 'title':title, 'description':description, 'blogger_link' : blogger_link, 'link' : link})

	return

def main():
	
	node = 'blog'
	srcText = input("검색어를 입력하세요 : ")
	cnt = 0
	jsonResult = []

    	## 네이버 openapi로 부터 jsonResponse 받아오기
	jsonResponse = getNaverSearch(node, srcText, 1, 100)
	## 한번에 100개씩 데이터 읽어오기
	total = jsonResponse['total']

	# jsonResponse 응답이 정상적이고, read할 데이터 개수가 존재하는 경우, 반복문을 실행
	while((jsonResponse != None) and (jsonResponse['display'] != 0)):
		for post in jsonResponse['items']:
			# jsonResponse['itmes'] 에 있는 항목들을 하나씩 post 에 읽어서 처리
			cnt += 1
			# jsonResponse['items'] 에 있는 결과항목을 jsonResult 리스트객체에 저장하기
			getPostData(post, jsonResult, cnt)
		
		## 다음 100개의 데이터를 읽어들이기
		start = jsonResponse['start'] + jsonResponse['display']
		## start를 재지정하여 반복 시행
		jsonResponse = getNaverSearch(node, srcText, start, 100)
	
	# 전체 검색 결과 확인하기
	print("전체 검색 : %d 건" %total)

	# 파이썬 파일 출력
	with open('%s_naver_%s.json' % (srcText, node), 'w', encoding="utf-8") as outfile:
		jsonFile = json.dumps(jsonResult, indent=4, sort_keys = True, ensure_ascii = False)
		outfile.write(jsonFile)
	
	print("가져온 데이터 : %d 건" %(cnt))
	print('%s_naver_%s.json SAVED' % (srcText, node))

if __name__ == "__main__" :
	main()