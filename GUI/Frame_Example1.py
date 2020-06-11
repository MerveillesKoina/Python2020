####################################
#LearnPython3.8
#June2020
#Frame Example
#Author: Merveille Koina Guidingar
####################################

from tkinter import *
from PIL import ImageTk,Image
import os

os.system('clear')

#Create an object of the tkinter
root = Tk()

#Change the default icon and create a title of the container
root.iconbitmap('D:/PythonStuff/GUI/images.ico')
root.title('Frame')

#Creae a frame
frame = LabelFrame(root,padx=50,pady=50)
frame.pack(padx=5,pady=5)

#Create a label and place it inside the frame
l = Label(frame,text='My Frame')
l.grid(row=0,column=0)

#Create buttons and place them inside the frame
b = Button(frame,text='Click Me!',padx=7,pady=6)
b.grid(row=1,column=1)

b2 = Button(frame,text='Or Me!')
b2.grid(row=2,column=2,padx=2,pady=5)

b3 = Button(frame,text='Here Me')
b3.grid(row=2,column=0)

b4 = Button(frame,text='Instead Here',padx=3,pady=3)
b4.grid(row=3,column=1)



mainloop()