l=['x','y','z','a','b']
for i in range(len(l)):
    print(l[0:i+1])
print('*')
for i in range(len(l)+1,0,-1):
    print(l[len(l)-i:len(l)])