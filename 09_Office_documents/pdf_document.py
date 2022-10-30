import PyPDF2

pdfFile = open('cuaet-factsheet-ukr.pdf', 'rb')
reader = PyPDF2.PdfReader(pdfFile)
print(reader.numPages)

page0 = reader.getPage(0)
page0text = page0.extractText()
print(page0text)

for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())

# ================================================

pdf1File = open('cuaet-factsheet-ukr.pdf', 'rb')
pdf2File = open('optionLanos.pdf', 'rb')
reader1 = PyPDF2.PdfFileReader(pdf1File, strict=False)
reader2 = PyPDF2.PdfFileReader(pdf2File, strict=False)
writer = PyPDF2.PdfFileWriter()

for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

outputFile = open('combined.pdf', 'wb')
writer.write(outputFile)
outputFile.close()
pdf1File.close()
pdf2File.close()
