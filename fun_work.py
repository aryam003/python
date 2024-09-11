emp=[]
def login():
    uname=input("enter uname:")
    passw=input("enter passw:")
    f=0
    if uname=='admin' and passw=='admin':
        f=1
    return f

def add_emp():
    id=int(input("enter id:"))
    f1=0
    for i in emp:
        if i['id']==id:
            f1=1
            print('id exits.')
            add_emp()
    if f1==0:
        name=input("enter name:")
        age=int(input("enter age:"))
        salary=int(input("enter salary:"))
        place=input("enter place:")
        dob=input("enter dob:")
        emp.append({'id':id,'name':name,'age':age,'salary':salary,'place':place,'dob':dob})

def edit_emp():
    id=int(input("enter id:"))
    f1=0
    for i in emp:
        if i['id']==id:
            f1=1
            name=input("enter name:")
            age=int(input("enter age:"))
            salary=int(input("enter salary:"))
            place=input("enter place:")
            dob=input("enter dob:")
            i['name']=name
            i['age']=age
            i['salary']=salary
            i['place']=place
            i['dob']=dob
    if f1==0:
        print("invalid id.")

def delete():
    id=int(input("enter id:"))
    f1=0
    for i in emp:
        if i['id']==id:
            f1=1
            emp.remove(i)
    if f1==0:
        print("invalid id.")
def display():
        print('{:<5}{:<10}{:<5}{:<10}{:<10}{:<10}'.format('id','name','age','salary','place','dob'))
        print('_'*50)
        for i in emp:
            print('{:<5}{:<10}{:<5}{:<10}{:<10}{:<10}'.format(i['id'],i['name'],i['age'],i['salary'],i['place'],i['dob'])) 
             
while True:
    print('''
1.login
2.exit
''')
    ch=int(input("enter ur choice:"))
    if ch==1:
        f=login()
        if f==1:
            while True:
                print('''
1.add emp
2.update emp
3.delete
4.display
''')
                sub_ch=int(input("enter ur choice:"))
                if sub_ch==1:
                    add_emp()
                elif sub_ch==2:
                    edit_emp()
                elif sub_ch==3:
                    delete()
                elif sub_ch==4:
                    display()
                elif sub_ch==5:
                    break
    elif f==0:
        print("invalied uname or passw")
    
