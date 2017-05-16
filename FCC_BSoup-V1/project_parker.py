from bs4 import BeautifulSoup
from urllib import urlopen

# company_codes = ['K7S', 'ENN']
company_codes = ['K7S']

for code in company_codes:

	stash = []

	print 'Code: '+ code

	fccUrl = 'https://fccid.io/' + code
	fccPage = urlopen(fccUrl)

	gravy = BeautifulSoup(fccPage)

	grantee_name = gravy.find("div", class_="org")
	print grantee_name.get_text()
	stash.append(grantee_name.get_text())

	grantee_address_city = gravy.find("span", class_="locality")
	print grantee_address_city.get_text()
	stash.append(grantee_address_city.get_text())

	grantee_address_state = gravy.find("span", class_="region")
	print grantee_address_state.get_text()
	stash.append(grantee_address_state.get_text())	

	grantee_address_zip = gravy.find("span", class_="postal-code")
	print grantee_address_zip.get_text()

	grantee_country_name = gravy.find("div", class_="country-name")
	print grantee_country_name.get_text()

	grantee_code = 'Grantee Code: ' + code

	print gravy.find_all(text=grantee_code)[0].parent.parent.find_all('h5')[3].get_text()

	a = gravy.find_all('table', class_="table")[1].td.contents
	print a[0].get_text()
	print a[2]

	print len(gravy.find_all('div', class_="panel-body")[2].find_all('tr')) #number of applications
	b = gravy.find_all('div', class_="panel-body")[2].find_all('td')[1].contents
	print b[0], ":", b[2]

	# print gravy.find_all('table', class_="table")[1].a.get_text()

	applicationUrl = 'https://fccid.io/K7SF9K1105V2'
	applicationPage = urlopen(applicationUrl)
	soup = BeautifulSoup(applicationPage)

	# print soup.find_all('div', class_="panel-body")[0].contents
	print soup.find_all(title="Person at the applicant's address to receive grant or for contact")[0].find_all('td')[1].get_text()
	print soup.find_all(title="Person at the applicant's address to receive grant or for contact")[0].find_all('td')[3].get_text()
	print soup.find_all(title="Person at the applicant's address to receive grant or for contact")[0].find_all('td')[5].get_text()
	print soup.find_all(title="Person at the applicant's address to receive grant or for contact")[0].find_all('td')[7].get_text()

	print stash