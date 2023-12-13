# 커밋이 없으면 데이터 사리진다.

import sqlite3

#연결객체 생성 ('':memory')
con = sqlite3.connect("c:\\work\\sample.db")
# 커서객체
cur = con.cursor()

# 테이블 구조
cur.execute ("create table Phonebook (Name text, PhoneNum text)")

cur.execute("insert into Phonebook values ('김길동', '010-1234-5678')")

# 입력 파라메터 처리
name = "전우치"
phonenumber = "010-222"
cur.execute("insert into Phonebook values (?,?);", (name, phonenumber))


#다중의 레코드
datalist = (("홍길동", "010-222"), ("박문수","010-444"))
cur.executemany("insert into Phonebook values (?,?);", datalist)

# 검색 구문
# cur.execute("select * from Phonebook")
# for row in cur:
#     print (row)

# print ("---fetchone()--")
# print (cur.fetchone())
# print ("---fetchmany(2)--")
# print (cur.fetchmany(2))
# print ("---fetchall()--")
print (cur.fetchall())

# 연결객체
con.commit()
