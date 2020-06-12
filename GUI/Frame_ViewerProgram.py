####################################
#LearnPython3.8
#June2020
#Practice
#Frame Viewer Program 
#Author: Merveille Koina Guidingar
####################################


import os
from tkinter import *
from PIL import ImageTk,Image


#Clear the console
os.system('clear')

#Create an object of the tkinter
root = Tk()
root.title('Viewer Program')

#Change the default the icon
root.iconbitmap('D:/PythonStuff/GUI/images.ico')

#Create a frame
frame = LabelFrame(root,padx=5,pady=5)
frame.pack(padx=5,pady=5)

#Define images
my_img = ImageTk.PhotoImage(Image.open('D:/PythonStuff/GUI/Pictures/M.jpg'))
my_img1 = ImageTk.PhotoImage(Image.open('D:/PythonStuff/GUI/Pictures/MLA.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('D:/PythonStuff/GUI/Pictures/DMR.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('D:/PythonStuff/GUI/Pictures/RM.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('D:/PythonStuff/GUI/Pictures/MT.jpg'))

images_list =[my_img,my_img1,my_img2,my_img3,my_img4]

#Create a status bar
status = Label(frame,text='Image 1 of '+str(len(images_list)),relief=SUNKEN,anchor=E)

#Define functions
def forward(image_number):
	global my_backbutton
	global my_label
	global my_fwdbutton

	#Delete the image in label
	my_label.grid_forget()

	#Update the image label
	my_label = Label(frame,image=images_list[image_number-1])

	#Update the forward button
	my_fwdbutton = Button(frame,text='>>',padx=10,pady=4,bd=3,command=lambda:forward(image_number+1))

	#Update the back button
	my_backbutton = Button(frame,text='<<',padx=10,pady=4,bd=3,command=lambda:back(image_number-1))

	#Update the status label
	status = Label(frame,text='Image '+str(image_number)+' of '+str(len(images_list)),relief=SUNKEN,anchor=E)
	

	#Disable the forward button when image list is out of range
	if(image_number ==5):
		my_fwdbutton = Button(frame,text='>>',padx=10,pady=4,bd=3,state=DISABLED)


	#Display the label on the frame
	my_label.grid(row=0,column=0,columnspan=3)


	#Display the buttons on the frame
	my_backbutton.grid(row=1,column=0)
	my_fwdbutton.grid(row=1,column=2)

	#Put the status bar on the frame
	status.grid(row=2,column=0,columnspan=3,sticky=W+E)


def back(image_number):
	global my_backbutton
	global my_label
	global my_fwdbutton

	#Get rid of the image in label
	my_label.grid_forget()

	#Update the image in label
	my_label = Label(frame,image=images_list[image_number-1])

	#Update the forward button
	my_fwdbutton = Button(frame,text='>>',padx=10,pady=4,bd=3,command=lambda:forward(image_number+1))

	#Update the back button
	my_backbutton = Button(frame,text='<<',padx=10,pady=4,bd=3,command=lambda:back(image_number-1))

	#Update the status label
	status = Label(frame,text='Image '+str(image_number)+' of '+str(len(images_list)),relief=SUNKEN,anchor=E)

	if(image_number==1):
		my_backbutton = Button(frame,text='<<',padx=10,pady=4,bd=3,state=DISABLED)

	#Put the label on the frame
	my_label.grid(row=0,column=0,columnspan=3)

	#Put the buttons on the frame
	my_backbutton.grid(row=1,column=0)
	my_fwdbutton.grid(row=1,column=2)
	
	#Put the status bar on the frame
	status.grid(row=2,column=0,columnspan=3,sticky=W+E)



#Create a Label and add it to the frame
my_label = Label(frame,image=my_img)
my_label.grid(row=0,column=0,columnspan=3)

#Create Buttons and add them in to the frame
my_backbutton = Button(frame,text='<<',padx=10,pady=4,bd=3,command=back,state=DISABLED)
my_button = Button(frame,text='Exit Program',padx=12,pady=4,bd=3,command=root.quit)
my_fwdbutton = Button(frame,text='>>',padx=10,pady=4,bd=3,command=lambda:forward(2))

#Display the buttons on the frame
my_backbutton.grid(row=1,column=0)
my_button.grid(row=1,column=1)
my_fwdbutton.grid(row=1,column=2)

#Display the status
status.grid(row=2,column=0,columnspan=3,sticky=W+E)

mainloop()