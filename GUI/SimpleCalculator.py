###################################
#June2020
#LearnToCode
#Author: Merveille Koina Guidingar


from tkinter import *
import os

os.system('clear')

root = Tk()
root.title('Simple Calculator')

#Define addButtons
def button_add(number):
	#txtbox.delete(0,END)
	current_number = txtbox.get()
	txtbox.delete(0,END)
	txtbox.insert(0,str(current_number) + str(number))

#Define the clear button
def button_clear():
	txtbox.delete(0,END)

#Define the plus button
def button_plus():
	first_number = txtbox.get()
	global f_num 
	global math
	math ='addition'
	f_num = int(first_number)
	txtbox.delete(0,END)

#Define the minus button
def button_subtract():
	first_number = txtbox.get()
	global f_num
	global math
	math ='subtraction'
	f_num = int(first_number)
	txtbox.delete(0,END)

#Define the multiply button
def button_multiply():
	first_number = txtbox.get()
	global f_num
	global math
	math ='multiplication'
	f_num = int(first_number)
	txtbox.delete(0,END)

#Define the minus button
def button_divide():
	first_number = txtbox.get()
	global f_num
	global math
	math ='division'
	f_num = int(first_number)
	txtbox.delete(0,END)

#Define the Equal button
def button_equal():
	second_number = txtbox.get()
	txtbox.delete(0,END)

	if(math == 'addition'):
		txtbox.insert(0,f_num + int(second_number))
	elif(math == 'subtraction'):
		txtbox.insert(0, f_num - int(second_number))
	elif(math == 'multiplication'):
		txtbox.insert(0, f_num * int(second_number))
	elif(math =='division'):
		txtbox.insert(0, f_num / int(second_number))
	else:
		print('Error001')


txtbox = Entry(root,width=30,borderwidth=6)
#txtbox.insert(0,'Enter......')
txtbox.grid(row=0,column=0,padx=10,pady=10,columnspan=3)

my_button1 = Button(root,text='1',padx=40,pady=20,command=lambda: button_add(1))
my_button2 = Button(root,text='2',padx=40,pady=20,command=lambda: button_add(2))
my_button3 = Button(root,text='3',padx=40,pady=20,command=lambda: button_add(3))
my_button4 = Button(root,text='4',padx=40,pady=20,command=lambda: button_add(4))
my_button5 = Button(root,text='5',padx=40,pady=20,command=lambda: button_add(5))
my_button6 = Button(root,text='6',padx=40,pady=20,command=lambda: button_add(6))
my_button7 = Button(root,text='7',padx=40,pady=20,command=lambda: button_add(7))
my_button8 = Button(root,text='8',padx=40,pady=20,command=lambda: button_add(8))
my_button9 = Button(root,text='9',padx=40,pady=20,command=lambda: button_add(9))
my_button0 = Button(root,text='0',padx=40,pady=20,command=lambda: button_add(0))
my_buttonplus = Button(root,text='+',padx=39,pady=20,command=button_plus)
my_buttonminus = Button(root,text='-',padx=40,pady=20,command=button_subtract)
my_buttonmultiply = Button(root,text='*',padx=41,pady=20,command=button_multiply)
my_buttondivision = Button(root,text='/',padx=42,pady=20,command=button_divide)
my_buttonequal = Button(root,text='=',padx=90,pady=20,command=button_equal)
my_buttonclear = Button(root,text='Clear',padx=79,pady=20,command=button_clear)




my_button1.grid(row=3,column=0)
my_button2.grid(row=3,column=1)
my_button3.grid(row=3,column=2)

my_button4.grid(row=2,column=0)
my_button5.grid(row=2,column=1)
my_button6.grid(row=2,column=2)

my_button7.grid(row=1,column=0)
my_button8.grid(row=1,column=1)
my_button9.grid(row=1,column=2)

my_button0.grid(row=4,column=0)
my_buttonplus.grid(row=5,column=0)
my_buttonequal.grid(row=5,column=1,columnspan=2)
my_buttonclear.grid(row=4,column=1,columnspan=2)

my_buttonminus.grid(row=6,column=0)
my_buttonmultiply.grid(row=6,column=1)
my_buttondivision.grid(row=6,column=2)





root.mainloop()