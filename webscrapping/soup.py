import bs4,requests
res=requests.get('https://adithyapai.com/')
soup=bs4.BeautifulSoup(res.text)
htmlfile=open('test.html')
htmlsoup=bs4.BeautifulSoup(htmlfile)
