import sqlite3
con=sqlite3.connect('python/Emp.db')
try:
    con.execute("create table Emp(id int,name text,age int,salary int,position text,experience int)")
except:    
    print('table exists')
while True:
    print('''
1.Add Emp.
2.View Emp.         
3.Delete Emp.
4.Update Emp.
5.Search Emp.
6.Exit.
''')
    choice=int(input("Enter ur choice:"))
    if choice==1:
        id=int(input("enter id :"))
        name=(input("enter name :"))
        age=int(input("enter age :"))
        salary=int(input("enter salary :"))
        position=(input("enter position :"))
        experience=int(input("enter experience :"))
        con.execute("insert into Emp(id,name,age,salary,position,experience)values(?,?,?,?,?,?)",(id,name,age,salary,position,experience))
        con.commit()
    elif choice==2:
        data=con.execute("select * from Emp")
        print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('id','name','age','salary','position','experience'))    
        print('_'*60)
        for i in data:
            print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(i[0],i[1],i[2],i[3],i[4],i[5]))
    elif choice==3:
        delete=int(input("enter id:"))
        con.execute("delete from Emp where id=?",(delete,))
        con.commit()
    elif choice==4:
        update_id=int(input("Enter ID of the employee to update: "))
        while True:
            print('''
1.age
2.salary
3.position
4.experience
5.exit
''')
            ch_sub=int(input('enter ur choice to update:'))
            if ch_sub==1: 
                new_age=int(input("Enter new age: "))
                con.execute("update Emp set age=? where id=?", (new_age, update_id))
                con.commit()
                
            elif ch_sub==2: 
                new_salary=int(input("Enter new salary: "))
                con.execute("update Emp set age=? where id=?", (new_salary, update_id))
                con.commit()
                
            elif ch_sub==3: 
                new_position=input("Enter new position: ")
                con.execute("update Emp set age=? where id=?", (new_position, update_id))
                con.commit()
                
            elif ch_sub==4:
                new_experience=int(input("Enter new experience: "))
                con.execute("update Emp set age=? where id=?", (new_experience, update_id))
                con.commit()
                
            elif ch_sub==5:
                print("Exiting update menu.")
                break
            else:
                print("Invalid choice. Please try again.")

    elif choice==5:
        search_id=int(input("Enter ID of the employee to search: "))
        data=con.execute("select * from Emp where id=?", (search_id,))
        for i in data:
            print(i)
        else:
            print("No employee found with ID")

    elif choice == 6:
        print("Exiting...")
        break

            


