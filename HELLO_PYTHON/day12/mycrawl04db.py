from bs4 import BeautifulSoup
import requests
from day12.daostock import DaoStock
from datetime import datetime

ds = DaoStock()

ymd_hm = datetime.now().strftime("%Y%m%d_%H%M")
mysrc = requests.get("https://vip.mk.co.kr/newSt/rate/item_all.php")
mysrc.encoding='euc-kr'
soup = BeautifulSoup(mysrc.text, 'html.parser')
sts = soup.select(".st2")

for idx,st2 in enumerate(sts):
    myparent = st2.parent
    tds = myparent.select("td")
    s_name = tds[0].text
    s_code = tds[0].a['title']
    price = tds[1].text.replace(",","")
    cnt = ds.myinsert(s_code, s_name, price, ymd_hm)
    print(idx,s_name,s_code,price,ymd_hm)

    

