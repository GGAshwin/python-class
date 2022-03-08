def computeGCD(x, y):
    while(y):
        x, y = y, x % y
        return x

x=int(input())
y=int(input())
print(computeGCD(x,y))