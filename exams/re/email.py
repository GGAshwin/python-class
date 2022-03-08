import re
regex=re.compile(r'''
[a-zA-Z%_.]+
@
[a-zA-Z%_]+
\.
[a-zA-Z]{2,4}
''',re.VERBOSE)

obj=regex.search('firstname.initial@domain.com').group()
print(obj)