freq={}
str='ashwinfdgsfda'
for i in str:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)