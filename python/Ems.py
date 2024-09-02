import datetime
Ems=[]
while True:
    print('''
1.Register 
2.View
3.Undate
4.Delete
5.Search
6.Add task
7.view task
8.Exit                    
''')
    choice=int(input("Enter ur choice:"))
    if choice==1:
        id=int(input("enter id :"))
        name=(input("enter name :"))
        age=int(input("enter age :"))
        salary=int(input("enter salary :"))
        position=(input("enter position :"))
        experience=int(input("enter experience :"))
        Ems.append([id,name,age,salary,position,experience])
    elif choice==2:
        print('{:<5}{:<10}{:<5}{:<10}{:<10}{:<5}'.format('id','name','age','salary','position','experience'))    
        print('_'*20)
        for i in Ems:
            print('{:<5}{:<10}{:<5}{:<10}{:<10}{:<5}'.format(i[0],i[1],i[2],i[3],i[4],i[5]))
    elif choice==3:
        id=int(input("enter id:"))
        f=0
        for i in Ems:
            if i[0]==id:
                f=1
                while True:
                    print('''
1.age
2.salary
3.position
4.experience
5.exit
''')
                    sub_choice=int(input("enter ur choice for undate:"))
                    if sub_choice==1:
                        new_age=int(input("new age:"))
                        i[2]=new_age
                    elif sub_choice==2:
                        new_salary=int(input("enter new salary:"))
                        i[3]=new_salary
                    elif sub_choice==3:
                        new_position=(input("enter new position:"))
                        i[4]=new_position
                    elif sub_choice==4:
                        new_experience=int(input("enter ur experience:"))
                        i[5]=new_experience
                    elif sub_choice==5:
                        break    
        if f==0:
            print("id nit in list")
    elif choice==4:
        id=int(input("enter id:"))
        f=0
        for i in Ems:
            if i[0]==id:
                Ems.remove(i)
                f=1
        if f==0:
            print("id not in list")
    elif choice==5:
        id=int(input("enter id:"))
        f=0
        for i in Ems:
            if i[0]==id:
                print(i)
                f=1
        if f==0:
            print("id not in list")
    elif choice==6:
        id=int(input("enter id:"))
        f=0
        for i in Ems:
            if i[0]==id:
                f=1
                task=input("enter task:")
                date=datetime.datetime.now().strftime("%x")
                i.append([task,date])
        if f==0:
            print("invalid id")
    elif choice==7:
        print('{:<5}{:<10}{:<10}{:<10}'.format('id','name','task','date'))    
        print('_'*30)
        for i in Ems:
            if len(i)>6:
               print('{:<5}{:<10}{:<10}{:<10}'.format(i[0],i[1],i[6][0],i[6][1]))
    elif choice==8:
          break
    else:
          print("invalid choice")            



