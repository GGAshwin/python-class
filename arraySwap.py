#Write a function to swap 2 array elements
def swap(a,i,j):
    t=a[i]
    a[i]=a[j]
    a[j]=t
    return a

a=[]
n=int(input())
for i in range(n):
    a.append(int(input()))
swap(a,0,3)
print(a)
i=0
for i in range(0,n-1):
    min=i
    for j in range()