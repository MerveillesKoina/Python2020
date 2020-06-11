####################################
#LearnPython3.8
#June2020
#Prime Number Example
#Author: Merveille Koina Guidingar
####################################


import os

#Clear the screen using the os module
os.system('clear')

#Using the for loop

for number in range(1,45):
	count=0
	for i in range(2, (number % 2 +1)):
		if(number % i == 0):
			count +=1
		break
	if(count ==0 and number !=1):
		print('%d'%number, end=' ')