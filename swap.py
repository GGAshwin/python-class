#swap 2 variables

a=int(input("Enter the value of first variable"))
b=int(input("Enter the value of second variable"))

def swap(a,b):
    return b,a

a,b=swap(a,b)

print(a,b)