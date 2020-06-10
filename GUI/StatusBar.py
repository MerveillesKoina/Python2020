###################################
#June2020
#LearnToCode
#Status Bar With Python 
#Author: Merveille Koina Guidingar
###################################


import os
from tkinter import *
from PIL import ImageTk,Image


#Clear the console
os.system('clear')

#Create an object of the tkinter module

root = Tk()
root.title('Image Viewer')

#Add an Icon
root.iconbitmap('D:/PythonStuff/GUI/Graduate.ico')

#Add an Image to the container

my_img = ImageTk.PhotoImage(Image.open('D:/PythonStuff/GUI/Images/Mervy.jpg'))
my_img1 = ImageTk.PhotoImage(Image.open('D:/PythonStuff/GUI/Images/Mom.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('D:/PythonStuff/GUI/Images/MDR.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('D:/PythonStuff/GUI/Images/Accra.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('D:/PythonStuff/GUI/Images/ArmandMer.jpg'))
my_img5 = ImageTk.PhotoImage(Image.open('D:/PythonStuff/GUI/Images/MIA.jpg'))
my_img6 = ImageTk.PhotoImage(Image.open('D:/PythonStuff/GUI/Images/BervainMerv.jpg'))
my_img7 = ImageTk.PhotoImage(Image.open('D:/PythonStuff/GUI/Images/Koina.jpg'))
my_img8 = ImageTk.PhotoImage(Image.open('D:/PythonStuff/GUI/Images/Soa.jpg'))
my_img9 = ImageTk.PhotoImage(Image.open('D:/PythonStuff/GUI/Images/Ngueita.jpg'))
my_img10 = ImageTk.PhotoImage(Image.open('D:/PythonStuff/GUI/Images/Merv.jpg'))
my_img11 = ImageTk.PhotoImage(Image.open('D:/PythonStuff/GUI/Images/MA.jpg'))
my_img12 = ImageTk.PhotoImage(Image.open('D:/PythonStuff/GUI/Images/Gh.jpg'))
my_img13 = ImageTk.PhotoImage(Image.open('D:/PythonStuff/GUI/Images/Drxx.jpg'))

#Create a list of image

image_list = [my_img,my_img1,my_img2,my_img3,my_img4,my_img5,my_img6,my_img7,my_img8,my_img9,my_img10,my_img11,my_img12,my_img13]

#Create a status bar
#status =Label(root,text='Image 1 of 14')

#Using the length function to determine how many items we have in the list
#status = Label(root,text='Image 1 of '+str(len(image_list)),bd=2,relief=SUNKEN)

#Let's add the anchor to place the status bar on a specific spot(E=stands for East)
status = Label(root,text='Image 1 of '+str(len(image_list)),bd=2,relief=SUNKEN,anchor=E)




my_label = Label(image=my_img)
my_label.grid(row=0,column=0,columnspan=3)

def forward(image_number):
	global my_label
	global my_fwdbutton
	global my_backbutton

#To get a rid of the image which is in the label. This function will delete the image on the label
	my_label.grid_forget()

#To tell the program what the new image should be:
	my_label = Label(image=image_list[image_number-1])

# To update the forward button to get the new image
	my_fwdbutton = Button(root,text='>>',command=lambda: forward(image_number+1),bg='#414141',fg='white',padx=10,pady=5)

#To update the back button to get the previous image
	my_backbutton = Button(root, text='<<',command=lambda:back(image_number-1),bg='#414141',fg='white',padx=10,pady=5)

#To prevent the forward button to display a null image on the screen
	if(image_number ==14):
		my_fwdbutton = Button(root,text='>>', state=DISABLED,bg='#414141',fg='white',padx=10,pady=5)

#Let's update the status bar to display whatever number we are on when we click the forward button
	status = Label(root,text='Image '+str(image_number)+' of '+str(len(image_list)),bd=2,relief=SUNKEN,anchor=E)

#To display the new label on the screen,
	my_label.grid(row=0,column=0,columnspan=3)

#To display the updated buttons on the screen
	my_fwdbutton.grid(row=1,column=2)
	my_backbutton.grid(row=1,column=0)

#Display the update status bar
	status.grid(row=2,column=0,columnspan=3,sticky=W+E)

def back(image_number):
	global my_label
	global my_fwdbutton
	global my_backbutton

#To get a rid of the image which is in the label. This function will delete the image on the label
	my_label.grid_forget()

#To tell the program what the new image should be:
	my_label = Label(image=image_list[image_number-1])

# To update the forward button to get the new image
	my_fwdbutton = Button(root,text='>>',command=lambda:forward(image_number+1),bg='#414141',fg='white',padx=10,pady=5)

#To update the back button to get the previous image
	my_backbutton = Button(root,text='<<',command=lambda:back(image_number-1),bg='#414141',fg='white',padx=10,pady=5)

#To prevent the forward button to display a null image on the screen
	if(image_number ==1):
		my_backbutton = Button(root,text='<<',state=DISABLED,bg='#414141',fg='white',padx=10,pady=5)

#Let's update the status bar to display whatever number we are on when we click the forward button
	status = Label(root,text='Image '+str(image_number)+' of '+str(len(image_list)),bd=2,relief=SUNKEN,anchor=E)

#To display the updated buttons on the screen
	my_label.grid(row=0,column=0,columnspan=3)
	my_backbutton.grid(row=1,column=0)
	my_fwdbutton.grid(row=1,column=2)

#Display the update status bar
	status.grid(row=2,column=0,columnspan=3,sticky=W+E)


#Create three buttons: back,forward and exit
my_backbutton = Button(root,text='<<',command=back, state=DISABLED,bg='#414141',fg='white',padx=10,pady=5)
my_exitbutton = Button(root,text='Exit Viewer',command=root.quit,bg='#414141',fg='white',padx=10,pady=5)
my_fwdbutton = Button(root,text='>>',command=lambda:forward(2),bg='#414141',fg='white',padx=10,pady=5)

#Put the buttons in the container

my_backbutton.grid(row=1,column=0)
my_exitbutton.grid(row=1,column=1,pady=10)
my_fwdbutton.grid(row=1,column=2)
#status.grid(row=2,column=0,columnspan=3,sticky=W+E)

#Let's add the sticker keyword to stretch status all the way left to right
status.grid(row=2,column=0,columnspan=3,sticky=W+E)

root.mainloop()
