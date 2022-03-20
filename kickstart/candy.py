testCases=int(input())
mainList=[]
for i in range(testCases):
        n=input().split()
        N=int(n[0])
        M=int(n[1])
        for k in range(N):
            l=list()
            l.append(int(input()))
        mainList+=l
print(mainList)
