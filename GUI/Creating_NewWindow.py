####################################
#LearnPython3.8
#June2020
#Create New Window
#Author: Merveille Koina Guidingar
####################################


from tkinter import *
from PIL import ImageTk,Image

#create an object of the tkinter
root = Tk()
root.title('First Window')

root.iconbitmap('D:/PythonStuff/GUI/images.ico')

#Create a new window

new_window = Toplevel()
new_window.title('Second Window')

mainloop()