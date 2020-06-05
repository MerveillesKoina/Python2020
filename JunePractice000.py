###################################
#June2020
#JunePractice000
#Author: Merveille Koina Guidingar
###################################



import os
import FizzBuzzEx
import MathOperations
import ListExample
import DictionaryExample
import ModuleTuple


os.system('clear')


#Variables(create variables name and age)

name = 'Merveille'
age=20
num = 5

options = 'Your body just shake my antenna. Long time you play games like cantana.'

#Strings

print('Using the Upper Function: '+name.upper())
print('\nUsing the Title Function: '+options.title())
print('\nUsing the Capitalize Function: '+options.capitalize())
print('\nUsing the SwapCase Function: '+name.swapcase())

#Numbers

Result = age + num
print('\nThe Result is: '+str(Result))

#Loops

print('\nFor Loop:')
for message in range(4):
	print('Welcome Merv!!')


#While Loop

print('\nWhile Loop:')

count = 0

while(count<=10):
	print(count)
	count +=1

#FizzBuzzExample
#Import the Created Fizzbuzz module
print('\nFizzBuzz Example:\n')

FizzBuzzEx.FizzBuzzExample()

#Math Operations Example
#Import the created mathop module

MathOperations.ChooseSign()

MathOperations.AssignmentOp()


ListExample.my_list()

DictionaryExample.my_dictionary()

print('\n')
ModuleTuple.tuples_example()
