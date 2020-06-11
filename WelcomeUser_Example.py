####################################
#LearnPython3.8
#June2020
#Create a program to display hello to a specific user
#Author: Merveille Koina Guidingar
####################################


import os

os.system('clear')

name = input('Enter your name: ')
pwd = input('Enter password: ')

if(name == 'Merveille' and pwd =='user1'):
	print('\n\tWelcome '+name)
else:
	print('Wrong Credentials, try again later.........')