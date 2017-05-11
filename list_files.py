import os
import csv

# folders = ['ConnectPort X4','ConnectPort X2E','WVA','']
# folders = ['ConnectPort X2e','ConnectPort X4','WVA','Connect Sensor','ConnectPort X2','XTrack','XBee Sensor','TC63i']
folders = ['']


with open('file-path-dump.csv', 'wb') as csvwritefile:
    spamwriter = csv.writer(csvwritefile, delimiter='|',quotechar='"', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Path|Filename|'])

    for folder_name in folders:

        PATH = "C:\Users\Andrew\Box Sync\DIGI-ONRULE"
        # folder_PATH = PATH + folder_name + '/'
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