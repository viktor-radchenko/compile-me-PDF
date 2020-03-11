import PyPDF2
import sys


# Provide paths to PDF file to be merged
pdf_list = sys.argv[1:]


def pdf_merger(pdf_list):
	# Merge PDFs
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		print(pdf)
		merger.append(pdf)
	merger.write('merged.pdf')


pdf_merger(pdf_list)