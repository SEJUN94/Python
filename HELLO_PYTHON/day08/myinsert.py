import pymysql

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='python', db='python', port=3305, charset='utf8')
# Connection 으로부터 Cursor 생성    
curs = conn.cursor()

# SQL문 실행
sql = """INSERT INTO emp(e_id, e_name, sex, age) VALUES ('6', '6', '6', 6);"""

e_id = 7
e_name = 7
sex = 7
age = 7
sql = f"""insert into emp(e_id, e_name, sex, age) VALUES ('{e_id}', '{e_name}', '{sex}', {age});"""


cnt = curs.execute(sql)
conn.commit()

if cnt == 1:
    print("성공적으로 처리하였습니다.")
else:
    print("insert실패하였습니다.")


curs.close()
conn.close()