# i=1
# while i<=5:
#     print(i)
#     i+=1

# i=int(input("enter starting number"))
# a=int(input("enter ending number"))
# while i<=a:
#     print(i)
#     i+=5
# i=1
# a=int(input("enter limit:"))
# while i<=a:
#     print("python")
#     i+=1

# i=int(input("enter starting number:"))
# e=int(input("enter ending number:"))
# sum=0
# while i<=e:
#     sum=sum+i
#     i+=1
# print('sum :',sum)    

# i=int(input("enter starting number:"))
# e=int(input("enter ending number:"))
# while i<=e:
#     if i%2==0:
#         print(i)
#     i+=1
    
# i=int(input("enter starting number:"))
# e=int(input("enter ending number:"))
# while i<=e:
#     if i%3==0:
#         print(i)
#     i+=1

# i=int(input("enter starting number:"))
# e=int(input("enter ending number:"))
# sum=0
# while i<=e:
#     if i%2==0:
#         sum+=i
#     i+=1
# print('sum :',sum)    

# i=int(input("enter starting number:"))
# e=int(input("enter ending number:"))
# sum=0
# while i<=e:
#     if i%2!=0:
#         sum+=i
#     i+=1
# print('sum :',sum)  
#   
# i=1
# a=int(input("enter a number:"))
# while i<=10:
#     print(i,'*',a,'=',i*a)
#     i+=1

# i=int(input("enter starting number:"))
# e=int(input("enter ending number:"))
# sum=0
# odd_sum=0
# normal_sum=0
# while i<=e:
#     normal_sum+=i
#     if i%2==0:     
#         sum+=i
#     else:
#         odd_sum+=i
#     i+=1
# print('even sum :',sum) 
# print('odd sum :',odd_sum) 
# print('normal sum :',normal_sum) 

# a=int(input("enter ending value:"))
# i=1
# factorial=1
# while i<=a:
#     factorial*=i
#     i+=1
# print('factorial:',factorial)    

# a=int(input("enter a number :"))
# rev=0
# while a>0:
#     d=a%10
#     # print(d)
#     rev=rev*10+d
#     a//=10
# print(rev)

# a=int(input("enter a number :"))
# rev=0
# while a>0:
#     d=a%10
#     # print(d)
#     rev=rev+d
#     a//=10
# print(rev)

# a=input('str:')
# l=len(a)
# i=0
# while i<l:
#     print(a[i])
#     i+=1
   

a=input("str:")
l=len(a)
i=0
rev=''
while i<l:
    rev=a[i]+rev
    i+=1
print(rev)    

