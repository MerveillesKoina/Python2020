#For Loop
#May2020
#Author: Merveille Guidingar Koina

import os

os.system('clear')

print('Variable Example:')
name='Koularambaye'

for n in name:
	print('\t'+n)

print('\nList Names Example:')
names =['Nasty','Jidenna','Breezy','Claver','Drxx']

for n_1 in names:
	print(n_1)

print('\nDictionary Example:')

phones = {
	2015:'iPhone5',
	2016:'iPhone6',
	2017:'iPhone7',
	2018:'iPhone8',
	2019:'iPhoneX',
	2020:'iPhone11'
	}

for key,value in phones.items():
	print(value+' manufactured in '+str(key))