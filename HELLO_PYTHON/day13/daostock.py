import pymysql
class DaoStock1:
    def __init__(self):
        print("DaoStock:init")
        # MySQL Connection 연결
        self.conn = pymysql.connect(host='localhost', user='root', 
                                    password='python', db='python', port=3305, charset='utf8')
        # Connection 으로부터 Cursor 생성    
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
    
    
    def myselect(self,s_name):
        # SQL문 실행
        sql = f"""
        select 
            s_code,
            s_name,
            price,
            ymd_hm
        from
            stock
        where 
            s_name = '{s_name}'
        """
        self.curs.execute(sql)
        # 데이터 Fetch
        mylist = self.curs.fetchall()
        return mylist

    
    def myprices(self,s_name):
        ret=[]
        # SQL문 실행
        sql = f"""
        select 
            s_code,
            s_name,
            price,
            ymd_hm
        from
            stock
        where 
            s_name = '{s_name}'
        order by ymd_hm
        """
        self.curs.execute(sql)
        mylist = self.curs.fetchall()
        for p in mylist:
            ret.append(p['price'])
        return ret

    
    def mys_names(self):
        # SQL문 실행
        sql = f"""
        select 
            s_name
        from
            stock
        group by s_name
        """
        self.curs.execute(sql)
        # 데이터 Fetch
        mylist = self.curs.fetchall()
        return mylist

    

    def __del__(self):
        print("DaoStock:del")
        self.curs.close()
        self.conn.close()
        
        
        
if __name__=='__main__':
    a=[]
    b=[]
    ds = DaoStock1()
    mylist = ds.myselect('삼성전자')
    mylist1 = ds.mys_names()
    for n in mylist1:
        s_name = n['s_name']
        prices = ds.myprices(s_name)
        a.append(s_name)
        b.append(prices)
        
    print(a)
    print(b)