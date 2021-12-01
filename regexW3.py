import re
from typing import Text
'''regular=re.compile(r'(\w{3})[-]?(\d{2})|ashwin')
text=input('Enter a string')
searchobj=regular.search(text)
if searchobj.group():
    print('pattern found')
    if searchobj.groups()!=(None,None):
        print(searchobj.groups())
    elif searchobj.group:
        print(searchobj.group())
else:
    print(text+' not found')
print(searchobj.group(0),searchobj.group(1))'''


'''regex=re.compile(r'[a-z]')
Text=input('Enter a string')
find=regex.findall(Text)
print(find)'''

regex=re.compile(r'(\d{3})-(\d{3})-(\d{4})')
Text=input('Enter a string')
find=regex.findall(Text)
print(find)

