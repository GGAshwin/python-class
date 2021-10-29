#write a program to calculate the factorial of a number and calculate binomial coefficient

def factorial(num):
    if(num==0):
        return 1
    elif(num==1):
        return 1
    else:
        return num*factorial(num-1)

num=int(input("Enter a number"))
ans=factorial(num)
print(ans)

r=int(input('Enter value of r'))

ncr=factorial(num)/(factorial(num-r)*factorial(r))
print(ncr)