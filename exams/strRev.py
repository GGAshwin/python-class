import re


string=input()
rev=string[::-1]
# print(rev)
#pallindrome
if(string==rev):
    print("The string is pallindrome")
else:
    print("String is not a pallindrome")