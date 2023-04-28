import sys
import csv
from subprocess import call


file = open('amp.csv','r')

data = list(csv.reader(file,delimiter=';'))
pages = []
for d in data:
    pages.append(d[0])

for p in pages:
    return_code = call(['amphtml-validator', p])
