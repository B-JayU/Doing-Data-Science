# -*- coding: euc-kr -*-
from bs4 import BeautifulSoup

html = '<h1 id="title">�Ѻ����ǳ�Ʈ��ũ</h1><div class="top"><ul class="menu"><li><a href="http://www.hanbit.co.kr/member/login.html" class="login">�α���</a></li></ul><ul class="brand"><li><a href="http://www.hanbit.co.kr/media/">�Ѻ��̵��</a></li><li><a href="http://www.hanbit.co.kr/academy/">�Ѻ���ī����</a></li></ul></div>'
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
print(tag_a.attrs) # tag_a�� ������ �Ӽ��̸� ���� �з��Ͽ� ��ųʸ� ���·� ���
print(tag_a['href'])
print(tag_a['class'])
'''

tag_ul_2 = soup.find('ul', attrs={'class' : 'brand'})
print(tag_ul_2)

li_list = soup.select("div>ul.brand>li")
for li in li_list:
	print(li.string)


