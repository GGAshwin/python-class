import json

file=open('test.json','w')

string='{"name":"Ash","age":20}'
val=json.loads(string)
print(val)