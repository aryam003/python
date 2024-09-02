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
# d={}
# d.setdefault('name')
# print(d)
'''{'name': None}'''

std=[]
while True:
    print('''
1.Add
2.View
3.Update
4.Delete
5.Search
6.Exit
''')
    choice=int(input("enter ur choice:"))
    if choice==1:
        name=(input("enter name:"))
        age=int(input("enter age:"))
        mark=int(input("enter mark:"))
        std.append({'name':name,'age':age,'mark':mark})
    elif choice==2:
        print('{:<10}{:<5}{:<5}'.format('name','age','mark'))    
        print('_'*20)
        for i in std:
            print('{:<10}{:<5}{:<5}'.format(i['name'],i['age'],i['mark']))
    elif choice==3:
        name=input("enter name:")
        f=0
        for i in std:
            if i['name']==name:
                mark=int(input("enter new mark:"))
                i['mark']=mark
                f=1
        if f==0:
            print('not found')        
    elif choice==4:
        name=input("enter name:")
        f=0
        for i in std:
            if i['name']==name:
                std.remove(i)
                f=1
        if f==0:
            print("name not in list")
    elif choice==5:
        name=input("enter name:")
        f=0
        for i in std:
            if i['name']==name:
                print(i)
                f=1
        if f==0:
            print("name not in list")
    elif choice==6:
        break
    else:
        print("invalid choice")         