import PyPDF4 as PDFReader
import PIL as ImageReader
import fitz

def Main2():
	ReadPDF = PDFReader.PdfFileReader(open('Chess_Guide.pdf', 'rb'))
	Page = ReadPDF.getPage(13)
	print(type(Page))
	Text = Page.extractText()
	print(Text)
	# GetBook.close()

def Main1():
	doc = fitz.open('Chess_Opening_Essentials.pdf', 'rb')
	for i in range(len(doc)):
		for img in doc.getPageImageList(i):
			xref = img[0]
			pix = fitz.Pixmap(doc, xref)
			if pix.n < 5:
				pix.writePNG("p%s-%s.png" % (i, xref))
			else:
				pix1 = fitz.Pixmap(fitz.csRGB, pix)
				pix1.writePNG("p%s-%s.png" % (i, xref))
				pix1 = None
			pix = None

Main2()