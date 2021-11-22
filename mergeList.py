a=[]
b=[]
l1=input("Enter number of string:")
l2=int(input('Enter the number of integers:'))
i=0
while i < int(l1):
    str=input(('Enter a string:'))
    a.append([str])
    i+=1
i=0
while i<l2:
    integer=int(input('Enter an integer:'))
    b.append([integer])
    i+=1
print(a,b)
c=a+b
print(c)
c.sort()
print(c)