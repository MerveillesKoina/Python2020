###################################
#June2020
#LearnToCode
#Author: Merveille Koina Guidingar
###################################

import os
from tkinter import *


os.system('clear')

root = Tk()

root.title('GUIExample')
#root.geometry('250x250')

def f1():
	l1 = Label(root,text='Hey '+entry.get()+' '+entry1.get())
	l1.grid(row=50,column=4)

def det():
	entry.delete(0,END)
	entry1.delete(0,END)

l2 = Label(root,text='Name: ')
l2.grid(row=2,column=0)

entry = Entry(root,width=15)
entry.grid(row=2,column=5)

l3 = Label(root,text='LastName: ')
l3.grid(row=12,column=0)

entry1 = Entry(root,width=15)
entry1.grid(row=12,column=5)

b1 = Button(root,text='Submit',command=f1)
b1.grid(row=40,column=5)

b2 = Button(root,text='Clear',width=5,command=det)
b2.grid(row=40,column=6)



root.mainloop()