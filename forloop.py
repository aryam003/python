# for i in range(6):
#     print(i)

# for i in range(2,6):
#     print(i)

# for i in range(2,10,3):
#     print(i)

# for i in range(3):
#     print('anu')

# s=int(input("enter starting no:"))
# e=int(input("enter ending no:"))
# sum=0
# for i in range(s,e+1):
#     sum+=i
# print(sum)    

# s=int(input("enter starting no:"))
# e=int(input("enter ending no:"))
# sum=0
# odd_sum=0
# normal_sum=0
# for i in range(s,e+1):
#     normal_sum+=i
#     if i%2==0:
#         sum+=i
#     else:
#         odd_sum+=i     
# print('sum:',sum)
# print('odd:',odd_sum)
# print('normal:',normal_sum)        

     
# a=int(input("enter a number"))
# for i in range(1,11):
#     print(i,'*',a,'=',i*a)    

# s=input("enter string:")
# rev=''
# for i in s:
#     rev=i+rev
# print(rev)    

# s=input("enter string:")
# for i in s:
#     print(i)

e=int(input("enter a number"))
factorial=1
for i in range(1,e+1):
    factorial*=i
print("factorial:",factorial)        