###################################
#June2020
#LearnToCode
#Frame Example 
#Author: Merveille Koina Guidingar
###################################

import os
from tkinter import *
from PIL import ImageTk,Image


#Clear the console
os.system('clear')

#Create an object of the tkinter
root = Tk()
root.title('Frame')

#change the default icon

root.iconbitmap('D:/PythonStuff/GUI/Graduate.ico')

#create a frame

frame = LabelFrame(root,padx=50,pady=50)
frame.pack(padx=10,pady=10)

#Create buttons
b = Button(frame,text='Click Here!')
b.grid(row=0,column=0)

b1 = Button(frame,text='Or Here!')
b1.grid(row=1,column=1)



root.mainloop()