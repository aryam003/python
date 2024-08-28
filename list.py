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

l=[1,5,8,10,11]
sum=0
for i in l:
    sum+=i
print("sum:",sum)    

           