import bs4

file = open("index\index.html", "r")
read = file.read()
print(read)
type(read)

file = open("index\index.html", "r")
read = file.read()
html = bs4.BeautifulSoup(read, 'html.parser')
print(html)
type(html)
html.find_all("li")
html.find_all("li")[0]
li_list = html.find("ul").find_all("li")
for li in li_list:
    print(li.text)