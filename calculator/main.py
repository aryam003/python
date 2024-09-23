import number
import add as d
import sub as s 
import mul as m
import div as v
import mod as o
while True:
    print('''
1.Add
2.Subtraction
3.Multiplication
4.Division
5.Modulus
6.Exit
''')
    choice=int(input("enter ur choice:"))
    if choice==1:
        a,b=number.num()
        d.add(a,b)
    elif choice==2:
        a,b=number.num()
        s.sub(a,b)
    elif choice==3:
        a,b=number.num()
        m.mul(a,b)
    elif choice==4:
        a,b=number.num()
        v.div(a,b)
    elif choice==5:
        a,b=number.num()
        o.mod(a,b)

    

        