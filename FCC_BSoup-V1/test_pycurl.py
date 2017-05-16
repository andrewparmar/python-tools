import pycurl, re
from StringIO import StringIO
from bs4 import BeautifulSoup
from urllib import urlopen
 
fccUrl = 'https://fccid.io/K7S'
fccPage = urlopen(fccUrl)

gravy = BeautifulSoup(fccPage)

file_path = 'test2.html'

buffer = StringIO()
c = pycurl.Curl()
c.setopt(c.URL, 'https://fccid.io/K7S')
c.setopt(c.WRITEDATA, buffer)
# c.setopt(pycurl.WRITEDATA, file(file_path,"wb"))
c.perform()
c.close()

body = buffer.getvalue()
# Body is a string in some encoding.
# In Python 2, we can print it without knowing what the encoding is.
# print(body)

# soup = BeautifulSoup(open(file_path))
soup = BeautifulSoup(body)
# print soup

# company_name = soup.find_all(class_="panel-body")
# # print company_name
# jim = str(company_name)
# # print jim

# soup2 = BeautifulSoup(jim)
# company_name2 = soup.find_all('tr.')
# # print company_name2
# # test1 = soup.tr.th
# # print test1.string
# # jam = soup.find_all('')
# # print jam

# # test2 = soup.find(class_="pa")
# # print test2
# # print test2 
# # css_soup.find_all("p", class_="strikeout body")

# # test3 = soup.find_all(class_="panel-body")
# # test3 = soup.find_all()
# # print test3

# a_string = soup.find(string="Belkin International")
# a_string = soup.find_all('a')
# print a_string
# a_string.find_parent("tr")

# test = soup.body.div.div.div.table
# print test

letters = soup.find_all("div", class_="panel-body")

# file = open("newfile.txt", "w")
# file.write(letters[1].get_text())
# file.write(letters[2])

print letters[1].get_text()
# # print letters[2]
# print letters[3].get_text()
# # jim =  letters[3].td.find_all

# item = letters.findNext('th')
# print item


# jim = str(letters[2])


# soup2 = BeautifulSoup(jim)
# print soup2.find_all('th')


# import BeautifulSoup
# import requests

# html = requests.get("http://yahoo.com").text
# b = BeautifulSoup.BeautifulSoup(html)
# m = soup.find(id='masthead')
# item = m.findNext('ul')

grantee_name = soup.find("div", class_="org")
print grantee_name.get_text()

grantee_address_city = soup.find("span", class_="locality")
print grantee_address_city.get_text()

grantee_address_state = soup.find("span", class_="region")
print grantee_address_state.get_text()

grantee_address_zip = soup.find("span", class_="postal-code")
print grantee_address_zip.get_text()

grantee_country_name = soup.find("div", class_="country-name")
print grantee_country_name.get_text()

print soup.find_all(text='Registered')

