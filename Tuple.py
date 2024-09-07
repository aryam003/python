# t=(1,2,3,'www',2.5,3)
# T=()
# for i in t:
#     print(i)

# if 2 in t:
#     print("true")
# else:
#     print("false")    

# print(t[0])

# t=(1,2,3,[4,5])
# print(t[3])
'''[4, 5]'''
# t[3].append(6)
# print(t)
'''(1, 2, 3, [4, 5, 6])'''

# t=[1,2,(3,4)]
# t.append(3)
# print(t)
'''[1, 2, (3, 4), 3]'''

'''methodes:
  1.index
  2.count'''
# t=(1,2,3,4,5)
# print(t.index(3))
'''2'''
# print(t.count(4))
'''1'''

'''updateting tuple'''
# t=(1,2,3,4,5)
# l=list(t)
# print(l)
'''[1, 2, 3, 4, 5]'''
# l.pop()
# print(l)
'''[1, 2, 3, 4]'''
# t=tuple(l)
# print(t)
'''(1, 2, 3, 4, 5)'''

# d={'name':'A','age':20}
# l=list(d)
# print(l)
'''['name', 'age'] ,keys '''

'''s=set()'''
# s={1,2,3,4,'abcd',3,4,4,5,2,6}
# print(s)
'''{1,2,3,4,'abcd'}
set is a dict'''

# l=[1,2,3,4,2,5,3]
# s=set(l)
# print(l)
'''{1, 2, 3, 4, 5} ,dict'''
# l=list(s)
# print(l)
'''[1, 2, 3, 4, 5] ,list'''

# s={10,20,30,40}
# s.add(50)
# print(s)
# print(s.difference({20,10,30}))
'''{40}'''
# s1={10,11,12,15}
# print(s.difference(s1))
'''{40, 20, 30}'''
# s.discard(20)
# print(s)
'''{40, 10, 30}'''
# s.pop()
# print(s)
'''{10, 20, 30}'''
# s={1,2,3}
# s1={1,2,3,4,5}
# s.intersection(s1)
# print(s)
'''{1,2,3}'''
# print(s.union(s1))
'''{1,2,3,4,5}'''
# s2={10,20,30}
# print(s.isdisjoint(s2))
'''True'''
# print(s.issubset(s1))
'''true'''
# print(s.issuperset(s1))
'''false: s={1,2,3} s1={1,2,3,4,5}
True: s={1,2,3} s1={1,2,3}'''
# print(s.symmetric_difference(s1))
'''{4,5} (difference b/w s&s1)'''
# s={1,2,3,6,7}
# s1={1,2,3,4,5}
'''updateting s.'''
# s.difference_update(s1)
# print(s)
'''{6,7}'''
# s.intersection_update(s1)
# print(s)
'''{1,2,3}'''
# s.symmetric_difference_update(s1)
# print(s)
'''{4,5,6,7}'''

php=set()
a=int(input("Enter limit :"))
for i in range(a):
    name=input("Enter name :")
    php.add(name)
print(php)

python=set()
b=int(input("Enter limit:"))
for i in range(b):
    n=input("Enter name:")
    python.add(n)
print(python)

java=set()
c=int(input("Enter limit:"))
for i in range(c):
    ne=input("Enter name:")
    java.add(ne)
print(java)

# data=php.intersection(python)
# data1=java.intersection(data)
# print(data1) 

data=python.difference(php)
data1=python.difference(java)
print(data1)

