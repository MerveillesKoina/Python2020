#Create a GUI program
#May2020
#Author: Merveille Guidingar Koina


import os
from tkinter import *

os.system('clear')

#Create an object of the tkinter module
root = Tk()

#Create the title of the container/window and the specify the dimension
root.title("User Graphical Interface")
root.geometry('300x300')

#Define the function hello

def hello():
	my_label1 = Label(root,text='Hello '+txtbx.get())
	my_label1.pack()

#Create a label
my_label = Label(root,text='Enter your first Name:')
my_label.pack()

#Create a textbox
txtbx = Entry(root,width=30)
txtbx.pack()

#Create a button
my_button = Button(root, text='Submit',bg='black',fg='white', command=hello)
my_button.pack()




root.mainloop()