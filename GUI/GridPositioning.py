###################################
#June2020
#LearnToCode
#Author: Merveille Koina Guidingar
###################################

from tkinter import *
import os 

os.system('clear')

root = Tk()

# Creating a Label Widget
my_label = Label(root,text='Hello Merveille!!!')
my_label1 = Label(root,text='I love coding')

my_label.grid(row=0,column=0)
my_label1.grid(row=1,column=5)

root.mainloop()