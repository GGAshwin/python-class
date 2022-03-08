import re
regex=re.compile(r'(\d{3})(\s|-)?(\d{7})')
matchobj=regex.search('8660297576 ,1234567891')
# print(matchobj)   #for findall
print(matchobj.group())