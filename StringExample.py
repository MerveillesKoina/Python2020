#Create a program using string variables, functions


import os

os.system('clear')


#Define a variable

greetings = 'hello, my name is Merveille Koina'

#Using Concatenation

hobby = ' and I love coding.'

print("\nUsing Concatenation: ",greetings + hobby)

#Using the upperfunction

print('\nUsing the Upper Function: '+greetings.upper())

#Using the lower function

print('\nUsing the lower function: '+greetings.lower())

#Using the title function
print('\nUsing the title function: '+greetings.title())

#Using the capitalize function

print('\nUsing the capitalize function: '+greetings.capitalize())

#Using the swapcase function

print('\nUsing the swapcase function: '+greetings.swapcase())


print('\nPrinting the length of the combining string: ',len(greetings+hobby))

print('\nUsing the split function: ',greetings.split(" "))

print('\nUsing the split function to display the string element: ',greetings.split(" ")[4:6])
