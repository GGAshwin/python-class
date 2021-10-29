import math

def root(num):
    return num**2,math.sqrt(num)

number=int(input('Enter a number'))

sqr,root=root(number)

print('Number is :%s\n Its square is:%s \n Its root is:%s'%(number,sqr,root))