# -*- encoding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from time import sleep
import csv


def FindNaverStock(code, ran, slptime):
    page = 1
    rows = []
    for page in range(1, ran):
        msg = f"\r 진행률 {page * 10}%"
        print(msg,end='')

        url = f"https://finance.naver.com/item/sise_day.nhn?code={code}&page={page}"
        response = requests.get(url, headers = {"User-Agent":"Mozilla/5.0"})

        text = response.text
        html = BeautifulSoup(text, 'html.parser')

        tr_list = html.find("table").find_all("tr", {"onmouseover":"mouseOver(this)"})

        for i in range(0, 10):
            tr = tr_list[i]
            td_list = tr.find_all("td")
            del td_list[2]
            row = []

            for td in td_list:
                text = td.find("span").text
                row.append(text)

            for i in range(1, len(row)):
                row[i] = int(row[i].replace(',',''))
            rows.append(row)
    sleep(slptime)
    return rows

def load_DB():
    import csv
    rfile = open("data_3949_20210218.csv", "r")
    datas = csv.reader(rfile)
    stock_datas = []
    for data in datas:
        com_code = data[0]
        com_name = data[1]
        sub_code = data[5]
        sub_name = data[6]
        ceo = data[13]
        com_phone = data[14]
        com_addr = data[15]
        data = [com_code, com_name, sub_code, sub_name, ceo, com_phone, com_addr]
        stock_datas.append(data)
    
    return stock_datas

def search_result(rows, name):
    rows = rows
    show_rows = []
    cnt = 0

    for row in rows:
        if name in row[1]:
            show_rows.append(row)

    for row in show_rows:
        cnt += 1
        print("순    서: " + str(cnt))
        print("종목코드: "+ row[0])
        print("업 체 명: "+ row[1])
        print("종 목 명: "+ row[3] + "\n")
        #print("연 락 처: "+ row[5] + "\n")
    
    num = int(input("선택번호: "))
    return show_rows[num -1][0]


#code = input("종목코드: ")
#ran = int(input("검색범위: "))
#time = int(input("시간차이: "))

#rows = FindNaverStock(code, ran, time)

"""
columns = ["날짜", "종가", "시가", "고가", "저가", "거래량"]
wfile = open(f"naver_{code}_stock.csv", "w", newline="", encoding="UTF-8-sig")
csvfile = csv.writer(wfile)
csvfile.writerow(columns)
csvfile.writerows(rows)
wfile.close()
"""