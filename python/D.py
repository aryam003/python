# d={'name':'anu','age':20,'mark':80}
# print(d['name'])
'''anu'''
# d['name']='ammu'
'''updating
{'name': 'ammu', 'age': 20, 'mark': 80}'''
# d['place']='pkd'
# print(d)
'''{'name': 'ammu', 'age': 20, 'mark': 80, 'place': 'pkd'}'''
# for i in d:
    # print(i)
'''key'''
    # print(d[i])
'''value'''
    # print(i,d[i])
'''name anu
   age 20
   mark 80'''
# if d['age']==20:
#     print('true')
# else:
#     print('false')
'''true'''
# print(d.get('name'))
'''anu'''
# print(d.get('place'))
'''Noue'''    
# print(d.values())
'''dict_values(['anu', 20, 80])'''
# print(d.keys())
# print(d.items())
'''items'''

'''pop'''
# d.pop('name')
# print(d)
'''{'age': 20, 'mark': 80}'''
# d.popitem()
# print(d)
'''{'name': 'anu', 'age': 20}'''

'''add/update'''
# d.update({'name':'achu'})
'''{'name': 'achu', 'age': 20, 'mark': 80}'''
# d.update({'place':'pkd'})
'''{'name': 'anu', 'age': 20, 'mark': 80, 'place': 'pkd'}'''
# print(d)

'''fromkeys'''
# d={}
# l=['name','age','mark']
# d=d.fromkeys(l)
# print(d)
'''{'name': None, 'age': None, 'mark': None}'''

'''setdefault'''
d={}
d.setdefault('name')
print(d)
'''{'name': None}'''