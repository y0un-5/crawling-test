# stockfind.py
# 종목 코드 검색
# 종목 코드, 종목명, 업종 코드, 업종명, 대표이사, 주소, 대표전화 출력

import naver_finance

db = naver_finance.load_DB()
name = input("회 사 명 : ")
print()
code = naver_finance.search_result(db, name)
rows = naver_finance.FindNaverStock(code, 10, 2)

for row in rows:
    print(row)