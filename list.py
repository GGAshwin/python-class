l=['a','b','c','ashwin']
print(l)
m=list([1,2,3,4,6,7,8,9])
print(m)
for i in l:
    print(i)
print('*')
for i in range(len(m)):
    print(m[i])

#negative index
print('*')
print(len(l[-1]))
print('*')
print(m[3:6])