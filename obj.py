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

# class demo:
#     def fun(name,age):
#        print('name=',name)
#        print('age=',age)


'''type of inheritance'''

#---------------------------------------------
#to connect one or more class
#---------------------------------------------

'''single inheritance'''

#A-->B

# s=demo
# s.fun(name='A',age=20)

# class parent:
#     def shop(self):
#         print('shop')
#     def car(self):
#         print('car')

# class child(parent):
#     def bike(self):
#         print('bike')

# anu=child()
# anu.bike()
# anu.shop()
'''bike
   shop'''

# class syn:
#     def python(self):
#         print('python')
#     def php(self):
#         print('php')
# class novavi(syn):
#     def dm(self):
#         print('dm_work')
#     def web(self):
#         print('web_dev')

# anu=novavi()
# anu.web()
# anu.python()  #can use methods of syn and novavi

# std=syn()
# std.php()    #only can use syn methods
''' #anu
        web_dev
        python
    #std
        php'''

#------------------------------------------------------------------

'''Multiple inheritance'''

#A---->C<-----B

# class mom:
#     def shop(self):
#         print('shop')
#     def car(self):
#         print('car')
# class dad:
#     def dress_shop(self):
#         print('derss shop')
# class child(mom,dad):
#     def bike(self):
#         print('bike')

# anu=child()
# anu.dress_shop()
# anu.car()
# anu.bike()
'''dress_shop
   car
   bike'''
# class school:
#     def class_room(self):
#         print('class_room')
#     def ground(self):
#         print('ground')
# class tuition:
#     def notes(self):
#         print('note')
#     def work(self):
#         print('work')    
# class std(school,tuition):
#     def uniform(self):
#         print('uniform')

# A=std()
# A.class_room()
# A.notes()
# A.uniform()
'''#school
        class_room
   #tuition     
        note
   #std
        uniform'''
#-----------------------------------------------------------

'''Multilevel inheritance'''
#

# class knr_un:
#     def exam_notice(self):
#         print('exam notice')
#     def result(self):
#         print('result')
# class clg(knr_un):
#     def notes(self):
#         print('notes')
#     def cls_rooms(self):
#         print('class room')
# class std(clg):
#     def uniform(self):
#         print('uniform')

# A=std()         
# A.exam_notice()
# A.notes()
# A.uniform()        

# B=clg()
# B.result()
# B.cls_rooms()
''' exam notice
    notes
    uniform
    result
    class room'''

# class g_father:
#     def shop(self):
#         print('shop')
#     def car(self):
#         print('car')
# class father(g_father):
#     def dress_shop(self):
#         print('derss shop')
# class child(father):
#     def bike(self):
#         print('bike')
# anu=child()
# anu.shop()
# anu.dress_shop()
# anu.bike()  
'''shop
   dress shop
   bike'''   
#-----------------------------------------------------

'''Higherarcial inheritance''' 

# class father:
#     def shop(self):
#         print('shop')
#     def car(self):
#         print('car')
# class child_1(father):
#     def bike(self):
#         print('bike')
# class child_2(father):
#     def dress_shop(self):
#         print('dress shop')

# anu=child_1()
# anu.bike()   #car,shop
# manu=child_2()
# manu.car()     #dress shop,shop

# class school:
#     def exam_notice(self):
#         print('exam notice')
#     def result(self):
#         print('result')
# class class_1(school):
#     def notes(self):
#         print('notes')
#     def cls_rooms(self):
#         print('class room')
# class class_2(school):
#     def notes(self):
#         print('notes')
#     def cls_rooms(self):
#         print('class room')

# c=class_1()
# c.cls_rooms()  #notes,exam notice,result
# s=class_2()
# s.result()     # ''
'''class room
result'''

#-----------------------------------------------------------------

'''hybrid inheritance'''

# class syn:
#     def python(self):
#         print('python')
#     def php(self):
#         print('php')
#     def admission(self):
#         print('admission')
# class teach_staff(syn):
#     def notes(self):
#         print('notes')
#     def attentence(self):
#         print('attentance')
# class staff(syn):
#     def account(self):
#         print('accounts')
#     def report(self):
#         print('repote') 
# class std(teach_staff):
#     def lab(self):
#         print('lab')
#     def task(self):
#         print('task')     
# anu=std()
# anu.admission()
# anu.notes()
# anu.lab() 
'''admission
   notes
   lab'''


# class library:
#     def books(self):
#         print('books')
#     def register(self):
#         print('register')    


# class owner(library):
#     def b_cost(self):
#         print('book cost')
#     def s_salary(self):
#         print('staff salary')

# class user(library):
#     def b_name(self):
#         print('book name')
#     def d_return(self):
#         print('date of return')

# class staff(owner):
#     def B_record(self):
#         print('book recodes')
#     def B_name(self):
#         print('book name')
#     def w_time(self):
#         print('working time')   


# staff1=staff()
# staff1.register()
# staff1.b_cost()
# staff1.w_time() 
# staff1.books()
# staff1.B_record()
# staff1.s_salary()
''' register
    book cost
    working time
    books
    book recodes
    staff salary
'''
# print('-'*20)
# user1=user()
# user1.register()
# user1.b_name()
# user1.books()
# user1.d_return()
'''register
   book name
   books
   date of return'''
            
#------------------------------------------------------------
'''method over loading
   method over riding(only supports python)'''
#-------------------------------------------------------------

'''method over riding'''

class bank():
    def __init__(self):
        print('Bank dtle')
class user():
    def __init__(self):
        print('User dtle')

A=user()
B=bank()
