import csv
import json


def read_data_file(filename,delim):
	data = []

	with open(filename, 'rb') as csvfile:
		data_list = csv.reader(csvfile, delimiter=delim, quotechar='^')
		for row in data_list:
			data.append(row)

	return data


def create_json(data_array):
	counter = 0

	json_array = []

	# 1. Read item from data array
	for item in data_array[1:]:

		counter += 1
		print counter

	# 1.5. Initialize attributes. Create attributes accroding to your csv column names.
		path = []
		document_name = []
		document_actual_name = []
		family_name = []
		product_id = []
		product_name = []
		document_type_id = []
		document_type_name = []
		country_id = []
		country_name = []
		tag = []
		tag = []
		tag = []
		tag = []

	# 2. Split item	into attributes
		# print "item:",item[0]
		path.append(item[0].replace('\\','/'))
		# print "path:",path[0]
		
		# Taking care of special character in file names
		for special_chr in ['`','*','|','?',',',';',':','<','>','[',']','{','}','!','$','(',')','/']:
			item[1] = item[1].replace(special_chr,'_')		# Comment out this line if you want to KEEP special characters in document_name
			# print item[1]
			item[2] = item[2].replace(special_chr,'_')		# Comment out this line if you want to KEEP special characters in document_actual_name
			# print item[2]

		document_name.append(item[1])
		document_actual_name.append(item[2])
		family_name.append(item[3])
		product_id.append(item[4])
		product_name.append(item[5])
		document_type_id.append(item[6])
		document_type_name.append(item[7])
		country_id.append(item[8])
		country_name.append(item[9])
		cup = []
		for a in item[10:13]:
			cup.append(a)
		tag=json.dumps(cup)

		# break
	
	# 3. Insert into json format
		json_statement ='[{"parent_document_id":"","document_name":"%s","document_actual_name":"%s","docDescription":"","audit_status":0,"family_name":["%s"],"product_id":["%s"],"product_name":["%s"],"document_type_id":"%s","document_type_name":"%s","country_id":["%s"],"country_name":["%s"],"grant_date": "","expiry_date": "","tags":%s,"issuedby":[],"standard_id":["0_%s_Not discipline specific"],"standard_name":["Not standard specific"],"discipline":["0"],"discipline_code":["Not discipline specific"],"physical_path":"%s","user_id":"1","login_id":"digi@onrule.com","user_name":"OnRule Admin"}]' \
		% (document_name[0],document_actual_name[0],family_name[0],product_id[0],product_name[0],document_type_id[0],document_type_name[0],country_id[0],country_name[0],tag,country_name[0],path[0])

		# print json_statement
		json_array.append(json_statement)
		final_json = (str(json_array)).replace("'[","[").replace("]'","]")

		# break

	# 4. Write to external file
	# print final_json
	f = open('digi_upload-data_json.txt', 'w')
	f.write(final_json)
	f.close()


def test_run(data):
	for item in data:
		print type(item[2])


pipe_delim = '|'
csv_master_file = 'sample-data-for-json.csv'

data = read_data_file(csv_master_file,pipe_delim)
json = create_json(data)

# test_run(data)
