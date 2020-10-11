import PyPDF2

Mypdf = PyPDF2.PdfFileReader("CSE catalogue.pdf")
numberOfPages = Mypdf.getNumPages()
print(numberOfPages)
# print(Mypdf.getPage(4).extractText())   - This prints the text present in the exact page.

str =""
for i in range(numberOfPages):
    str = str + (Mypdf.getPage(i).extractText())

with open("output.txt" , 'w') as f :
    f.write(str)