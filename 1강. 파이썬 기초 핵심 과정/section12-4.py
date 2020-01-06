# section12-4
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 조회

import sqlite3

# DB파일 조회(없으면 새로 생성)
conn = sqlite3.connect('C:/python_basic/resource/database.db') # 본인 DB 경로

# 커서 바인딩

c = conn.cursor()

# 데이터 조회(전체)
c.execute("SELECT * FROM users")

# 커서 위치가 변경 >> 실행한 다음 커서가 이동한다. 마지막 데이터 이후에 없으면 none을 리턴
# 1개 로우 선택
# print('One -> \n', c.fetchone())

# 지정 로우 선택
# print("Three -> \n", c.fetchmany(size=3)) 

# 전체 로우 선택
# print('All -> \n', c.fetchall()) #5번 이후에는 데이터가 없기 때문에 1개만 출력

print()
# 커서가 읽어올 위치에 따라 데이터를 읽어오기 때문에 중요!

# 순회1
# rows = c.fetchall()
# for row in rows:
#     print('retrieve1 >', row) 

# 순회2 >> 이게 가장 많이 사용 
for row in c.fetchall(): 
    print('retrieve2 >', row) 

# # 순회3
# for row in c.execute('SELECT * FROM users ORDER BY id desc'):
#     print('retrieve3 >', row) 

print()

# WHERE Retrieve1(where 조건 6가지)

# ?로 되있는것을 튜플로 만든다음 문장에 넣었다 
param1 = (3, ) #튜플형태로 입력 받았다
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1', c.fetchone())
print('param1', c.fetchall()) #커서가 다음 나올 위치를 기억하고 있는데 튜플이 빈 값이어서 데이터 없음 

# WHERE Retrieve2
param2 = 2
c.execute('SELECT * FROM users WHERE id="%s"' % param2)
print('param2', c.fetchone())
print('param2', c.fetchall()) #커서가 다음 나올 위치를 기억하고 있는데 튜플이 빈 값이어서 데이터 없음 

# WHERE Retrieve3 // 딕셔너리 이용
param3 = 2
c.execute('SELECT * FROM users WHERE id=:Id', {"Id": 5})
print('param3', c.fetchone())
print('param3', c.fetchall()) #커서가 다음 나올 위치를 기억하고 있는데 튜플이 빈 값이어서 데이터 없음 

# WHERE Retrieve4
param4 = (3,5)
c.execute("SELECT * FROM users WHERE id IN(?,?)", param4)
print('param4', c.fetchall())

# WHERE Retrieve5
c.execute("SELECT * FROM users WHERE id IN('%d, %d')" % (3,4))
print('param5', c.fetchall())

# WHERE Retrieve6
c.execute("SELECT * FROM users WHERE id IN('%d, %d')" % (3,4))
print('param5', c.fetchall())

# WHERE Retrieve7 // 딕셔너리 형태
c.execute("SELECT * FROM users WHERE id=:id1 OR id=:id2", {"id1": 2, "id2": 5})
print('param6', c.fetchall())

# dump (SQlite를 백업) 출력
with conn:
    with open('C:/python_basic/resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete')

