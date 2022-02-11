from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

#html = urlopen("http://127.0.0.1:5000/memberlist")

mysrc = requests.get("http://127.0.0.1:5000/memberlist")
soup = BeautifulSoup(mysrc.text, 'html.parser')
print(mysrc.text)
print("---------------------------------------------------------------------------------------")
mytable = soup.select("table")[0]
trs = mytable.select("tr")
for idx,tr in enumerate(trs):
    if idx>0:
        td4 = tr.select("td")
        print(td4[0].get_text(),td4[1].get_text(),td4[2].text,td4[3].text)