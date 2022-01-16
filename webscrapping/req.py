import requests
req=requests.get('https://nodejs.medium.com/')
# print(req.status_code)
print(req.text[:100])