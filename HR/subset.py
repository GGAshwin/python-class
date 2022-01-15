n=int(input())
for i in range (0,n):
    a=int(input())
    seta=set()
    vala=input().split()
    for j in vala:
        seta.add(j)
    b=int(input())
    setb=set()
    valb=input().split()
    for k in valb:
        setb.add(k)
    print(seta.issubset(setb))