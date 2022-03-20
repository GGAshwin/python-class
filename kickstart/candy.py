from json.tool import main


testCases=int(input())
mainList=[]
for i in range(testCases):
    for j in range(2):
        N=int(input())
        M=int(input())
        for k in range(N):
            l=list()
            l.append(int(input()))
        mainList.append(l)
print(mainList)