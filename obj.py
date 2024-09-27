# class synnefo:                         
#     def python():                       
#         print('python in synnefo')
#     def php():
#         print('php in synnefo')

# std1=synnefo
# std1.python()  #method
# std1.php()    
# std2=synnefo
# std2.php()


# class bank:
#     def __init__(self):
#         self.bal=0
#     def deposit(self,amt):
#         self.bal+=amt
#         print('amt added')
#     def withdrow(self,amt):
#         self.bal-=amt
#         print('withdrow')
#     def display(self):
#         print('display',self.bal)
# user1=bank()
# user1.deposit(2000)
# print(user1.bal)   #amt added 2000
# user1.withdrow(500)
# print(user1.bal)   #withdrow 1500
# user1.display()    #display 1500
''' amt added
    withdrow
    display 1500''' 
# user2=bank()
# user2.deposit(500)
# user2.withdrow(200)
# user2.display()
''' amt added
    withdrow
    display 300'''

# class demo:
#     def __init__(self,a):
#         print(a)
# obj=demo(500)
# obj1=demo(200)       

class demo:
    def fun(name,age):
       print('name=',name)
       print('age=',age)

s=demo
s.fun(name='A',age=20)