import sqlite3
con=sqlite3.connect('python/join.db')
try:
    con.execute("create table std(No int,name text,age int)")
except:    
    print('table exists')

# con.execute("insert into std(No,name,age)values(1,'A',20),(2,'B',21),(3,'C',22)")
# con.commit()   

try:
    con.execute("create table mark(No int,sub text,mark int)")
except:    
    print('table exists') 
# con.execute("insert into mark(No,sub,mark)values(1,'py',70),(2,'php',60),(4,'java',65),(1,'php',72)")
# con.commit()

# data=con.execute("select std.No,std.name,std.age,mark.sub,mark.mark from std join mark on std.No=mark.No")       #inner join
# for i in data:
#     print(i)  
''' (1, 'A', 20, 'php', 72)
    (1, 'A', 20, 'py', 70)
    (2, 'B', 21, 'php', 60)'''

# data=con.execute("select std.No,std.name,std.age,mark.sub,mark.mark from std left join mark on std.No=mark.No")   #left join
# for i in data:
#     print(i)
''' (1, 'A', 20, 'php', 72)
    (1, 'A', 20, 'py', 70)
    (2, 'B', 21, 'php', 60)
    (3, 'C', 22, None, None)'''

# data=con.execute("select std.No,std.name,std.age,mark.sub,mark.mark from mark left join std on std.No=mark.No")     #right join
# for i in data:
#     print(i)
''' (1, 'A', 20, 'py', 70)
    (2, 'B', 21, 'php', 60)
    (None, None, None, 'java', 65)
    (1, 'A', 20, 'php', 72)'''

# data=con.execute("select std.No,std.name,std.age,mark.sub,mark.mark from std cross join mark")
# for i in data:
#     print(i)
'''(1, 'A', 20, 'py', 70)
(1, 'A', 20, 'php', 60)
(1, 'A', 20, 'java', 65)
(1, 'A', 20, 'php', 72)

(2, 'B', 21, 'py', 70)
(2, 'B', 21, 'php', 60)
(2, 'B', 21, 'java', 65)
(2, 'B', 21, 'php', 72)

(3, 'C', 22, 'py', 70)
(3, 'C', 22, 'php', 60)
(3, 'C', 22, 'java', 65)
(3, 'C', 22, 'php', 72)'''