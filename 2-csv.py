#!/usr/bin/python
import csv
import sys

#with open('data.csv') as fd:
#    data=[tuple(line) for line in csv.reader(fd)]

with open('data.csv') as fd:
    data=[list(line) for line in csv.reader(fd)]

print (data)
for row in data:
    print(row)

fd.close()
