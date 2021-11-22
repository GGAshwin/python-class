pnum=nnum=zero=0
while True:
    n=input('Enter a number: ')
    if n=='done':
        break
    elif int(n)>0:
        pnum+=1
    elif int(n)<0:
        nnum-=1
    elif int(n)==0:
        zero+=1
    else:
        print('Invalid input')
print(pnum,nnum,zero)
    