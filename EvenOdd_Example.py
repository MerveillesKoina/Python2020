####################################
#LearnPython3.8
#June2020
#EvenOdd Example
#Author: Merveille Koina Guidingar
####################################

import os

os.system('clear')

number = int(input('Enter a number: '))

if(number % 2 == 0):
	print(str(number)+' is an even number.')
else:
	print(str(number)+' is an odd number.')