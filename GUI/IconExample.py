####################################
#LearnPython3.8
#June2020
#Icon Example
#Author: Merveille Koina Guidingar
####################################


import os
from tkinter import *
from PIL import ImageTk,Image

#Clear the screen/Console
os.system('clear')

#Create an object of the tkinter
root = Tk()
root.title('Icon')

#Change the default icon to a new icon

root.iconbitmap('images.ico')

L1 = Label(root,text='First Image')
L1.pack()
my_img = ImageTk.PhotoImage(Image.open('D:/Python/images.jpg'))
my_label= Label(image=my_img)
my_label.pack()

L2 = Label(root,text='Second Image')
L2.pack()
my_img1 = ImageTk.PhotoImage(Image.open('D:/Python/img.jpg'))
my_label1 = Label(image=my_img1)
my_label1.pack() 

L3 = Label(root,text='Third Image')
L3.pack()
my_img2= ImageTk.PhotoImage(Image.open('D:/Python/download.jpg'))
l4= Label(image=my_img2)
l4.pack() 

root.mainloop()