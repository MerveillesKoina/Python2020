############################
#Practice00
#Variables
#Lists
#Math
#Tuples
#Dictionaries
#Strings

###########################


import os

os.system('clear')


#Variables

full_name = 'Koina Merveilles'
age = 41

print('\nVariables:\n'+full_name)
print(age)

#Lists
numbers = [250,25,3,12,45]
phones = ['iPhone','Samsung','Vivo','Pixel',numbers]

print('\nLists:\n',phones)

#Math

number_1 = 45
number_2 = 10

Answer = number_1 + number_2
Answer1 = number_1 - number_2

print('\nMath:\n')
print(Answer)
print(Answer1)

#Tuples
pc = ('gateway','surface','dell')

laptops = ('hp','Samsung','MacBook',1500,250,'Acer',pc)

print('\nTuples:\n',laptops)

#Dictionaries


names = {'Tim':23,'Nathan':40,25:'Ghyslaine','X':'dix'}

print('\nDictionaries:\n',names)
#Strings

first_name = 'Hndrxx'
last_name = 'Zeus'

quote = 'They tried to bury us, but they didn\'t know we were seeds!!'

#String Concatenation
print('\nThe Concatenation of ',first_name,'and',last_name,'is: '+first_name+last_name)

print('\nUsing the title function: '+quote.title())
print('\nUsing the swapcase function: '+quote.swapcase())
print('\nUsing the capitalize function: '+quote.capitalize())
print('\nUsing the title function: '+quote.title())
print('\nUsing the split function: ',quote.split(' '))



