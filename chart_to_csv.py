# -*- encoding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

import csv

url = "https://music.bugs.co.kr/chart"

response = requests.get(url)
response.headers['Content-Type']

text = response.text
html = BeautifulSoup(text, 'html.parser')

tr_list = html.find("table", {"class":"list"}).find("tbody").find_all("tr")
len(tr_list)

rankings = []
for tr in tr_list:
    ranking = tr.find("div", {"class":"ranking"}).find("strong").text.strip()
    rankings.append(ranking)
print(rankings)

songs = []
for tr in tr_list:
    song = tr.find("p", {"class":"title"}).text.strip()
    songs.append(song)
print(songs)

artists = []
for tr in tr_list:
    artist = tr.find("p", {"class":"artist"}).find("a").text.strip()
    artists.append(artist)
print(artists)

albums = []
for tr in tr_list:
    album = tr.find("a", {"class":"album"}).text.strip()
    albums.append(album)
print(albums)

total_ranks = []
for x, y, z, a in zip(rankings, songs, artists, albums):
    total_rank = [x, y, z, a]
    total_ranks.append(total_rank)
    print(x, y, z, a)
print(total_ranks)

columns = ["랭킹", "제목", "가수", "앨범"]
wfile = open("total_rank.csv", "w", newline="", encoding="UTF-8-sig")
csvfile = csv.writer(wfile)
csvfile.writerow(columns)
csvfile.writerows(total_ranks)
wfile.close()