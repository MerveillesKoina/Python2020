###############################
#Conditional Operators
#if/else/elif
###############################

import os

os.system('clear')


numb = 10
#numb = 15
#numb = 8

if(numb>10):
	print('Your number is greater than 10!')
elif(numb==10):
	print('Your number is equal to 10!')
else:
	print('Your number is less than 10!')


#Multiple Conditional Operators
#You use multiple conditional operators with the AND / OR keywords

numbers =40
if(numbers>0) and (numbers <50):
	print('Statement Verified')

if(numbers==40) or (numbers >150):
	print("Verified")
