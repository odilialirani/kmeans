#!/usr/bin/python

'''
Purdue CS 390 - Fall 2016
Odilia Lirani
0027603470
HW 4
Prof. Dan Goldwasser
'''

import sys, csv, random, math
import numpy as np

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
	tabRow = []
	#data = np.array()
	data = []
	centroids = []
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
				# this will eliminate the column names row
				counter += 1
				continue
			for a in line[0].split(','):
				tabRow.append(a);
			#print tabRow[3], ',', tabRow[4], ',', tabRow[6], ',', tabRow[7]
			data.append([tabRow[3], tabRow[4], tabRow[6], tabRow[7]])
			tabRow[:] = []
		# Select k random points
		for i in range(int(k)):
			index = random.randint(0, len(data)-1)
			centroids.append(data[index])
		
		while (True):
			# TODO: Change the while loop condition
			for i in range(len(data)):
				# Reassign points to the closest , use Euclidean mean
				nearest = sys.float_info.max
				for j in centroids:
					# Calculate the distance
					s = 0;

					for w in range(4) :
						s = s + math.pow((float(j[w]) - float((data[i])[w])), 2)
					dist = math.sqrt(s)
					print dist
				break
			break





