#!/usr/bin/python

'''
Purdue CS 390 - Fall 2016
Odilia Lirani
0027603470
HW 4
Prof. Dan Goldwasser
'''

import sys
import csv

# Need to store latitude, longitude, revCount, checkins to calc centroid
# 7 (lat) 8 (long) 10 (revCount) 11 (checkins)
# to find the centroids, we need to calculate the 

arguments = sys.argv
if (len(arguments) < 3):
	print "Invalid arguments"
else:
	dataFile = arguments[1]
	k = arguments[2]
	counter = 0
	data = []
	o = 0
	skip = True;
	with open(dataFile, 'rU') as file:
		reader = csv.reader(file, dialect=csv.excel_tab)
		for line in reader:
			'''if (skip):
				skip = False
				continue
			counter += 1
			print line[0]
			for a in line[0].split(',') :
				data.append(a)
			# make sure to do this twice
			if (counter == 2) :
				counter = 0
				print data[7], ',', data[8], ',', data[10], ',', data[11]
				data = []'''
			if (counter == 0):
				counter += 1
				continue
			for a in line[0].split(','):
				data.append(a);

			if (counter > 1):
				counter = 1
				# DO SOMETHING HERE
				print data[7], ',', data[8], ',', data[10], ',', data[11]
				data[:] = []
				continue
			counter += 1
		
	'''with open(dataFile, 'rb') as file:
		r = csv.reader(open(self.file, 'rU'), dialect=csv.excel_tab)
		for row in r:
			print row
	for num,line in enumerate(lines, 1):
			print line.split()
			print '\n'
			break
	tabHeader = next(reader)
		ite = True
		while (ite == True):
			for i in range(0, 2):
				line = next(reader)
				for num, l in enumerate(line, 1):
					print l
				if (line == ''):
					ite == False
					break
				#print line
	'''