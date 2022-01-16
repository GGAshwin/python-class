import time
for i in range(2,5+1):
    print('i:'+str(i))
    for j in range(2,i):
            print("i:"+str(i)+" j:"+str(j))
            if(i%j)==0:
                time.sleep(2)
                print('i%j condition is true')
                break
    else:
        print(i)
        time.sleep(2)
        print(str(i)+" is a prime")