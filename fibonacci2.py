n=int(input())
f1,f2=0,1
count=0
if n<0:
    print("invalid")
elif n==0:
    count=f1
else:
    while count<n:
        print(f1)
        new=f1+f2
        f1=f2
        f2=new
        count +=1
