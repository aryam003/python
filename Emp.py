import sqlite3
con=sqlite3.connect('python/Emp.db')
try:
    con.execute("create table std(id int,name text,age int,salary int)")
except:    
    print('table exists')

while True:
    print('''
1.Add Emp.
2.View Emp.         
3.Delete Emp.
4.Update Emp.
5.search Emp.
''')
    choice=int(input("enter ur choice:"))
    if choice==1:
        print