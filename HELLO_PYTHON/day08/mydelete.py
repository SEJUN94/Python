import pymysql

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='python', db='python', port=3305, charset='utf8')
# Connection 으로부터 Cursor 생성    
curs = conn.cursor()

# SQL문 실행
e_id = 6
sql = f"""
DELETE FROM emp 
WHERE e_id = '{e_id}';
"""

cnt = curs.execute(sql)
conn.commit()

if cnt == 1:
    print("성공적으로 처리하였습니다.")
else:
    print("실패하였습니다.")


curs.close()
conn.close()