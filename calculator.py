#program for calculator


def calci(a,op,b):
    if(op=='+'):
        return a+b
    elif(op=='-'):
        return a-b
    elif(op=='*'):
        return a*b
    elif(op=='/'):
        if(b==0):
            return 'divide by zero'
        return a/b
    elif(op=='%'):
        return a%b
    else:
        return 'Invalid operator'

a=int(input("Enter an operand"))
op=str(input("Enter an operator"))
b=int(input("Enter an operand"))
ans=calci(a,op,b)
print(ans)