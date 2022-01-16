'''Write a Python program to create a list of prime numbers between a given range'''
try:
    lst=[]
    s=int(input("Enter starting point:"))
    e=int(input("Enter ending point:"))
    if(s==1):
        s+=1

    elif(s==0):
        s=2

    #if the user has provided reverse values
    if(e<s):
        temp=s
        s=e
        e=temp
        print('The endpoints are swapped')

    for i in range(s,e+1):
        for j in range(2,i):
            if (i%j==0):
                break
        else:
            lst.append(i)

    #if the only value in the list is 1
    if(len(lst)==1 and lst[0]==1):
        lst=[]
    print(lst)
except:
    print("Invalid input")