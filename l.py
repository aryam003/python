user=[]
book=[]
def add():
    if len(book)==0:
        id=101
    else:
        id=book[-1]['id']+1    
    print(id)
    name=input("Enter book name:")
    stock=int(input("Enter stock:"))
    price=int(input("Enter price:"))
    book.append({'id':id,'name':name,'stock':stock,'price':price})
def view():
    print('{:<10}{:<10}{:<10}{:<10}'.format('id','name','stock','price'))
    print('_'*40)
    for i in book:
        print('{:<10}{:<10}{:<10}{:<10}'.format(i['id'],i['name'],i['stock'],i['price']))        
def undate():
    id=int(input("Enter id:"))
    f1=0
    for i in book:
        if i['id']==id:
            f1=1
            name=input("Enter book name:")
            stock=int(input("Enter stock:"))
            price=int(input("Enter price:"))  
            i['name']=name
            i['stock']=stock
            i['price']=price
    if f1==0:
        print("Invalid id.") 
def delete():
    id=int(input("Enter id:"))
    f1=0
    for i in book:
        if i['id']==id:
            f1=1
            book.remove(i)
    if f1==0:
        print("Invalid id.") 
# def view_user():
#     print('{:<10}{:<10}{:<10}{:<10}'.format('id','name','address','phone','password'))
#     print('_'*50)
#     for i in user:
#         print('{:<10}{:<10}{:<10}{:<10}{:<10}'.format(i['id'],i['name'],i['address'],i['phone'],i['password']))                       
def login():
    u_name=input("Enter name:")
    p_word=input("Enter password:")
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
    email=input('Enter email:')
    f1=0
    for i in user:
        if i['email']==email:
            f1=1
            print('Email exits.')
            register()
    if f1==0:
        name=input('Enter name:')
        address=input('Enter address:')
        phone=int(input('Enter phone No:'))
        password=input("Enter password:")
        user.append({'id':id,'name':name,'address':address,'email':email,'phone':phone,'password':password})
while True:
    print('''
1.Register
2.Login
3.Exit
''')
    choice=int(input("Enter ur choice:"))
    if choice==1:
        register()
    elif choice==2:
        f,user=login()
        if f==1:
            while True:
                print('''
1.Add book.
2.View book.
3.Update book.
4.Delete book.
5.View user.
6.Exit.
''')
                sub_ch=int(input("Enter ur choice:"))
                if sub_ch==1:
                    add()
                elif sub_ch==2:
                    view()
                elif sub_ch==3:    
                    undate()
                elif sub_ch==4:
                    delete() 
                # elif sub_ch==5:
                #     view_user()  
                elif sub_ch==6:
                    break      
        elif f==2:
            print('user login')
        else:
            print('Invalid username or password.')
            
    elif choice==3:
        break    