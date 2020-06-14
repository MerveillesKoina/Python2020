####################################
#LearnPython3.8
#June2020
#Radiobuttons
#Author: Merveille Koina Guidingar
####################################

import os
from tkinter import *
from PIL import ImageTk,Image

#clear the console
os.system('clear')

#Create an object of the tkinter module
root = Tk() 
root.title('Radiobuttons')

root.iconbitmap('D:/PythonStuff/GUI/images.ico')

#Define the variable as integer
#r = IntVar()
#Confirm if which Radiobutton is clicked using the get() function
#r.get()

#Let's set the Radiobutton
#r.set('2')

#Create a list 
PHONES =[
	('iPhone','iPhone X'),
	('Samsung','Samsung 20'),
	('Vivo','Vivo Neo'),
	('Pixel','Pixel 2'),
	('Huawei','Huawei P20'),
]

#create a variable
pizza = StringVar()
pizza.set('iPhone')

#Using the for loop 
for brand,model in PHONES:
	Radiobutton(root,text=brand,variable=pizza,value=model).pack(anchor=W)
#define the function
def clicked(value):
	my_label = Label(root,text=value)
	my_label.pack()

#Create radiobuttons and display on the container
#Radiobutton(root,text='Option 1',variable=r,value=1,command=lambda:clicked(r.get())).pack()
#Radiobutton(root,text='Option 2',variable=r,value=2,command=lambda:clicked(r.get())).pack()


#Using the Label to confirm which Radiobutton is clicked
#my_label = Label(root,text=pizza.get())
#my_label.pack()

#create a button
my_button = Button(root,text='Click Me!',command=lambda:clicked(pizza.get()))
my_button.pack()

mainloop()