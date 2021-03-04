# search_email.py

import requests, re
from bs4 import BeautifulSoup
from time import sleep

def extract_urls(domain):
   headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/70.0.3538.110"}
   url = fr"https://www.google.co.kr/search?q={domain}"
   response = requests.get(url, headers = headers)
   text = response.text
   html = BeautifulSoup(text, "html.parser")
   div_list = html.find_all("div", {"class":"g"})
   url_list = []
   for div in div_list:
      aurl = div.find("a").get("href")
      url_list.append(aurl)
   return url_list

def extract_email(url, concord = True):
    
    if concord:
        pattern = re.compile(rf"\b\w+@{domain}\b")
    else:
        pattern = re.compile(r"\b\w+@\w+([.]\w+)+\b")
    
    email_list = []
    
    try:
        response = requests.get(url)
    except:
        pass
    else:
        text = response.text
        matchs = pattern.finditer(text)
        for match in matchs:
            email_list.append(match.group(0))
    return email_list


domain = "kitri.re.kr"
url_list = extract_urls(domain)

email_lists = []
for url in url_list:
    email_list = extract_email(url, True)
    email_lists.extend(email_list)
    sleep(10)

print(email_lists)