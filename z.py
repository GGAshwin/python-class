#print z pattern of stars
for row in range(5):
    for column in range(5):
        if(row==0 or row==4 or row+column==4):
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()