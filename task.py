def number():
    a=int(input("enter a No:"))
    b=int(input("enter a No:"))
    return a,b
def add():
    a,b=number()
    print(a+b)
def sub():
    a,b=number()
    print(a-b)
def mult():
    a,b=number()
    print(a*b)
def div():
    a,b=number()
    print(a/b)    
def mod():
    a,b=number()
    print(a%b)

while True:
    print('''
1.Add
2.Subtraction
3.Multiplication
4.Division
5.Modulus
6.Exit''')
    choice=int(input("enter ur choice:"))
    if choice==1:
        add()
    elif choice==2:
        sub()
    elif choice==3:
        mult()
    elif choice==4:
        div()
    elif choice==5:
        mod()
    elif choice==6:
        break
    