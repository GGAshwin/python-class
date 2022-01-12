'''Write a Python program to create a list of prime numbers between a given range'''
import sys
lst=[]
s=int(input("Enter starting point:"))
e=int(input("Enter ending point:"))


if(s==1):
    s+=1
elif(s==0):
    s=2
if(e<s):
    print('\n---End cannot be larger than beginning---\n')
    sys.exit()
for i in range(s,e+1):
    for j in range(s,i):
        if (i%j==0):
            break
    else:
        lst.append(i)
print(lst)