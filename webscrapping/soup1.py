import bs4
file=open('test.html')
#soup=bs4.BeautifulSoup(file.read(),features="html.parser")
soup=bs4.BeautifulSoup(file,features="html.parser")
ele=soup.select('.div')
print(ele[0].get('class'))