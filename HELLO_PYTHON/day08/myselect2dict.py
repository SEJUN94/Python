import pymysql

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='python', db='python', port=3305, charset='utf8')
# Connection 으로부터 Cursor 생성    
curs = conn.cursor(pymysql.cursors.DictCursor)

# SQL문 실행
sql = 'select * from emp'
curs.execute(sql)

# 데이터 Fetch
rows = curs.fetchall()
print(rows)

curs.close()
conn.close()