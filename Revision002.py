#Practice002
#May2020
#Author: Merveille Guidingar Koina


#Write a program using the for loop to display the fizzbuzz. 

print('\n\tDisplaying the FizzBuzz: \n')
for fizzbuzz in range(0,16):
	if((fizzbuzz % 3 == 0 ) and (fizzbuzz % 5 == 0 )):
		print(str(fizzbuzz)+' FizzBuzz!')
	elif(fizzbuzz % 3 ==0):
		print(str(fizzbuzz)+' Fizz!')
	elif(fizzbuzz % 5 ==0):
		print(str(fizzbuzz)+' Buzz')
	else:
		print(fizzbuzz)