import sqlite3

con=sqlite3.connect('python/database.db')

try:
    con.execute("create table std(roll_no int,name text,age int,mark real)")
except:    
    print('table exists')

    
'''insert'''
# con.execute("insert into std(roll_no,name,age,mark)values(1,'sree',21,70),(2,'achu',21,75),(3,'arya',21,73)")
# con.commit()    

#-------------------------------------------------------------------------------------------------

# roll=int(input('enter roll_no:'))
# name=input('enter name:')
# age=int(input('enter age:'))
# mark=float(input('enter mark:'))

# con.execute('insert into std(roll_no,name,age,mark)values(?,?,?,?)',(roll,name,age,mark))
# con.commit()

# limit=int(input('enter limit:'))
# for i in range(limit):
#     roll=int(input('enter roll_no:'))
#     name=input('enter name:')
#     age=int(input('enter age:'))
#     mark=float(input('enter mark:'))
#     con.execute('insert into std(roll_no,name,age,mark)values(?,?,?,?)',(roll,name,age,mark))
#     con.commit()

'''select'''

# data=con.execute("select * from std")
# for i in data:
#     print(i)                                    #display all data 

# data=con.execute("select name from std")
# for i in data:
#     print(i)                                    #display names(select name.age display name and age)

# data=con.execute("select * from std")
# for i in data:
#     print('{:<10}{:<10}{:<10}{:<10}'.format('roll_no','name','age','mark'))
#     print('_'*40)
#     for i in data:
#         print('{:<10}{:<10}{:<10}{:<10}'.format(i[0],i[1],i[2],i[3]))

# data=con.execute("select * from std where name='achu'")
# for i in data:
#     print(i)
'''(2, 'achu', 21, 75.0)'''

# data=con.execute("select * from std where age='21'")
# for i in data:
#     print(i)       #display all data that age=21

# roll=int(input("enter roll no:"))
# data=con.execute("select * from std where roll_no=?",(roll,))
# for i in data:
#     print(i)
'''(2, 'achu', 21, 75.0)'''
#------------------------------------------------------------------------------------
'''update'''

# con.execute("update std set name='athi' where name='a'")
# con.commit()


# new_name=input("enter new name:")
# old_name=input("enter old name:")
# con.execute("update std set name=? where name=?",(new_name,old_name))
# con.commit()

#------------------------------------------------------------------------------------
'''delete'''

# con.execute("delete from std where roll_no=3")
# con.commit()

delete=int(input("enter roll no:"))
con.execute("delete from std where roll_no=?",(delete,))
con.commit()