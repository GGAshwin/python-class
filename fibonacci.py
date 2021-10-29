#read n and create a list of fibonacci numbers upto n
n=int(input())
l=[0,1]
def fibo(n):
    i=2
    while i<n:
        l.append(l[i-1]+l[i-2])
        i+=1
    return l
fibo(n)
print(l)