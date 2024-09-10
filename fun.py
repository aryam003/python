# def fun1():
#     print('hi')
#     print('hello')
#     print('python')
#     print('java')

# fun1()
# print(2+2)
# fun1()
# print(2*3)
# fun1()   
'''hi
   hello
   python
   java
   4
   hi
   hello
   python
   java '''

# def fun2():
#     a=20  #local var
#     print('local var ,a:',a)
#     print('global var ,b',b)

# b=30  #global var
# fun2()
# print("global var out side",b)
# print('local var b out side',a) 
'''local var ,a: 20
   global var ,b 30
   global var out side 30''' 

# def fun3():
#     global a
#     a=10
#     print('g var ,b:',b)

# b=20
# fun3()
# print('g var ,b:',b)
# print('a:',a) 
'''g var ,b: 20
   g var ,b: 20
   a: 10'''  
 
# def fun4():
#     return 'hi',10,'hello'
# a,b,c=fun4()
# print(a)
# print(b)
# print(c) 
'''hi
   10
   hello''' 
# def fun5():
#     a=10   #local var
#     b=20
#     c=30
#     return a,b,c
# a1,b1,c1=fun5()
# print(a1)
# print(b1)
# print(c1)  
'''10
   20
   30''' 

'''argument'''
# def dtls(name,age):
#     print('name=',name) 
#     print('age=',age)

# dtls('anu',20)
# dtls('ammu',22)
'''name= anu
   age= 20
   name= ammu
   age= 22'''
# dtls(20,'a')
'''name=20
age=a'''

def fun(name,age):
    print('name=',name)
    print('age=',age)
fun(age=20,name='anu') 
'''name=anu
age=20'''   