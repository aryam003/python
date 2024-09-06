import datetime
print(datetime.datetime.now().strftime("%x"))
sale=[]
while True:
    print('''
1.Register of product. 
2.View of products.
3.Update.
4.Search.         
5.Delete.
6.Exit.
''')
    choice=int(input("Enter your choice :"))
    if choice==1:
        name=input("Enter product Name :")
        price=int(input("Enter product price :"))
        B_name=input("Enter Brand Name :")
        N_weight=int(input("Enter Net Weight :"))
        B_No=int(input("Enter Batch Number :"))
        contact=int(input("Enter contact information :"))
        date=datetime.datetime.now().strftime("%x")
        sale.append([name,price,B_name,N_weight,B_No,contact,date])
    elif choice==2:
        print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('name','price','B_name','N_weight','B_No','contact','date'))
        print('_'*70)
        for i in sale:
             print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    elif choice==3:
        name=input("Enter product name :")
        f=0
        for i in sale:
            if i[0]==name:
                f=1
                while True:
                    print('''
1.Price.
2.Brand Name.
3.Net Weight.                          
4.Batch Number.
5.Contact. 
6.Date.
7.Exit.                          
''')
                    sub_choice=int(input("Enter choice for update :"))
                    if sub_choice==1:
                        new_price=int(input("Enter new price :"))
                        i[1]=new_price
                    elif sub_choice==2:
                        new_B_name=input("Enter new Brand name :")
                        i[2]=new_B_name
                    elif sub_choice==3:
                        new_N_weight=int(input("Enter new Net Weight :"))
                        i[3]=new_N_weight
                    elif sub_choice==4:
                        new_B_No=int(input("Enter new Batch Number :"))
                        i[4]
                    elif sub_choice==5:
                        new_c=int(input("Enter new contact :"))
                        i[5]
                    elif sub_choice==6:
                        new_date=datetime.datetime.now().strftime("%x")
                        i[6]  
                    elif sub_choice==7:
                        break
        if f==0:
            print("invalied data.") 
    elif choice==4:
        name=input("Enter product name :")
        f=0
        for i in sale:
            if i[0]==name:
                price(i)
                f=1
        if f==0:
            print("invalied data.")
    elif choice==5:
        name=input("Enter product name :")
        f=0
        for i in sale:
            if i[0]==name:
                sale.remove(i)
                f=1
        if f==0:
            print("invalied data.")
    elif choice==6:
        break
    else:
        print('invalid data.')                           
