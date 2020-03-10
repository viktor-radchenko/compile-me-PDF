import PyPDF2

pdf_document = input('Please, provide path to the PDF file: ')
watermark_document = input('Please, provide path to the watermark file: ')

# Create PDF reader objects from files
template = PyPDF2.PdfFileReader(open(pdf_document, 'rb'))
watermark = PyPDF2.PdfFileReader(open(watermark_document, 'rb'))

# Create PDF writer objects for output
output = PyPDF2.PdfFileWriter()

# Loop through the pages and apply watermark
for i in range(template.numPages):
	page = template.getPage(i)
	page.mergePage(watermark.getPage(0))
	output.addPage(page)

	# Write to a new file and save it
	with open('ANwtr.pdf', 'wb') as file:
		output.write(file)