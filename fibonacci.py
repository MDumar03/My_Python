num=int(input("Enter Any Number : "))

a=0
b=1

print(a,b,end=" ")



for i in range(2,num,1):
       c=a+b
       a=b
       b=c
       print(c,end=" ")
