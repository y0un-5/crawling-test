# 파일명 : crawl_test2.py

import requests
from bs4 import BeautifulSoup

response = requests.get("http://192.168.0.155/table.html")
response.headers['Content-Type']
text = response.text
html = BeautifulSoup(text, 'html.parser')
tr_list = html.find("tbody").find_all("tr")
for tr in tr_list:
	td_list = tr.find_all("td")
	row = []
	for td in td_list:
		row.append(td.text)
	print(row)