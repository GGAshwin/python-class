import re
sent="my tel no is 91-0824-1234567 "
telobj=re.compile(r'(\d(2)-)?(\d{3})-(\d{7})')
telmat=telobj.search(sent)
if(telmat):
    print(telmat.group())
else:
    print('no match')