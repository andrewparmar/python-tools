from bs4 import BeautifulSoup
import re

empty_array= []

soup = BeautifulSoup(open('UL/156_1.html'))

results_tag = soup.find(class_= "total_results")
a = results_tag.contents[0].split(" ")
b = int(a[0].replace(',',''))
print results_tag.contents
print b

