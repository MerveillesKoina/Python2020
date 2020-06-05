###################################
#June2020
#JunePractice000
#Author: Merveille Koina Guidingar
###################################

from tkinter import *
import os

os.system('clear')


root = Tk()

root.title('Gui')
root.geometry('250x250')

#define functions

def display():
	l4 = Label(root,text='I am '+txtb.get()+' '+txtb1.get())
	l4.place(x=95,y=120)

def clearRoot():
    txtb.delete(0,END)
    txtb1.delete(0,END)
    

l1 = Label(root,text='Form')
l1.pack()

l2 = Label(root, text='First Name: ')
l2.place(x=5,y=30)

txtb = Entry(root,width=25)
txtb.place(x=85,y=30)

l3 = Label(root,text='Second Name: ')
l3.place(x=0,y=60)

txtb1 = Entry(root,width=25)
txtb1.place(x=85,y=60)

b1 = Button(root, text='Submit', width=7,command=display)
b1.place(x=90,y=90)

b2 = Button(root,text='Clear', width=7,command=clearRoot)
b2.place(x=160,y=90)

root.mainloop()
