####################################
#LearnPython3.8
#June2020
#FizzBuzz Example
#Author: Merveille Koina Guidingar
####################################

import os

#Use the os module to clear the screen

os.system('clear')

for fizb in range(0,35):
	if(fizb % 15 ==0):
		print(str(fizb)+'.FizzBuzz!')
	elif(fizb % 3 ==0):
		print(str(fizb) +'.Fizz!')
	elif(fizb % 5 ==0):
		print(str(fizb) +'.Buzz')
	else:
		print(fizb)