#Practice003
#May2020
#Author: Merveille Guidingar Koina

fizzbuzzcount = 0
fizzcount = 0
buzzcount = 0

for fz in range(0,11):
	if(fz%15==0):
		print(fz,'Fizzbuzz')
		fizzbuzzcount += 1
	elif(fz%3==0):
		print(fz,'Fizz')
		fizzcount += 1
	elif(fz%5==0):
		print(str(fz)+' Buzz')
		buzzcount += 1
	else:
		print(fz)

print('\t\t_________________________________________')
print('\t\tFizz\t\tBuzz\t\tFizzBuzz')
print('\t\t '+str(fizzcount)+'\t\t '+str(buzzcount)+'\t\t    '+str(fizzbuzzcount))
