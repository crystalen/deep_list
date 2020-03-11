import sqlite3

conn=sqlite3.connect('words.db')
print('open database')

cursor=conn.cursor()

#cursor.execute('create table stu(id,name,age)')
#conn.commit()
#data=('dat1',2122)
cursor.execute('insert into stu (id,name,age) values(?,?,?),('a','12','34')')
conn.commit()
print(cursor.lastrowid)

cursor.execute('select*from stu')
print(cursor.fetchall())

conn.close()
