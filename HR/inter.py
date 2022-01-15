n=int(input())
setE=set()

roll=input().split()
for i in roll:
    setE.add(i)
b=int(input())
setF=set()

roll=input().split()
for i in roll:
    setF.add(i)
print(len(setE.intersection(setF)))