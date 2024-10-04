                                            #regular expression(re)
import re                                         
a='abcd'
# print(re.search('a',a))
'''<re.Match object; span=(0, 1), match='a'>'''
# print(re.search('ab',a))
'''<re.Match object; span=(0, 2), match='ab'>'''
# print(re.search('s',a))
'''None'''
# if re.search('a',a):
#     print('match')
# else:
#     print('not match')
'''match'''
#-----------------------------------------------------------

'''represent single character'''

# print(re.search('a.',a))
'''<re.Match object; span=(0, 2), match='ab'>'''
# print(re.search('b.',a))
'''<re.Match object; span=(1, 3), match='bc'>'''
#------------------------------------------------------------

'''represent zero or more character'''

# print(re.search('a.*',a))
'''<re.Match object; span=(0, 4), match='abcd'>'''
# print(re.search('c.*',a))
'''<re.Match object; span=(2, 4), match='cd'>'''
# print(re.search('d.*',a))
'''<re.Match object; span=(3, 4), match='d'>'''
#-----------------------------------------------------------

'''represent one or more character'''

# print(re.search('a.+',a))
'''<re.Match object; span=(0, 4), match='abcd'>'''
# print(re.search('c.+',a))
'''<re.Match object; span=(2, 4), match='cd'>'''
#------------------------------------------------------------

'''represent zero or one character'''

# print(re.search('a.?',a))
'''<re.Match object; span=(0, 2), match='ab'>'''
# print(re.search('c.?',a))
'''<re.Match object; span=(2, 4), match='cd'>'''
#------------------------------------------------------------

'''represent set of character'''

# print(re.search('[abcd]',a))
'''<re.Match object; span=(0, 1), match='a'>'''

# print(re.search('[a-z]',a))
'''<re.Match object; span=(0, 1), match='a'>'''
# print(re.search('[b-z]',a))
'''<re.Match object; span=(1, 2), match='b'>'''
b='ABCD'
# print(re.search('[A-Z]',b))
'''<re.Match object; span=(0, 1), match='A'>'''
c='ABCabc'
# print(re.search('[a-z]',c))
'''<re.Match object; span=(3, 4), match='a'>'''
d='1234'
# print(re.search('[0-9]',d))
'''<re.Match object; span=(0, 1), match='1'>'''
e='abc123'
# print(re.search('[a-z][0-9]',e))
'''< match='c1'>'''
# print(re.search('[a-z0-9]',d))
'''< match='1'>'''
# print(re.search('[a-z0-9]',a))
'''< match='a'>'''
# print(re.search('[a-z0-9]',e))
'''< match='a'>'''
# print(re.search('[a-z].*[0-9]',e))
'''< match='abc123'>'''
# print(re.search('[a-z].+[0-9]',e))
'''  "  '''
# print(re.search('[a-z].?[0-9]',e))
'''bc1'''
#----------------------------------------------------

'''number validation'''
# s='9961174177'         
# if len(s)==10 and re.search('[6-9].{9}',s) and s.isdigit():
#     print('valid')
# else:
#     print('not valid')  
'''valid'''  

# s='2296117410'         
# if len(s)==10 and re.search('[6-9].{9}',s) and s.isdigit():
#     print('valid')
# else:
#     print('not valid') 
'''not valid'''

m='anu@gmail.com'
print(re.search('^[a-z].*@gmail.com$',m))