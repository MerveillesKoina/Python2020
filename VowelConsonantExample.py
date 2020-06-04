#Create a program to display if an enterred character is consonant or vowel
#May2020
#Practice
#Author: Merveille Guidingar Koina


import os

os.system('clear')

character = input('Enter a Character: ')

if(character =='a' or character =='e' or character =='i' or character =='o' or character=='u'):
	print(character,'is a Vowel!')
elif(character =='A' or character =='E' or character =='I' or character =='O' or character=='U'):
	print(character,'is a Vowel!')
else:
	print(character,'is a Consonant!')
