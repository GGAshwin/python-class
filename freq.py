import pprint
str='ashwinprabhu'
d=dict()
for c in str:
    d.setdefault(c,0)
    d[c]=d[c]+1
pprint.pprint(d)