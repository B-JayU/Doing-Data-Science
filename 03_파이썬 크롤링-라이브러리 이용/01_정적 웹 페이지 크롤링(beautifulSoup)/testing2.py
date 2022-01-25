# -*- coding: euc-kr -*-
from bs4 import BeautifulSoup

html = '<h1 id="title">한빛출판네트워크</h1><div class="top"><ul class="menu"><li><a href="http://www.hanbit.co.kr/member/login.html" class="login">로그인</a></li></ul><ul class="brand"><li><a href="http://www.hanbit.co.kr/media/">한빛미디어</a></li><li><a href="http://www.hanbit.co.kr/academy/">한빛아카데미</a></li></ul></div>'
soup = BeautifulSoup(html, 'html.parser')

tag_h1 = soup.h1
tag_div = soup.div
tag_ul = soup.ul
tag_li = soup.li
tag_a = soup.a

# print(tag_h1, tag_div, tag_ul, tag_li, tag_a)

'''
print(soup.find_all('ul'))
print(soup.find_all('li'))
print(soup.find_all('a'))
'''

'''
print(tag_a.attrs) # tag_a의 내용을 속성이름 별로 분류하여 딕셔너리 형태로 출력
print(tag_a['href'])
print(tag_a['class'])
'''

tag_ul_2 = soup.find('ul', attrs={'class' : 'brand'})
print(tag_ul_2)

li_list = soup.select("div>ul.brand>li")
for li in li_list:
	print(li.string)


