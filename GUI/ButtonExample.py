###################################
#June2020
#LearnToCode
#Author: Merveille Koina Guidingar
###################################


from tkinter import *
import os

os.system('clear')

root = Tk()
root.title('Button Example')

myButton = Button(root,text='Click Me!',pady=50)

myButton.pack()

root.mainloop()