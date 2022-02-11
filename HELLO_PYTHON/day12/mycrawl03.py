from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

#html = urlopen("http://127.0.0.1:5000/memberlist")

mysrc = requests.get("https://vip.mk.co.kr/newSt/rate/item_all.php")
mysrc.encoding='euc-kr'
#mysrc.encoding='ANSI'
soup = BeautifulSoup(mysrc.text, 'html.parser')
#print(mysrc.text)
print("---------------------------------------------------------------------------------------")
sts = soup.select(".st2")

for st2 in sts:
    myparent = st2.parent
    tds = myparent.select("td")
    s_name = tds[0].text
    s_code = tds[0].a['title']
    price = tds[1].get_text()
    print(s_name,s_code,price)
    
