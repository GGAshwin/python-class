import re
regex=re.compile(r'^X-\S*:([0-9.]+)')
text='X-sdjfj-skdjfd:0.654 units X-asf-fgh:7.49875'
numb=regex.findall(text)
print(numb)