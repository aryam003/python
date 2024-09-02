# l=[10,20,'A',2.5]
# if 20 in l:
#         print('yes')
# else:
#         print('no')
'''yes'''
# l=[10,15,5,'a',2.3]
# print(l[1])
'''15'''
# l=[10,15,5,'a',2.3]
# l[2]="anu"
# print(l)
'''[10,15,'anu','a',2.3]'''
# l=[10,15,5,'a',2.3]
# l[3]="list"
# print(l)
'''[10,15,5,'list',2.3]'''

'''Add'''

# l=[1,2]
# l.append(10)
# l.append('anu')
# l.append([1,2,3])
# print(l)
'''[1, 2, 10, 'anu', [1, 2, 3]]'''
# l=[1,2]
# l.append(10)
# l.append('anu')
# l.append([1,2,3])
# print(l[3])
'''anu'''
# print(l[4][1])
'''2'''
# l=[1,2]
# l.extend(['a','b','c'])
# print(l)
'''[1,2,'a','b','c']'''
# l=[1,2,3]
# l.insert(0,'a')
# print(l)
'''['a', 1, 2, 3]'''


# l=[1,2,3,4,5]
# l.clear()
# print(l)
'''[]'''
# l=[1,2,3,4,5]
# l.pop()
# print(l)
'''[1,2,3,4]'''
# l=[1,2,'abc',3,4,5]
# l.remove('abc')
# print(l)
'''[1,2,3,4,5]'''

# l=[4,2,8,6,1,9]
# l.sort()
# print(l)
'''[1, 2, 4, 6, 8, 9]'''
# l=[4,2,8,6,1,9]
# l.reverse()
# print(l)
'''[9, 1, 6, 8, 2, 4]'''
# l=[4,2,8,6,1,9]
# l.sort()
# l.reverse()
# print(l)
'''[9, 8, 6, 4, 2, 1]'''
# l=[1,2,3,4,5]
# l1=[1,4,7,4,5]
# l1=l.copy()
# print(id(l))
# print(id(l1))
# print('l=',l)
# print('l1=',l1)
# l1.pop()
# print('l=',l)
# print('l1=',l1)
'''140430968234752
140430968552576
l= [1, 2, 3, 4, 5]
l1= [1, 2, 3, 4, 5]
l= [1, 2, 3, 4, 5]
l1= [1, 2, 3, 4]'''
# l=[1,2,3,4,5]
# print(l.index(5))
'''4'''

# l=[1,5,8,10,11]
# odd=[]
# even=[]
# for i in l:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("odd:",odd)         
# print("even:",even) 

# l=[1,5,8,10,11]
# sum=0
# for i in l:
#     if i%2==0:
#        sum+=i
#        print(i)
# print("sum:",sum)    

# l=['welcome','python','hello']
# for i in l:
#     print(i[::-1])          
'''emoclew
   nohtyp
   olleh'''
# l=[1,3,2.5,'ab',6]
# sum=0
# for i in l:
#     if type(i)==int or type(i)==float:
#       sum+=i
# print("sum:",sum)
'''sum: 12.5'''    
# l=[2,3,4,2,5,3,1,6,1]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)
'''[2, 3, 4, 5, 1, 6]''' 
# names=[]
# limit=int(input("enter limit:"))
# for i in range(limit):
#     name=(input("enter name:"))
#     names.append(name)
# print(names)
'''enter limit:2
   enter name:a
   enter name:s
   ['a', 's']'''  
# std=[]
# limit=int(input("enter limit :"))
# for i in range(limit):
#     name=(input("enter a name:"))
#     age=int(input("enter age:"))
#     mark=int(input("enter mark:"))
#     std.append([name,age,mark])
# print(std) 
'''[['Anu', 20, 90], ['Ammu', 15, 100]]'''
std=[]
while True:
     print('''
1.Add std
2.View std
3.Update std
4.Delet std 
5.Search std
6.Exit                                                
''')
     choice=int(input("enter ur choice:"))
     if choice==1:
         name=(input("enter a name:"))
         age=int(input("enter age:"))
         mark=int(input("enter mark:"))
         std.append([name,age,mark])
     elif choice==2:
         print('{:<10}{:<5}{:<5}'.format('name','age','mark'))
         print('_'*20)
         for i in std:
               print('{:<10}{:<5}{:<5}'.format(i[0],i[1],i[2])) 
     elif choice==3:
          name=input("enter name:")
          f=0
          for i in std:
               if i[0]==name:
                    mark=int(input("enter new mark:"))
                    i[2]=mark
                    f=1
          if f==0:
               print("name not in list") 
     elif choice==4:
          name=input("enter name:")
          f=0
          for i in std:
               if i[0]==name:
                    std.remove(i)
                    f=1
          if f==0:
               print("name not in list")
     elif choice==5:
          name=input("enter name:")
          f=0
          for i in std:
               if i[0]==name:
                    print(i)
                    f=1
          if f==0:
               print("name not in list")
     elif choice==6:
          break
     else:
          print("invalid choice")                                     
