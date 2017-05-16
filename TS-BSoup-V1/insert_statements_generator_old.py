import pickle

curled_pages = pickle.load(open("scraped_standards.pkl","rb"))

# print curled_pages

sql_file = open('techstreet_scraped.sql', 'w+')

table_name = "standards"
values = ""
standard_id = 1001

for item in curled_pages:
	# insert_command = "INSERT INTO " + table_name+" "+values+" "+item+"\r"
	a = item.replace("'", "\\'")
	insert_command = "insert into standard_master (standard_id,standard_name) values("+str(standard_id)+", '"+item+"');\r"
	sql_file.write(insert_command)
	standard_id += 1