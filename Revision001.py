############################
#Practice001
#Assignment Operators
#Comparison Operators
#Conditional Statements
#Author: Merveille Guidingar Koina
###########################


import os

os.system('clear')


#Assignments Operators

print('\tAssignment Operators:')
# equal operator
number = 10

print('Equal Operator:',number)

#plus equal operator
number +=15

print('Plus Equal Operator:',number)

# minus equal operator
number -=5

print('Minus equal operator:',number)

# multiply equal operator

number *=5

print('Multiply equal operator:',number)

#exponent equal operator 

number **=5

print('Exponent equal operator:',number)

#division equal operator

number /=3

print('Division equal operator',number)

#modulo equal operator

number %=2
print('Modulo equal operator',number)

#Comparison Operators

print('\nComparison Operators:')

name = 'Merv'
num = 200

print(name=='merv')

print(num>=10)

print(num<150)

print(num>250)

print(num<=200)

print(name!='Merv')

#Conditional Statements
print('\nCondition Statements:\n')

fname = 'Hndrxx'
age=25

character = 'a','e','i'

if(fname=='Hndrxx'):
	print('Welcome',fname)

if(fname=='Hndrxx' and age==25):
	print('Credentials Verified!! Access Granted')
else:
	print('Wrong Credentials, Try again later')


if(fname=='Drxx' and age==23):
	print('Credentials Verified!! Access Granted')
else:
	print('Wrong Credentials, Try again later')


