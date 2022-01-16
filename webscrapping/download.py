import requests
res=requests.get('https://adithyapai.com/')
res.raise_for_status()
file=open('node.txt','wb')
for i in res.iter_content(10000):
    file.write(i)