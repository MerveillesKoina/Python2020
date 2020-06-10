###################################
#June2020
#LearnToCode
#Using Icons, Images and Exit Buttons 
#Author: Merveille Koina Guidingar
###################################

import os
from tkinter import *
from PIL import ImageTk,Image

#Clear the screen
os.system('clear')

root = Tk()

root.title('Icon,Image,Exit')

#Change the default icon with a new icon
root.iconbitmap('D:/PythonStuff/GUI/Graduate.ico')

'''
In case you save your code in the same path as your icon, you can just specify the name and extension as following:
root.iconbitmap('Graduate.ico') 
'''

#Add an image in your window

#Create an image

my_img = ImageTk.PhotoImage(Image.open('D:/PythonStuff/GUI/Mervy.jpg'))

#Create a label
my_label = Label(image=my_img)
my_label.pack()

'''
To add image in the container, it is a three way process.
First: create an image
Second: add your image to any of the widget
Third: Print the widget on the screen
'''


#Create an exit button

my_button = Button(root, text='Exit Program',padx=10,pady=10,bg='#414141',fg='white',command=root.quit)
my_button.pack()

root.mainloop()