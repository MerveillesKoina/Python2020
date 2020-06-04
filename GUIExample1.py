#Create a GUI program
#May2020
#Author: Merveille Guidingar Koina

import os
from tkinter import *


os.system('clear')


ct = Tk()

ct.title("Merveille - Learn To Code!")
ct.geometry('300x300')

#Define the function send

def send():
	l4 = Label(ct,text='Hey! My name is: '+txtb.get()+' and I am '+txtbx.get())
	l4.pack()

l1 = Label(ct,text='Form:')
l1.pack()

l2 = Label(ct,text='Name: ')
l2.pack()

txtb = Entry(ct,width=25)
txtb.pack()

l3 = Label(ct, text='Age: ')
l3.pack()

txtbx = Entry(ct,width=25)
txtbx.pack()

b = Button(ct,text='Submit', command=send)
b.pack()


ct.mainloop()