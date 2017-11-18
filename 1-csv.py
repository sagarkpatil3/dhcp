#!/usr/bin/python
import csv
import sys

fd = 0

try:
    fd = open('data.csv', 'rt')

except IOError as e:
    print ("I/O error({0}): {1}".format(e.errno, e.strerror))
    #print "%d %s" % (e.errno, e.strerror)
    exit(1)


data_list = []

reader = csv.reader(fd)

print ("reader type :", type(reader))
print (next(reader))
print (next(reader))
'''
'''

for row in reader:
    print (row)
    data_list.append(row)

print (data_list)

print ("-" * 20)
for row in data_list:
    print (row)

print ("-" * 20)
print (data_list[0])
print (data_list[1])

print (data_list[0][0])
print (data_list[1][0])

if  (int(data_list[0][0]) > int(data_list[1][0])):
    t = data_list[0]
    data_list[0] = data_list[1]
    data_list[1] = t

print ("-" * 20)
print ("data_list[0] :", data_list[0])
print ("data_list[1] :", data_list[1])

print ("-" * 20)
for row in data_list:
    print (row)

fd.close()

exit(1)

