import PyPDF2

# Provide paths to PDF file to be merged
user_path = input("Drag PDF file inside this window to edit: ")
file_path = user_path.strip()

with open(file_path, 'rb') as root_file:
	reader = PyPDF2.PdfFileReader(root_file)
	# Select which page to rotate
	page = reader.getPage(0)
	# Select degree to rotate (note: ' - ' before degree will rotate page counterclockwise)
	page.rotateCounterClockwise(180)
	writer = PyPDF2.PdfFileWriter()
	writer.addPage(page)
	with open('new_pdf_file.pdf', 'wb') as new_file:
		writer.write(new_file)