
# import datetime
# print(datetime.datetime.now().strftime('%d'))
'''day of month'''
# print(datetime.datetime.now().strftime('%a'))
'''weekday (short)(full:%A):mon ,etc...'''
# print(datetime.datetime.now().strftime('%b'))
'''month (short)(full:%B):sep,etc...'''

# from datetime import datetime
# print(datetime.now())


'''math'''
# import math
# print(math.ceil(10.5))
'''11'''
# print(math.floor(10.5))
'''10'''
# print(math.factorial(5))
'''120'''
# print(math.sqrt(64))
'''8.0'''

'''file crating'''
# p=open('python/demo.txt','x')
'''methods in file handaling'''
'''write'''

# p.write('hello')
# p=open('python/demo.txt','r')
# a=p.read()
# print(a)
'''hello(demo.txt)'''

# f=open('python/demo.txt','x')
# f.write('welcome \n hello \n hi')

# f=open('python/demo.txt','r')
# a=f.read()
# print(a)
'''Welcome'''
# or
# print(f.read())
'''Welcome'''




# f=open('python/demo.txt','r')
# a=f.read(5)

# f.seek(0)

# b=f.read()

# print(f.tell())
# print(a)
# print('_'*20)
# print(b)

'''
7
welco
____________________
welcome
'''

# f=open('python/demo.txt','r')
# a=f.readline(5)
# b=f.readline()
# c=f.readline()
# print(a)
# print(b)
# print(c)
'''
welco
me 

hello 

'''

# f=open('python/demo.txt','r')
# a=f.readline(5)
# b=f.readline()

# print(a)
# print(b)
# f.seek(0)
# l=f.readlines()
# print(l)

'''
welco
me 

['welcome \n', 'hello \n', 'hi']'''



# f=open('python/demo.txt','r')
# l=f.readlines()
# f.seek(0)
# for i in range(len(l)):
#     a=f.readline().strip()
#     print(a)

'''
welcome
hello
hi
'''   

# f=open('python/demo.txt','r')
# l=f.readlines()
# f.seek(0)

# for i in range(len(l)):
#     a=f.readline().strip()
#     rev=' '
#     rev=i+rev
    
# print(rev) 
'''
welcome 
hellowelcome 
hihellowelcome '''    

# f=open('python/demo.txt','r')
# l=f.readlines()
# f.seek(0)
# for i in range(len(l)):
#     a=f.readline().strip()
#     print(a[::-1])   # slicing method
'''
emoclew
olleh
ih
'''
# f=open('python/demo1.txt','w')
# f.write('\nWELCOME')

# f=open('python/demo1.txt','a')
# f.write('\nWELCOME')
'''
WELCOME
WELCOME
WELCOME
'''
    #  print(x*y)

# f=open('python/demo1.txt','w')
# a=int(input("Enter a no :"))
# for i in range(1,11):
#     # print(i ,'*', a ,'=',i*a)
#     f.write(str(i)+'*'+str(a)+'='+str(i*a)+'\n')
'''write in to new file (1*2=2 to 10*2=20)'''

# f=open('python/demo2.txt','w')
# a=int(input("Enter a no :"))
# for i in range(1,11):
#     # print(i ,'*', a ,'=',i*a)
#     f.write(str(i)+'*'+str(a)+'='+str(i*a)+'\n')

        

# w=open('python/demo2.txt', 'w')
# for i in range(1, 11):  
#         for a in range(1, 6):  
#             w.write(str(i)+'*'+str(a)+'='+str(i*a)+'\t')
#         w.write("\n")
'''or'''
# w=open('python/demo2.txt', 'w')
# s=int(input("enter a No:"))
# for i in range(1, 11):  
#         for a in range(1,s+1):  
#             w.write(str(i)+'*'+str(a)+'='+str(a*i)+'\t')
#         w.write("\n")

# f=open('python/demo.txt','r')
# l=f.readlines()
# f.seek(0)
# letter=0
# for i in range(len(l)):
#     a=f.readline().strip()
#     for i in a:
#         if i !=' ':
#             letter+=1
# print(letter)
'''14'''

# f=open('./arya/python/demo.txt','r')
# l=f.readlines()
# f.seek(0)
# letter=0
# cap=0
# for i in range(len(l)):
#     a=f.readline().strip()
#     for i in a:
#          if i !=' ':
#             if i.isupper():
#                 cap+=1
#             letter+=1
# print(letter)
# print('cap:',cap)
# print('small:',letter-cap)
'''14
cap 3
small 11'''
f=open('./arya/python/demo.txt','r')
l=f.readlines()
f.seek(0)
letter=0
cap=0
w=0
for i in range(len(l)):
    a=f.readline().strip()
    s=a.split(' ')
    for i in s:
        if i!='':
            w+=1
    for i in a:
         if i !=' ':
            if i.isupper():
                cap+=1
            letter+=1
print(letter)
print('cap:',cap)
print('small:',letter-cap)
print('word:',w)
print('no of lines:',len(l))