####################################
#LearnPython3.8
#June2020
#Status Bar Example
#Author: Merveille Koina Guidingar
####################################

import os
from tkinter import *
from PIL import ImageTk,Image


os.system('clear')

root = Tk()

root.title('Viewer App')

#Change the default icon
root.iconbitmap('D:/PythonStuff/GUI/images.ico')


#add images on the container
my_img = ImageTk.PhotoImage(Image.open('D:/PythonStuff/GUI/images.jpg'))
my_img1 = ImageTk.PhotoImage(Image.open('D:/PythonStuff/GUI/download.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('D:/PythonStuff/GUI/img.jpg'))

#Create a list of the images

images_list =[my_img,my_img1,my_img2]

#Create a status bar
status = Label(root,text='Image 1 of '+str(len(images_list)),bd=3,relief=SUNKEN,anchor=E)

#Define forward button
def forward(image_number):
	global my_label
	global my_fwdbutton
	global my_backbutton

	my_label.grid_forget()

	my_label = Label(image=images_list[image_number-1])


	my_fwdbutton = Button(root,text='>>',padx=10,pady=5,bg='#939393',fg='white',command=lambda:forward(image_number+1))

	my_backbutton = Button(root,text='<<',padx=10,pady=5,bg='#939393',fg='white',command=lambda:back(image_number-1))

	if(image_number==3):
		my_fwdbutton = Button(root, text='>>',padx=10,pady=5,bg='#939393',fg='white',state=DISABLED)

	#Update the status bar
	status = Label(root,text='Image '+str(image_number)+' of '+str(len(images_list)),bd=3,relief=SUNKEN,anchor=E)

	my_label.grid(row=0,column=0,columnspan=3)
	my_backbutton.grid(row=1,column=0)
	my_fwdbutton.grid(row=1,column=2)

	#Add the status bar to the container
	status.grid(row=2,column=0,columnspan=3,sticky=W+E)


#Define back button
def back(image_number):
	global my_label
	global my_fwdbutton
	global my_backbutton

	my_label.grid_forget()

	my_label = Label(image=images_list[image_number-1])

	my_fwdbutton = Button(root,text='>>',padx=10,pady=5,bg='#939393',fg='white',command=lambda:forward(image_number+1))

	my_backbutton = Button(root,text='<<',padx=10,pady=5,bg='#939393',fg='white',command=lambda:back(image_number-1))

	if(image_number==1):
		my_backbutton = Button(root,text='<<',padx=10,pady=5,bg='#939393',fg='white',state=DISABLED)

	#Update the status bar
	status = Label(root,text='Image '+str(image_number)+' of '+str(len(images_list)),bd=3,relief=SUNKEN,anchor=E)
	
	#Print out on the container
	my_label.grid(row=0,column=0,columnspan=3)
	my_backbutton.grid(row=1,column=0)
	my_fwdbutton.grid(row=1,column=2)

	#Add The status label
	status.grid(row=2,column=0,columnspan=3,sticky=W+E)

#Add image on the label
my_label = Label(root,image=my_img)
my_label.grid(row=0,column=0,columnspan=3)

#Create buttons
my_button = Button(root,text='Exit Program',command=root.quit,padx=10,pady=5,bg='#414141',fg='white')
my_backbutton = Button(root,text='<<',padx=10,pady=5,command=lambda:back(),state=DISABLED,bg='#939393',fg='white')
my_fwdbutton = Button(root,text='>>',padx=10,pady=5,command=lambda:forward(2),bg='#939393',fg='white')

#Add buttons on the container
my_backbutton.grid(row=1,column=0)
my_button.grid(row=1,column=1,pady=10)
my_fwdbutton.grid(row=1,column=2)

#Add status bar on the container
status.grid(row=2,column=0,columnspan=3,sticky=W+E)




root.mainloop()