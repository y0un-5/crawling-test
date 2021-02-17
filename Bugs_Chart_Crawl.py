# -*- encoding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import urllib.request
import csv
import os
import re
import calendar
from time import sleep
# 필요한 모듈 import

def makefolder(date):
    path = f".\{date}"
    os.mkdir(path)
    imgpath = f".\{date}\img"
    os.mkdir(imgpath)
    return date
# 폴더 생성 함수
# 크롤링 데이터를 저장할 폴더 생성 (20200210)

def makeparse(url):
    response = requests.get(url)
    response.headers['Content-Type']
    text = response.text
    html = BeautifulSoup(text, 'html.parser')
    # txt 타입 콘텐츠 -> html parser 사용

    tr_list = html.find("table", {"class":"list"}).find("tbody").find_all("tr")
    len(tr_list)
    # tr_list까지 parsing

    return tr_list


date = input("검색 할 날짜:[YYYYMMDD]: ")


"""
for year in range(2019, 2021):
    for month in range(1, 13):
        drange = calendar.monthrange(year, month)[1] + 1
        for day in range(1, drange):
            date = f'{year}' + f'{month:02}' + f'{day:02}'
            print(date)
            sleep(5)
"""

# 날짜 입력 부분 (20200210)
makefolder(date)
# 폴더 생성 함수 사용
url = f"https://music.bugs.co.kr/chart/track/realtime/total?chartdate={date}"
# Bugs 음원 순위 사이트 url + 20200210
tr_list = makeparse(url)

rankings = []
for tr in tr_list:
    ranking = tr.find("div", {"class":"ranking"}).find("strong").text.strip()
    rankings.append(ranking)
#print(rankings)
# 랭킹 크롤링

songs = []
for tr in tr_list:
    song = tr.find("p", {"class":"title"}).text.strip()
    songs.append(song)
#print(songs)
# 제목 크롤링

artists = []
for tr in tr_list:
    artist = tr.find("p", {"class":"artist"}).find("a").text.strip()
    artists.append(artist)
#print(artists)
# 가수 크롤링

albums = []
for tr in tr_list:
    try:
        album = tr.find("a", {"class":"album"}).text.strip()
        albums.append(album)
    except:
        album = tr.find("span", {"class":"album"}).text.strip()
        albums.append(album)
#print(albums)
# 앨범명 크롤링 + 에러 처리

total_ranks = []
for x, y, z, a in zip(rankings, songs, artists, albums):
    total_rank = [x, y, z, a]
    total_ranks.append(total_rank)
    #print(x, y, z, a)
#print(total_ranks)
# 크롤링한 랭킹, 제목, 가수, 앨범명 리스트 저장

columns = ["랭킹", "제목", "가수", "앨범"]
wfile = open(f"{date}/total_rank.csv", "w", newline="", encoding="UTF-8-sig")
csvfile = csv.writer(wfile)
csvfile.writerow(columns)
csvfile.writerows(total_ranks)
wfile.close()

# 20200210/total_rank.csv 파일로 저장
# 한글은 utf-8-sig로 설정해야 엑셀에서 정상적으로 볼 수 있다.
# 폴더는 위에서 생성한 20200210 폴더를 사용한다.

imgs = []
cnt = 0
for tr in tr_list:
    msg = f"\r 진행률 {cnt+1}%"
    print(msg,end='')
    try:
        img = tr.find("a", {"class":"thumbnail"}).find("img").get("src").replace('/50/', '/original/').split("?")[0]
        imgname = str(rankings[cnt]) + "_" + str(songs[cnt])
        imgname = re.sub('[-=.#/?:$\\n\\}]', '', imgname) + ".jpg"
        cnt += 1
        urllib.request.urlretrieve(img, f"{date}\img\\"+ imgname)
        imgs.append(img)
    except:
        img = tr.find("a", {"class":"thumbnail"}).find("img").get("src").replace('/50/', '/original/').split("?")[0]
        imgname = str(rankings[cnt+1]) + "_" + str(songs[cnt+1])
        imgname = re.sub('[-=.#/[?:$\\n\\}]', '', imgname) + ".jpg"
        cnt += 1
        urllib.request.urlretrieve(img, f"{date}\img\\"+ imgname)
        imgs.append(img)
imgs

print("\nFinished")

"""
# 이미지 파일 저장 및 에러처리
# tumbnail에서 img src를 가져오며, 저장은 20200210/img/에 저장된다. 

"""