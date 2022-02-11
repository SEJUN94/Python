from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

#html = urlopen("http://127.0.0.1:5000/memberlist")

tet = requests.get("http://127.0.0.1:5000/memberlist")
#print(tet.text)
print("---------------------------------------------------------------------------------------")

soup = BeautifulSoup(tet.text, "html.parser")

#print(soup) #웹 문서 전체가 출력됩니다.

mytable = soup.find_all("table")[0]
trs = mytable.find_all("tr")
for idx,i in enumerate(trs):
    if idx > 0:
        tds = i.find_all("td")
        print(tds[0].get_text(),end="\t")
        print(tds[1].get_text(),end="\t")
        print(tds[2].get_text())
