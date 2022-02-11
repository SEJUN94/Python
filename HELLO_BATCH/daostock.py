import pymysql
class DaoStock:
    def __init__(self):
        print("DaoStock:init")
        # MySQL Connection 연결
        self.conn = pymysql.connect(host='localhost', user='root', 
                                    password='python', db='python', port=3305, charset='utf8')
        # Connection 으로부터 Cursor 생성    
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
        
    def myselect(self):
        #SQL문 실행
        sql= """
        select * from stock
        """
        self.curs.execute(sql)
        #데이터 Fetch
        mylist = self.curs.fetchall()
        return mylist    
    
    
        
    def myinsert(self,s_code,s_name,price,ymd_hm):
        #SQL문 실행
        sql= f"""
        insert into stock(s_code, s_name, price, ymd_hm)
        values('{s_code}','{s_name}','{price}', '{ymd_hm}');
        """
        self.cnt = self.curs.execute(sql)
        self.conn.commit()
        return self.cnt
    
        if self.cnt == 1:
            print("성공적으로 추가되었습니다.")
        else:
            print("실패하였습니다.")   
    
    
    def __del__(self):
        print("DaoStock:del")
        self.curs.close()
        self.conn.close()
    
        
if __name__=='__main__':
    ds = DaoStock()
    cnt = ds.myinsert('1', '1', '1', '1')
    print("cnt",cnt)
    
