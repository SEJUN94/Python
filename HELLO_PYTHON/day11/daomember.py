import pymysql

class DaoMember:
    def __init__(self):
        print("DaoMember:init")
        # MySQL Connection 연결
        self.conn = pymysql.connect(host='localhost', user='root', 
                                    password='python', db='python', port=3305, charset='utf8')
        # Connection 으로부터 Cursor 생성    
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def myselect(self):
        #SQL문 실행
        sql= """
        select * from member
        """
        self.curs.execute(sql)
        #데이터 Fetch
        mylist = self.curs.fetchall()
        return mylist
    
    def myinsert(self,m_name,tel,addr):
        #SQL문 실행
        sql= f"""
        insert into member(m_name, tel, addr)
        values('{m_name}','{tel}','{addr}');
        """
        self.cnt = self.curs.execute(sql)
        self.conn.commit()
        return self.cnt
    
        if self.cnt == 1:
            print("성공적으로 추가되었습니다.")
        else:
            print("실패하였습니다.")
            
    def myupdate(self,m_id,m_name,tel,addr):
        sql = f"""
        update member
        set
            m_name ='{m_name}',
            tel = '{tel}',
            addr = '{addr}'
        WHERE 
            m_id = '{m_id}';
        """
        self.cnt = self.curs.execute(sql)
        self.conn.commit()
        return self.cnt
        
        if self.cnt == 1:
            print("성공적으로 처리하였습니다.")
        else:
            print("실패하였습니다.")
            
    
    def mydelete(self,m_id):
        sql= f"""
        delete from member
        where m_id ='{m_id}'
        """
        
        self.cnt = self.curs.execute(sql)
        self.conn.commit()

        if self.cnt == 1:
            print("성공적으로 처리하였습니다.")
        else:
            print("실패하였습니다.")
    
        return self.cnt
            
    def __del__(self):
        print("DaoMember:del")
        self.curs.close()
        self.conn.close()
    
        
if __name__=='__main__':
    de = DaoMember()
    mylist = de.myselect()
    print(mylist)