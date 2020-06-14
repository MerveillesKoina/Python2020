####################################
#LearnPython3.8
#June2020
#MessageBox
#Author: Merveille Koina Guidingar
####################################

import os
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

#Clear the console
os.system('clear')

#Create an object of the tkinter
root = Tk()

#Change the default icon
root.iconbitmap('D:/PythonStuff/GUI/images.ico')

#Define the function and create a message box inside it
def mbx():
	condition = messagebox.showinfo('Show Info','Hello World!')
	#messagebox.showwarning('Show Warning','Hello World!')
	#messagebox.showerror('Show Error','Hello World!')
	#messagebox.askquestion('Ask Question','Do you want to quit?')
	#messagebox.askokcancel('Ask Ok Cancel','Do you want to quit?')
	#condition=messagebox.askyesno('Ask Yes No','Are you sure to exit?')
	my_label= Label(root,text=condition).pack()
	
	#Condition
	if condition == 'ok':
		l1 = Label(root,text='Yes, clicked!').pack()
	else:
		l2 = Label(root,text='No, clicked!').pack()


#Create a button
my_button = Button(root,text='Clicked Me!',command=mbx)
my_button.pack()

mainloop()