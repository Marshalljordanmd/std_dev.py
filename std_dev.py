#a program to analyze the chromosome data file for continuity. 
#info sought in this is the mean distance between variant positions and the SD of the mean. Max distance. Position of 1st and last variant.


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

file = input('name of file = ')
D = 0
s = 0
next = [] #a list of distances between variant positions
n=0
last_dist = 0
total_rows = 0
gaps = 0
end_file = False

#os.remove('new_file')

with open(file,'r') as big:
	
	for j in range(0,50000000):
		l= big.readline()
		if l =='':
			end_file = True
			n=5000
			
		
			
		with open('new_file','a') as new:
			new.write(l)
			n=n+1
			if n > 5000:
				data_raw= pd.read_csv('new_file', sep='\t', header=None,comment='#',low_memory=False)
				rows= data_raw.shape[0]
				position = data_raw.iloc[ : ,1]
				print('j = ',j)
	
				for i in range(0,rows):
					if i == 0 and last_dist == 0:
						distance = 0
							
					elif i == 0 and last_dist != 0:
						distance = abs(position[0] - last_dist)
							
					else:
						distance = abs(position[i] - position[i-1])
	
					
					if distance > 1000000:#gaps over 1 million are the centromere, except the Y has 2 gaps over 1 million
					    print('distance = ',distance)
					    print('position = ',position[i],' - ', position[i-1])
					    gaps = gaps + distance
					else:
						next.append(distance)
						D = D + distance
						total_rows = total_rows +1
						
					if i == rows - 1:
						last_dist = position[i]
					
				n = 0
				os.remove('new_file')
				if end_file == True:
				
					mean = D / (total_rows -1)
					sum = 0
					
					for j in range(1,total_rows):
						s =(abs(next[j] - mean))**2
						sum = sum + s
	
					argument = ((1/(total_rows-1))*sum)	
					std_dev = (argument)**(.5)
				
					print('N = ', total_rows)
					print('mean of distances = ',mean)
					print('standard deviation = ', std_dev)
					print('gaps = ', gaps)
