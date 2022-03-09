# import requests module
import requests
  
# Making a get request
response = requests.get('https://medium.com/@mertcanarguc/15-javascript-codes-you-will-always-need-e8569903dd1')
  
# print response
print(response)
  
# print iter_content data
print(response.iter_content())

# print(response.content)

# iterates over the list
for i in response.iter_content(1000):
    print(i)