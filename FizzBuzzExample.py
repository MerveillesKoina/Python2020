#May2020
#Author: Merveille Guidingar Koina

import os

os.system('clear')

#FizzBuzz


number = 0

while(number<=100):
	if(number % 3 ==0) and (number % 5 ==0):
		print(str(number) +". FizzBuzz!")
	elif(number % 3 ==0):
		print(str(number) +'. Fizz!')
	elif(number % 5 == 0):
		print(str(number) +'. Buzz!')
	else:
		print(str(number)+' .')

	number+=1