import url, pycurl, urlparse, os
from StringIO import StringIO

from bs4 import BeautifulSoup
import re, math, time, random
import csv, sys

publisher_codes = []

with open('techstreet_publisher_codes.csv', 'rb') as csvfile:
    techstreet_pub_codes = csv.reader(csvfile, delimiter='|')
    for row in techstreet_pub_codes:
    	# print row
    	publisher_codes.append(row)
        # print ', '.join(row)
        # print row[0]
csvfile.close()

# print publisher_codes

# sys.exit()s

c = pycurl.Curl()

firefox_useragent = 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
chrome_useragent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36'
opera_useragent = 'Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.2.15 Version/10.00'
useragent_array = {"firefox":firefox_useragent, "chrome":chrome_useragent, "opera":opera_useragent}

base_page_url = "http://www.techstreet.com/"
page_number = "1"
page_extension = ".html"
path = os.getcwd()

# publisher_dict = 	#[{"publisher_name":"UL","publisher_id":"156","agent":"opera"},{"publisher_name":"UL_Canada","publisher_id":"157","agent":"chrome"}]#, \
# 					[{"publisher_name":"IEEE","publisher_id":"95","agent":"opera"}, {"publisher_name":"DIN","publisher_id":"69","agent":"chrome"}, \
# 					{"publisher_name":"IEC","publisher_id":"94","agent":"opera"}, {"publisher_name":"ETSI","publisher_id":"605","agent":"chrome"}, \
# 					{"publisher_name":"ANSI","publisher_id":"24","agent":"firefox"} ]

publisher_dict = []
<<<<<<< HEAD
for item in publisher_codes[1:]:
=======
for item in publisher_codes[62:]:
>>>>>>> 86472dc9e00c1dacfa1ae20c171ec3ca3d4193c4
	publisher_dict.append({'publisher_name':item[0],'publisher_id':item[1],'agent':"chrome"})

# print publisher_dict

# sys.exit()

# publisher_dict = 	[{"publisher_name":"IEC","publisher_id":"94","agent":"opera"}, \
# 					{"publisher_name":"ETSI","publisher_id":"605","agent":"chrome"},{"publisher_name":"ANSI","publisher_id":"24","agent":"firefox"}]

for publisher in publisher_dict:
	publisher_name = publisher["publisher_name"]
	publisher_id = publisher["publisher_id"]
	ua = publisher["agent"]
	useragent = useragent_array[ ua ]
	print useragent

	c.setopt(pycurl.USERAGENT, useragent)
	parameterUrl = "products?publisher_id="+publisher_id+"&sort_direction=asc&sort_order=doc_no&action=index&controller=products&sort_direction=asc&sort_order=doc_no&per_page=10"

	publisher_url = urlparse.urljoin(base_page_url, parameterUrl)
	print publisher_url
	publisher_path = os.path.join(path, publisher["publisher_name"])
	os.mkdir(publisher_path, 0777)
	
	page_name = publisher_id+"_"+page_number+page_extension
	file_path = os.path.join(publisher_path, page_name)
	c.setopt(pycurl.URL, publisher_url)
	# c.setopt(c.WRITEDATA, buffer)
	
	c.setopt(pycurl.WRITEDATA, file(file_path,"wb"))
	c.perform()

	# urlparse.urljoin(url1, url2)
	# body = buffer.getvalue()

	########### Document Counter ##############
	empty_array= []

	soup = BeautifulSoup(open(file_path))

	results_tag = soup.find(class_= "total_results")
	a = results_tag.contents[0].split(" ")
	b = float(a[0].replace(',',''))
	# print results_tag.contents
	# print b
	publisher.update({'count':b})
	per_page = 100
	pages = int(math.ceil(b/per_page))
	publisher.update({'page_count':pages})
	print publisher['count'], publisher['page_count']

<<<<<<< HEAD
	page_number_range = [1]


	for i in range(1,publisher['page_count']):
		# if i == 0:
		# 	pass
		# else:
=======

	for i in range(1,publisher['page_count']):
>>>>>>> 86472dc9e00c1dacfa1ae20c171ec3ca3d4193c4
		print i
		parameterUrl ="products?page="+str(i)+"&per_page="+str(per_page)+"&publisher_id="+publisher_id+"&sort_direction=desc+NULLS+LAST&sort_order=edition_date"
		publisher_url = urlparse.urljoin(base_page_url, parameterUrl)
		page_name = publisher_id+"_"+str(i)+page_extension
		file_path = os.path.join(publisher_path, page_name)
<<<<<<< HEAD
		print publisher_url
=======
>>>>>>> 86472dc9e00c1dacfa1ae20c171ec3ca3d4193c4
		c.setopt(pycurl.URL, publisher_url)
		# c.setopt(c.WRITEDATA, buffer)
		
		c.setopt(pycurl.WRITEDATA, file(file_path,"wb"))
		c.perform()
		time.sleep(random.randint(15, 120))
<<<<<<< HEAD


=======
>>>>>>> 86472dc9e00c1dacfa1ae20c171ec3ca3d4193c4
