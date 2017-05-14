from bs4 import BeautifulSoup
import re
import os
import os.path
import glob
import pickle
import csv

csvwritefile = open('techstreet_compiled_standards.csv', 'wb')


directories = []

files_in_dir = os.listdir(os.getcwd())
for file_in_dir in files_in_dir:
    if len(file_in_dir) <= 10:
        directories.append(file_in_dir)

# directories.remove(".svn")

print directories
filelist = []

root = os.getcwd()

# <<<<<<< HEAD
counter = 0

for i in directories:
    for item in os.listdir(os.path.join(root, i)):
        print "test print:", item
        if os.path.isfile(os.path.join(root, i, item)):
            print item
            filelist.append(os.path.join(i, item))
            print filelist[-1]
            counter += 1
            print counter
# =======
for i in directories:
    for item in os.listdir(os.path.join(root, i)):
        if os.path.isfile(os.path.join(root, i, item)):
            print item
            filelist.append(os.path.join(i, item))
# >>>>>>> 86472dc9e00c1dacfa1ae20c171ec3ca3d4193c4

# print filelis
print "Done with creating filelist from all folders..."


standards_array = []
# <<<<<<< HEAD
counter = 0

print "Starting to soup..."
for x in filelist:
    soup = BeautifulSoup(open(x))
    counter += 1
    
    # print x
    print counter
# =======

# for x in filelist:
# 	soup = BeautifulSoup(open(x))
# # >>>>>>> 86472dc9e00c1dacfa1ae20c171ec3ca3d4193c4

    a_tag = soup.select("h3 > a")

    # print type(a_tag[1])

    for item in a_tag:
        e = item.contents[0].replace("\n\t\t\t\t\t", "")
        x = x.replace("/","|")
        # print x
        # break
        # e = e.replace("\n\t\t\t\t\t", "")
        # print e
        # bucket = [str(e), str(x)]
        try:
            csvwritefile.write(str(e))
            csvwritefile.write("|")
            csvwritefile.write(str(x))
            csvwritefile.write("\n")
        except:
            print "Couldn't write to csv", e
            pass
        # print "test"

        # break
        # standards_array.append(str(e))
    # break

# # print standards_array
# print "Creating pickle..."
# pickle.dump(standards_array, open("scraped_standards.pkl", "wb"))
# print "Pickle done..."

# for standard in standards_array:
# 	csvwritefile.write(standard)
