emp=[]
def login():
    uname=input("enter uname:")
    passw=input("enter passw:")
    f=0
    user=''
    if uname=='admin' and passw=='admin':
        f=1
    for i in emp:
        if i['id']==uname and i['password']==passw:
            f=2
            user=i    
    return f,user

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
        print('Employee added successfully')
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
def view_profile(user):
    print('_'*65)
    print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<15}".format('id','name','age','salary','place','date of birth'))
    print('-'*65)
    print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<15}".format(user['id'],user['name'],user['age'],user['salary'],user['place'],user['date_of_birth']))
def user_update(user):
    f4=0
    for i in emp:
        if i['id']==user['id']:
            f4=1
            name=input('enter the updatede name: ')
            age=int(input('enter your age: '))
            place=(input('enter your place: '))
            dob=(input('enter your date of birth: '))
            i['name']=name
            i['age']=age
            i['place']=place
            i['date_of_birth']=dob
            print('updated')
    if f4==0:
        print('invalid id.')
while True:
    print('''
1.login
2.exit
''')
    ch=int(input("enter ur choice:"))
    if ch==1:
        f,user=login()
        if f==1:
            while True:
                print('''
1.add emp
2.update emp
3.delete
4.display
5.exit.
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
                else:
                    print("Invalid choice.")
        elif f==0:
            print("invalied uname or passw")
        elif f==2: 
            while True:
                if user['date_of_birth']==user['password']:
                    password=input('enter a new password')
                    user['password']=password
                else:
                    print('''
                        1.view profile
                        2.edit profile
                        3.logout
    ''')
                    sub_ch=int(input('enter your choice: '))
                    if sub_ch==1:
                        view_profile(user)
                    elif sub_ch==2:
                        user_update(user)
                    elif sub_ch==3:
                        break 
    elif ch==2:
        break
    
