import pymysql
class DaoEmp:
    def __init__(self):
        # MySQL Connection 연결
        self.conn = pymysql.connect(host='localhost', user='root', 
                                    password='python', db='python', port=3305, charset='utf8')
        # Connection 으로부터 Cursor 생성    
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
    
    
    def myselect(self):
        # SQL문 실행
        sql = """
        select 
            e_id,
            e_name,
            sex,
            age
        from
             emp
        """
        self.curs.execute(sql)
        # 데이터 Fetch
        mylist = self.curs.fetchall()
        return mylist
        
        
    def myinsert(self,e_name,sex,age):
        # e_name = 999
        # sex = 1
        # age = 999
        sql = f"""
        insert into 
        emp(e_name, sex, age) 
        VALUES ('{e_name}', '{sex}', {age});
        """
        self.cnt = self.curs.execute(sql)
        self.conn.commit()
        return self.cnt
    
    
    def myupdate(self,e_id,e_name,sex,age):
        sql = f"""
        update emp
        set
            e_name ='{e_name}',
            sex = '{sex}',
            age = '{age}'
        WHERE 
            e_id = '{e_id}';
        """
        self.cnt = self.curs.execute(sql)
        self.conn.commit()
        
        if self.cnt == 1:
            print("성공적으로 처리하였습니다.")
        else:
            print("실패하였습니다.")
          
            
    def mydelete(self,e_id):
        sql = f"""
        delete 
        from 
             emp
        where e_id='{e_id}'
        """
    
        self.cnt = self.curs.execute(sql)
        self.conn.commit()
        
        if self.cnt == 1:
            print("성공적으로 처리하였습니다.")
        else:
            print("실패하였습니다.")
        
        
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
        
if __name__=='__main__':
    de = DaoEmp()
    mylist = de.myselect()
    # myinsert = de.myinsert(9,9,9)
    # myupdate = de.myupdate(9, 9, 9, 9)
    # de.mydelete(10)
    print(mylist)