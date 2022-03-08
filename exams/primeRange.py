n=int(input("Enter endpoint:"))
p=[]

def prime(n):
    for i in range(2,n):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            p.append(i)

prime(n)
print(p)