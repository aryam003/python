book=[{'id':1,'b_name':'b_name','b_price':100,'stock':12}]
# user=[{'id':101,'name':'anu','address':'w','email':'anu@gmail.com','phone':22222,'password':'ww','books':[]}]


# while True:
#     print('''
# 1.Register
# 2.Login
# 3.Exit
# ''')
#     choice=int(input("Enter ur choice:"))
#     if choice==1:
#         if len(user)==0:
#            id=101
#         else:
#             id=user[-1]['id']+1
#         print(id)    
#         email=input('Enter email:')
#         f1=0
#         for i in user:
#             if i['email']==email:
#                 f1=1
#                 print('Email exits.')



while True:
    print("""
1.Add book
2.View book
3.Update book
4.Remove book 
5.Search book
6.Exit 
""")
    choice=int(input("enter ur choice:"))
    if choice==1:
        id=int(input("enter book id:"))
        b_name=input("enter book name:")
        b_price=int(input("enter price:"))
        stock=int(input("enter stock :"))
        book.append({'id':id,'b_name':b_name,'b_price':b_price,'stock':stock})
    elif choice==2:
        print('{:<10}{:<10}{:<15}{:<10}'.format('id','book_name','book_price','stock'))
        print('_'*50)
        for i in book:
            print('{:<10}{:<10}{:<15}{:<10}'.format(i['id'],i['b_name'],i['b_price'],i['stock']))

    elif choice==3:
        id=int(input("Enter id:"))
        f=0
        for i in book:
            if i['id']==id:
                f=1
                while True:
                    print("""
1.new price
2.stock
3.exit
""")
                    sub_choice=int(input("Enter choice for update :"))
                    if sub_choice==1:
                        new_price=int(input("Enter new price :"))
                        i['b_price']=new_price
                    elif sub_choice==2:
                        new_B_name=int(input("Enter new Brand name :"))
                        i['stock']=new_B_name
                    elif sub_choice==3:
                        break

    elif choice==4:
        id=int(input("Enter id:"))
        f1=0
        for i in book:
            if i['id']==id:
                book.remove(i)
                f1=1
        if f1==0:
            print("Invalid id.") 

    elif choice==5:
        id=int(input("enter id:"))
        f=0
        for i in book:
            if i['id']==id:
                print(i)
                f=1
        if f==0:
            print(" not in list")

    elif choice==6:
        break
    else:
        print('invalid data.')
         
                
        
