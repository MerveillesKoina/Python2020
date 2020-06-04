#Create a program to check if a number is even or odd
#May2020
#Practice
#Author: Merveille Guidingar Koina

import os 

os.system('clear')


print('\tOdd Even Program:\n')

number=int(input('Enter a number: '))

if(number % 2 ==0):
	print(number,'is Even.')
else:
	print(number,'is Odd.')
