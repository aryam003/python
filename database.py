import sqlite3

con=sqlite3.connect('python/database.db')

try:
    con.execute("create table std(roll_no int,name text,age int,mark real)")
except:    
    print('table exists')

con.execute("insert into std(roll_no,name,age,mark)values(1,'sree',21,70),(2,'achu',21,75),(3,'arya',21,73)")
con.commit()    