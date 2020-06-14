####################################
#LearnPython3.8
#June2020
#Radiobutton_list
#Author: Merveille Koina Guidingar
####################################

import os
from tkinter import *
from PIL import ImageTk,Image

#Clear the screen
os.system('clear')

#Create an object of the tkinter

root = Tk()

#Change the default icon
root.iconbitmap('D:/PythonStuff/GUI/Graduate.ico')

#Create a list

NAMES = [
		('Radjy','3'),
		('Mateo','13'),
		('Dave','11'),
		('Koula','5'),
		('Merv','20'),
]

#Create a variable

name = StringVar()
name.set('Radjy')

#def function
def clicked(value):
	l = Label(root,text=value)
	l.pack()

#Using the for loop to display the radiobuttons

for n, a in NAMES:
	Radiobutton(root,text=n,variable=name,value=a).pack()


#Create a button
b = Button(root,text='Clicked Me!',command=lambda:clicked(name.get()))
b.pack()
mainloop()