# Section12-1
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

import sqlite3
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now :', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)

# sqlite3
print('sqlite3.version: ', sqlite3.version) # 버젼확인
print('sqlite3.sqite_version:', sqlite3.sqlite_version)

# DB 생성 & auto commit(Rollback)
conn = sqlite3.connect('C:/python_basic/resource/database.db', isolation_level=None) # 데이터베이스 만들기

# Cursor
c = conn.cursor()
print('Cursor Type : ', type(c)) 


# 테이블 생성(Data Type: Text, Numeric, integer, real, blob)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, \
    phone text, website text, regdate text)")
    # 데이터베이스를 만들고 그 안에 테이블이 존재

# 데이터 삽입
c.execute("INSERT INTO users VALUES(1, 'Kim', 'Kim@naver.com', '010-0000-0000', 'Kim.com', ?)", (nowDatetime,)) #튜플 형태로 입력을 해주고 튜플형태로 넘겨줌
c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", (2, 'Park', 'Park@daum.net', '010-1111-1111', 'Park.com', nowDatetime)) # 원소의 갯수가 맞아야함

# Many 삽입(튜플, 리스트)!!! 
# 많은 데이터를 한번에 insert하는 방법을 알아야함
userList = (
    (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', nowDatetime),
    (4, 'Cho', 'Cho@daum.net', '010-3333-3333', 'Cho.com', nowDatetime),
    (5, 'Yoo', 'Yoo@google.com', '010-4444-4444', 'Yoo.net', nowDatetime)
)
# 파일에서 읽어왔거나 json 형태로 오면 dict로 올수있다
# 튜플안에 튜플, 리스트를 한번에 인서트하는게 훨씬 빠르다

c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", userList) # 알아서 반복문을 통해 들어감

# 테이블 데이터 삭제
# conn.execute("DELETE FROM users") #SQL Delete문을 실행
print("user db deleted : ", conn.execute("DELETE FROM users").rowcount) #지운다음에 지운 결과를 알려줌

# 커밋 : isolation_lever = None 일 경우 자동 반영(auto commit)
# con.commit() // autocommit이 아닐경우 이렇게 commit을 해야함

# 롤백
# conn.rollback()

# 접속 해제
conn.close()