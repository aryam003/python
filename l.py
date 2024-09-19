user=[]
def add():
    if len(user)==0:
        id=101
    else:
        id=user[-1]['id']+1    
    print(id)
    name=input("enter book name:")
    stock=int(input("enter stock:"))
    price=int(input("enter price:"))
    user.append({'id':id,'name':name,'stock':stock,'price':price})

def view():
    print('{:<10}{:<10}{:<10}{:<10}'.format('id','name','stock','price'))
    print('_'*30)
    for i in user:
        print('{:<10}{:<10}{:<10}{:<10}'.format(i['id'],i['name'],i['stock'],i['price']))    
def login():
    u_name=input("enter name:")
    p_word=input("enter password:")
    f=0
    user=''
    if u_name=='admin' and p_word=='admin':
        f=1
    for i in user:
        if i['email']==u_name and i['password']==p_word:
            f=2
            user=i
    return f,user
            
def register():
    if len(user)==0:
        id=101
    else:
        id=user[-1]['id']+1
    print(id)    
    email=input('enter email:')
    f1=0
    for i in user:
        if i['email']==email:
            f1=1
            print('email exits.')
            register()
    if f1==0:
        name=input('enter name:')
        address=input('enter address:')
        phone=int(input('enter phone No:'))
        password=input("enter password:")
        user.append({'id':id,'name':name,'address':address,'email':email,'phone':phone,'password':password})
while True:
    print('''
1.register
2.login
3.exit
''')
    choice=int(input("enter ur choice:"))
    if choice==1:
        register()
    elif choice==2:
        f,user=login()
        if f==1:
            while True:
                print('''
1.add book.
2.view book.
3.update book.
4.delete book.
5.view user.
''')
                sub_ch=int(input("enter ur choice:"))
                if sub_ch==1:
                    add()
                elif sub_ch==2:
                    view()

        elif f==2:
            print('user login')
        else:
            print('invalid username or password.')
            
    elif choice==3:
        break    