#May2020
##Write a program to display the prime numbers
#Author: Merveille Guidingar Koina


import os

os.system('clear')


for Number in range(1,50):
	count = 0
	for i in range(2, (Number//2 + 1)):
		if(Number % i ==0 ):
			count +=1
			break

	if(count==0 and Number!=0):
		print("%d"%Number, end=' ')