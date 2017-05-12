#!/usr/bin/env python

''' Create list of all documents in a folder for analysis

User this script to get a complete analysis of all files in a folder.
The script will recursivley walk through nested folder as well.
The output is a csv file that includes filename, path, extension and size(in bytes).

'''
import os
import csv

PATH = "C:\Users\Andrew\Google Drive\_Archive"

# If you want to limit the scope to a specifc folders in a parent folder, list
# folder using the list below. See example
# folders = ['documents','pcitures','audio','video/my_videos']
folders_scope = ['']


with open('file-path-dump.csv', 'wb') as csvwritefile:
    spamwriter = csv.writer(csvwritefile, delimiter='|',quotechar='"', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Path|Filename|'])

    for folder_name in folders_scope:


        folder_PATH = PATH + folder_name + '\''      #Commnet out for Unix-based systems
        # folder_PATH = PATH + folder_name + '/'      # Comment out for Windows systems
        folder_PATH = PATH

        # for root, directories, filenames in os.walk('C:/Users/andrew/Box Sync/DIGI-ONRULE/ConnectPort X4/'):
        for root, directories, filenames in os.walk(folder_PATH):
            for filename in filenames:
                file_path = os.path.join(root,filename)

                star = []
                star.append(file_path)
                star.append(filename)
                name, extension = os.path.splitext(file_path)
                # print extension
                star.append(extension)
                # Taking care of special character in file names
                for special_chr in ['`','*','|','?',',',';',':','<','>','[',']','{','}','!','$','(',')','/','@','#']:
                    filename = filename.replace(special_chr,'_')        # Comment out this line if you want to KEEP special characters in document_name
                    # print filename

                star.append(filename)
                try:
                    statinfo = os.stat(file_path)
                    star.append(statinfo.st_size)
                except Exception:
                    pass

                # print os.path.join(root,filename)

                print star
                spamwriter.writerow(star)
                # spamwriter.writerow(star)
