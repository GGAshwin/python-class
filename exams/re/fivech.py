import re
regex=re.compile(r'^a\w{3}z$')
print(regex.search('abc2z').group())