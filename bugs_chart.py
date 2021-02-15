# 파일명 : bugs_chart.py
# 벅스 음원 차트 크롤링 연습

import requests
from bs4 import BeautifulSoup

url = "https://music.bugs.co.kr/chart"

response = requests.get(url)
response.headers['Content-Type']
text = response.text
html = BeautifulSoup(text, 'html.parser')

tr_list = html.find("article").find("section").find("tbody").find_all("tr")
len(tr_list)

songs = []
for tr in tr_list:
    song = tr.find("p", {"class":"title"}).text.strip()
    songs.append(song)
print(songs)