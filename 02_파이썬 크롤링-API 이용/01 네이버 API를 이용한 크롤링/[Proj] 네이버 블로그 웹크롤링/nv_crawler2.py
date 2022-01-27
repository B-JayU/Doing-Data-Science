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
	
	# ���� url request ��û�ϴ� �ܰ�
	req = urllib.request.Request(url)
	
	# header �߰��ϱ� ( client ID, Secret )
	req.add_header("X-Naver-Client-Id", client_id)
	req.add_header("X-Naver-Client-Secret", client_secret)

	try:
        	## context�� ������???
		## context = ssl._create_unverified_context()
        	## urlopen()�� context ���� ssl ��ü�� �־��־�� ��.
		context = ssl._create_unverified_context()
		response = urllib.request.urlopen(req, context=context)

		if response.getcode() == 200:
			print("[%s] Url Request success" % datetime.datetime.now())
			return response.read().decode('utf-8')
            		## .read() : �޾ƿ� �����͸� ����Ʈ������ ��ȯ 
            		## -> .decode('utf-8') : �̸� 'utf-8'�� ��ȯ

	except Exception as e:
        ## ����ó��  : ���������� ����ϰ�, �α� ���
		print(e)
		print("[%s] Error for URL : %s" %(datetime.datetime.now(), url))
		return None


def getNaverSearch(node, srcText, start, display):
	
   	## url�� �����ϴ� �ܰ�
	base = "https://openapi.naver.com/v1/search"
	node = "/%s.json" % node
	parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(srcText), start, display)
	url = base + node + parameters

	## url ��û
	responseDecode = getRequestUrl(url)

	if (responseDecode == None):
		return None
	else:
		return json.loads(responseDecode)

def getPostData(post, jsonResult, cnt):

	# json ���Ͽ� �߰��� items�� attribute
	title = post['title']
	description = post['description']
	blogger_link = post['bloggerlink']
	link = post['link']

	# %Y : ��ü ����
	# %m : �ش� �⵵�� ���ڷ� ǥ���� �� (0���� �е�)
	# %d : �ش� ���� ���� (0���� �е�)
	# [��¥ ������ ���� �Ľ��ϱ�] https://hbase.tistory.com/103
	pDate = datetime.datetime.strptime(post['postdate'], '%Y%m%d')
	pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

	# jsonResult(list)��  dictionary ������ �����͸� ����
	# jsonResult �� dictionary ������ �����͸� ���ҷ� ���� ����Ʈ ��ü
	jsonResult.append({'cnt':cnt, 'title':title, 'description':description, 'blogger_link' : blogger_link, 'link' : link})

	return

def main():
	
	node = 'blog'
	srcText = input("�˻�� �Է��ϼ��� : ")
	cnt = 0
	jsonResult = []

    	## ���̹� openapi�� ���� jsonResponse �޾ƿ���
	jsonResponse = getNaverSearch(node, srcText, 1, 100)
	## �ѹ��� 100���� ������ �о����
	total = jsonResponse['total']

	# jsonResponse ������ �������̰�, read�� ������ ������ �����ϴ� ���, �ݺ����� ����
	while((jsonResponse != None) and (jsonResponse['display'] != 0)):
		for post in jsonResponse['items']:
			# jsonResponse['itmes'] �� �ִ� �׸���� �ϳ��� post �� �о ó��
			cnt += 1
			# jsonResponse['items'] �� �ִ� ����׸��� jsonResult ����Ʈ��ü�� �����ϱ�
			getPostData(post, jsonResult, cnt)
		
		## ���� 100���� �����͸� �о���̱�
		start = jsonResponse['start'] + jsonResponse['display']
		## start�� �������Ͽ� �ݺ� ����
		jsonResponse = getNaverSearch(node, srcText, start, 100)
	
	# ��ü �˻� ��� Ȯ���ϱ�
	print("��ü �˻� : %d ��" %total)

	# ���̽� ���� ���
	with open('%s_naver_%s.json' % (srcText, node), 'w', encoding="utf-8") as outfile:
		jsonFile = json.dumps(jsonResult, indent=4, sort_keys = True, ensure_ascii = False)
		outfile.write(jsonFile)
	
	print("������ ������ : %d ��" %(cnt))
	print('%s_naver_%s.json SAVED' % (srcText, node))

if __name__ == "__main__" :
	main()