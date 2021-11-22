import re
sentph='tel number is 824-2496548'
phobj=re.compile(r'(\d{3,4})-(\d{7}) | (\d{10})')
matchobj=phobj.search(sentph)
if matchobj:
    print(matchobj.group())
else:
    print('not found')