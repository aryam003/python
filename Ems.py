Ems=[]
while True:
    print('''
1.Register 
2.View
3.Undate
4.Delete
5.Search
6.Add task
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
                age=int(input("enter new age:"))
                salary=int(input("enter new salary:"))
                position=(input("enter new position:"))
                experience=int(input("enter ur experience"))
                i[2]=age
                i[3]=salary
                i[4]=position
                i[5]=experience
                f=1 
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