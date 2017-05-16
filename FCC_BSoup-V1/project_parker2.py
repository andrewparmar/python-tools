from bs4 import BeautifulSoup
from urllib import urlopen
import csv

company_codes = []

with open('fcc_scraping_customer_codes.csv', 'rb') as csvfile:
    fcc_codes = csv.reader(csvfile, delimiter='|')
    for row in fcc_codes:
    	company_codes.append(row[0])
        # print ', '.join(row)
        # print row[0]

# print company_codes
# company_codes = ['K7S', 'GBU']
# company_codes = ['GBU','2AB8Z','SU2','QZE','QTA','UEZ','TMN','VOB','R4V','Z2E','OWS','SSH','A2O']

ignore_list = ['ENN','GYS']

with open('eggs.csv', 'wb') as csvwritefile:
	spamwriter = csv.writer(csvwritefile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
	spamwriter.writerow("test")

	for code in company_codes:

		if code not in ignore_list:
			stash = []

			stash.append(code)
			print 'Code: '+ code

			fccUrl = 'https://fccid.io/' + code
			fccPage = urlopen(fccUrl)
			gravy = BeautifulSoup(fccPage)

			# Get company name and address from vcard div.
			company_name = gravy.find_all("div", class_="vcard")[0].h1.div.get_text()		# Company name
			stash.append(company_name)
			# print gravy.find_all("div", class_="vcard")[0].h4.get_text()					# Grantee Code
			print gravy.find_all("div", class_="vcard")[0].find_all('h5')[0].get_text() \
				+ gravy.find_all("div", class_="vcard")[0].find_all('h5')[1].get_text() \
				+ gravy.find_all("div", class_="vcard")[0].find_all('h5')[2].get_text()		# Address
			
			print gravy.find_all("div", class_="vcard")[0].find_all('h5')[3].get_text()		# Registration date and applicant name

			# # Registration date and name of applicant
			# grantee_code = 'Grantee Code: ' + code
			# print gravy.find_all(text=grantee_code)[0].parent.parent.find_all('h5')[3].get_text()

			print len(gravy.find_all('div', class_="panel-body")[2].find_all('tr')) 		# Total Number of applications


			a = gravy.find_all('table', class_="table")[1].td.contents						# Latest grant application
			# print a[0].get_text()															# Application Number for user in next curl
			print a[2]																		# Application date


			b = gravy.find_all('div', class_="panel-body")[2].find_all('td')[1].contents	# Equipment type
			print b[0:len(b)]																
			# print b[0], ":", b[2]

			application_id = gravy.find_all('table', class_="table")[1].a.get_text()		# Applicaiton id

			applicationUrl = 'https://fccid.io/' + application_id
			print applicationUrl
			applicationPage = urlopen(applicationUrl)
			soup = BeautifulSoup(applicationPage)

			# print "test"

			s = soup.find_all(title="Person at the applicant's address to receive grant or for contact")[0].find_all('td')
			print len(s)

			print soup.find_all(title="Person at the applicant's address to receive grant or for contact")[0].find_all('td')[1].get_text()		# Name of latest applicant

			# try:
			# 	print soup.find_all('div', class_="panel-body")[0].contents
			# 	# print soup.find_all(title="Person at the applicant's address to receive grant or for contact")[0].find_all('td')[1].get_text()
			# 	# print soup.find_all(title="Person at the applicant's address to receive grant or for contact")[0].find_all('td')[2].get_text()
			# 	# print soup.find_all(title="Person at the applicant's address to receive grant or for contact")[0].find_all('td')[5].get_text()
			# 	# print soup.find_all(title="Person at the applicant's address to receive grant or for contact")[0].find_all('td')[7].get_text()
			# except Exception, e:
			# 	raise
			# else:
			# 	pass


			print stash

			spamwriter.writerow(stash)

			print "------------------------------"