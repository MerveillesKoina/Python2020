###################################
#June2020
#LearnToCode
#Author: Merveille Koina Guidingar

from tkinter import *
import os

os.system('clear')


root = Tk()

root.title('TextBox Example')

entry = Entry(root,width=25)

entry.insert(0,'Enter your name')
entry.grid(row=0,column=0,columnspan=5,padx=5,pady=8)

b = Button(root,text='Click Me!')
b.grid(row=3,column=3)

root.mainloop()