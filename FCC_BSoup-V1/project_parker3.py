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
csvfile.close()

# print company_codes
# company_codes = ['K7S', 'GBU']
# company_codes = ['ENN','GBU','2AB8Z','SU2','QZE','QTA','UEZ','TMN','VOB','R4V','Z2E','OWS','SSH','A2O']

ignore_list = []

with open('eggs.csv', 'wb') as csvwritefile:
	spamwriter = csv.writer(csvwritefile, delimiter='|',quotechar='"', quoting=csv.QUOTE_MINIMAL)
	spamwriter.writerow(['Code|Company Name|Address|Registration Date|Nuber of Applications|Last Application Date|Equipment Type|Applicatiion ID|'])

	mycount = 0

	for code in company_codes:

		mycount +=1
		print "Serial count:", mycount

		# if code not in ignore_list:
		stash = []

		stash.append(code)
		print 'Code: '+ code

		fccUrl = 'https://fccid.io/' + code
		print fccUrl
		fccPage = urlopen(fccUrl)
		gravy = BeautifulSoup(fccPage)

		# Get company name and address from vcard div.
		company_name = gravy.find_all("div", class_="vcard")[0].h1.div.get_text()		# Company name
		stash.append(company_name)
		print company_name
		# print gravy.find_all("div", class_="vcard")[0].h4.get_text()					# Grantee Code
		addy = gravy.find_all("div", class_="vcard")[0].find_all('h5')[0].get_text() \
			+ gravy.find_all("div", class_="vcard")[0].find_all('h5')[1].get_text() \
			+ gravy.find_all("div", class_="vcard")[0].find_all('h5')[2].get_text()		# Address
		print addy
		stash.append(addy)
		registration_date = gravy.find_all("div", class_="vcard")[0].find_all('h5')[3].get_text()		# Registration date and applicant name
		stash.append(registration_date)


		# # Registration date and name of applicant
		# grantee_code = 'Grantee Code: ' + code
		# print gravy.find_all(text=grantee_code)[0].parent.parent.find_all('h5')[3].get_text()

		count = len(gravy.find_all('div', class_="panel-body")[2].find_all('tr')) 		# Total Number of applications
		print count
		stash.append(count)

		if count > 1:
			a = gravy.find_all('table', class_="table")[1].td.contents						# Latest grant application
			# print a[0].get_text()															# Application Number for user in next curl
			print a[2]																		# Application date
			stash.append(a[2])
			


			b = gravy.find_all('div', class_="panel-body")[2].find_all('td')[1].contents	# Equipment type
			equipment_type = b[0:len(b)]																
			# print b[0], ":", b[2]
			print equipment_type
			stash.append(equipment_type)

			application_id = gravy.find_all('table', class_="table")[1].a.get_text()		# Applicaiton id
			stash.append(application_id)

			applicationUrl = 'https://fccid.io/' + application_id
			print applicationUrl
			stash.append(applicationUrl)
			applicationPage = urlopen(applicationUrl)
			soup = BeautifulSoup(applicationPage)

			# print "test"

			s = soup.find_all(title="Person at the applicant's address to receive grant or for contact")[0].find_all('td')
			print len(s)

			applicant_name = soup.find_all(title="Person at the applicant's address to receive grant or for contact")[0].find_all('td')[1].get_text()		# Name of latest applicant
			stash.append(applicant_name)
			print applicant_name

			i = 0

			cbeck = []

			if len(s)>2:
				if i < (len(s) + 1) and stash[-1] != "Email":
					# t
					print soup.find_all(title="Person at the applicant's address to receive grant or for contact")[0].find_all('td')[i].get_text()
					stash.append(soup.find_all(title="Person at the applicant's address to receive grant or for contact")[0].find_all('td')[i].get_text())
					# else:
					# 	pass

					# try/:/
					# 	print soup.find_all(title="Person at the applicant's address to receive grant or for contact")[0].find_all('td')[i].get_text()
					# 	stash.append(soup.find_all(title="Person at the applicant's address to receive grant or for contact")[0].find_all('td')[i].get_text())
					# except Exception, e:
					# 	raise
					# else:
					# 	pass
					# finally:
					# 	pass
					i += 1

			# if len(s)>2:
			# 	print soup.find_all(title="Person at the applicant's address to receive grant or for contact")[0].find_all('td')[2].get_text()
			# 	print soup.find_all(title="Person at the applicant's address to receive grant or for contact")[0].find_all('td')[3].get_text()
			# 	print soup.find_all(title="Person at the applicant's address to receive grant or for contact")[0].find_all('td')[4].get_text()
			# 	print soup.find_all(title="Person at the applicant's address to receive grant or for contact")[0].find_all('td')[5].get_text()
			# 	print soup.find_all(title="Person at the applicant's address to receive grant or for contact")[0].find_all('td')[6].get_text()
			# 	print soup.find_all(title="Person at the applicant's address to receive grant or for contact")[0].find_all('td')[7].get_text()
			# 	print soup.find_all(title="Person at the applicant's address to receive grant or for contact")[0].find_all('td')[8].get_text()

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
		else:
			ignore_list.append(code)

print ignore_list
