import PyPDF2

obj=open('Module 4.pdf','rb')
pdfreader=PyPDF2.PdfFileReader(obj)
page0=pdfreader.getPage(0)
print(page0.extractText())