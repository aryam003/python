user=[{'id':101,'name':'anu','address':'w','email':'anu@gmail.com','phone':22222,'password':'ww','books':[]}]
book=[{'id':101,'name':'name','stock':2,'price':2}]
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
def view_user():
    print('{:<10}{:<10}{:<10}{:<10}{:<10}'.format('id','name','address','phone','email'))
    print('_'*50)
    for i in user:
        print('{:<10}{:<10}{:<10}{:<10}{:<10}'.format(i['id'],i['name'],i['address'],i['phone'],i['email']))                       
def login():
    u_name=input("Enter email:")
    p_word=input("Enter password:")
    f=0
    u=''
    if u_name=='admin' and p_word=='admin':
        f=1
    for i in user:
        if i['email']==u_name and i['password']==p_word:
            f=2
            u=i
    return f,u          
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
        user.append({'id':id,'name':name,'address':address,'email':email,'phone':phone,'password':password,'books':[]})
def view_profile(user):
    print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('id','name','address','phone','email','password'))
    print('_'*60)
    print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(user['id'],user['name'],user['address'],user['phone'],user['email'],user['password']))
def borrow_book(user):
    id=int(input("Enter id:"))
    f=0
    for i in book:
        if i['id']==id:
            f=1
            if i['stock']>0:
                user['books'].append(i['id'])
                i['stock']-=1
                print('book added')
            else:
                print("outof stock.")
    if f==0:
        print('invalid id')
def return_book(user):
    id=int(input("Enter id:"))
    f=0
    for i in book:
        if i['id']==id and id in user['books']:
            f=1
            i['stock']+=1
            user['books'].remove(id)
            print('book returned')
    if f==0:
        print("book not found.") 
def book_in_hand(u):
    print(u['books'])
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
        f,u=login()
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
                elif sub_ch==5:
                    view_user()  
                elif sub_ch==6:
                    break      
        elif f==2:
            while True:
                print('''
1.View profile.
2.View book.
3.Borrow book.
4.Return book.
5.Book in hand.
6.Exit.
''')
                sub_ch=int(input("enter ur choice:"))
                if sub_ch==1:
                    view_profile(u)
                elif sub_ch==2:
                    view()    
                elif sub_ch==3:
                    borrow_book(u)
                elif sub_ch==4:
                    return_book(u)
                elif sub_ch==5:
                    book_in_hand(u)
                elif sub_ch==6:
                    break
                    
        else:
            print('Invalid username or password.')
            
    elif choice==3:
        break    