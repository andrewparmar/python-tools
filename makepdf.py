import csv
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

with open('file-path-dump.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:
		print(row[0], row[1])
		try:
			os.makedirs(row[0])
		except Exception as e:
			pass

		file_path = os.path.join(row[0],row[1])
		
		c = canvas.Canvas(file_path, pagesize=letter)
		c.setFont("Helvetica-Bold", 40)

		c.drawCentredString(300, 600, "Sample File")
		c.setFont("Helvetica", 30)
		c.drawCentredString(300, 550, "Content")
		c.drawCentredString(300, 500,  "Expiration: MM-DD-YYYY")
		c.save()

		# break

