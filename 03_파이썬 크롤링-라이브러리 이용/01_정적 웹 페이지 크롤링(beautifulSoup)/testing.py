# -*- coding: euc-kr -*- 
from bs4 import BeautifulSoup

html = '<h1 id="title">�Ѻ����ǳ�Ʈ��ũ</h1><div class="top"><ul class="menu"><li><a href="http://www.hanbit.co.kr/member/login.html" class="login">�α���</a></li></ul><ul class="brand"><li><a href="http://www.hanbit.co.kr/media/">�Ѻ��̵��</a></li><li><a href="http://www.hanbit.co.kr/academy/">�Ѻ���ī����</a></li></ul></div>'

soup = BeautifulSoup(html, 'html.parser')

print(soup)

