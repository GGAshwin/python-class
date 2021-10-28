from typing import Counter


s="ashwin"
ss="win"
ml=len(s)
sl=len(ss)
count=0
for i in range(ml-sl+1):
    if(s[i:i+sl]==ss):
        count+=1
print(count)