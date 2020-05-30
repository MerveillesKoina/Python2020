#May2020
#Create a program using a defined function
#Author: Merveille Guidingar Koina


'''Syntax to define a function: 
 def function_name():
 	Code to be written
 '''

import os

os.system('clear')


def nameit():
	print('Hello World!')


nameit()



def Mathit(first_number, second_number):
	return(first_number + second_number)


#print(Mathit(5,10))

Result =(Mathit(4,5))
 
Result /=4

print(Result)


def Name(fname,lname):
	return('Welcome '+fname+' '+lname)

message = (Name('Merveilles','Koina'))
print(message)