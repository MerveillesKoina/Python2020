####################################
#LearnPython3.8
#June2020
#Build a Simple Calculator
#Author: Merveille Koina Guidingar
####################################



from tkinter import *
import os

#Clear the Screen
os.system('clear')


#Create an object of the tkinter module
root = Tk()

#Give a title to the window
root.title('Calculator')

#Change the default icon
root.iconbitmap('D:/PythonStuff/GUI/images.ico')

#Create a textbox
txtbox = Entry(root,width=30,borderwidth=6)
txtbox.grid(row=0,column=0,columnspan=4,padx=10,pady=20,ipady=10)


#Define button click fuction
def button_click(number):
	#txtbox.delete(0,END)
	current_number = txtbox.get()
	txtbox.delete(0,END)
	txtbox.insert(0, str(current_number) + str(number))

#Define the clearce function
def clearce():
	txtbox.delete(0,END)

#Define the clear Button function
def clear():
	txtbox.delete(0,END)


#Define the button equal function
def button_add():
	first_number = txtbox.get()
	global f_num
	global math
	math ='addition'
	f_num=int(first_number)
	txtbox.delete(0,END)

#Define the button subtract function
def button_subtract():
	first_number = txtbox.get()
	global f_num
	global math
	math='subtraction'
	f_num = int(first_number)
	txtbox.delete(0,END)

#Define the button multiply function
def button_multiply():
	first_number = txtbox.get()
	global f_num
	global math
	f_num = int(first_number)
	math='multiplication'
	txtbox.delete(0,END)

#Define the button divide function
def button_divide():
	first_number = txtbox.get()
	global f_num
	global math
	f_num = int(first_number)
	math = 'division'
	txtbox.delete(0,END)

#Define the button modulo function
def button_modulo():
	first_number = txtbox.get()
	global f_num
	global math
	f_num = int(first_number)
	math = 'modulo'
	txtbox.delete(0,END)

#Define the button equal function
def button_equal():
	second_number = txtbox.get()
	s_num = int(second_number)
	txtbox.delete(0,END)

	if(math =='addition'):
		Answer = (f_num + s_num)
		txtbox.insert(0, Answer)

	elif(math =='subtraction'):
		Answer = (f_num - s_num)
		txtbox.insert(0, Answer)

	elif(math == 'multiplication'):
		Answer = (f_num * s_num)
		txtbox.insert(0, Answer)

	elif(math == 'division'):
		Answer = (f_num / s_num)
		txtbox.insert(0, Answer)

	elif(math == 'modulo'):
		Answer = (f_num % s_num)
		txtbox.insert(0, Answer)

	else:
		print('Error00001')


#Create buttons
my_button1 = Button(root,text='1',padx=25,pady=10,bg='#151515',fg='white',borderwidth=2,relief='ridge',command= lambda: button_click(1))
my_button2 = Button(root,text='2',padx=25,pady=10,bg='#151515',fg='white',borderwidth=2,relief='ridge',command= lambda: button_click(2))
my_button3 = Button(root,text='3',padx=25,pady=10,bg='#151515',fg='white',borderwidth=2,relief='ridge',command=lambda: button_click(3))
my_button4 = Button(root,text='4',padx=25,pady=10,bg='#151515',fg='white',borderwidth=2,relief='ridge',command= lambda: button_click(4))
my_button5 = Button(root,text='5',padx=25,pady=10,bg='#151515',fg='white',borderwidth=2,relief='ridge',command=lambda: button_click(5))
my_button6 = Button(root,text='6',padx=25,pady=10,bg='#151515',fg='white',borderwidth=2,relief='ridge',command=lambda: button_click(6))
my_button7 = Button(root,text='7',padx=25,pady=10,bg='#151515',fg='white',borderwidth=2,relief='ridge',command=lambda: button_click(7))
my_button8 = Button(root,text='8',padx=25,pady=10,bg='#151515',fg='white',borderwidth=2,relief='ridge',command=lambda: button_click(8))
my_button9 = Button(root,text='9',padx=25,pady=10,bg='#151515',fg='white',borderwidth=2,relief='ridge',command=lambda: button_click(9))
my_button0 = Button(root,text='0',padx=25,pady=10,bg='#151515',fg='white',borderwidth=2,relief='ridge',command=lambda: button_click(0))
my_buttonplusminus = Button(root,text='+/-',padx=19,pady=10,bg='#151515',fg='white',borderwidth=2,relief='ridge')
my_buttondot = Button(root,text='.',padx=26.5,pady=10,bg='#151515',fg='white',borderwidth=2,relief='ridge')
my_buttonmodulo = Button(root,text='%',padx=23,pady=10,bg='#484848',fg='white',borderwidth=2,relief='ridge',command=button_modulo)
my_buttonce = Button(root,text='CE',padx=21,pady=10,bg='#484848',fg='white',borderwidth=2,relief='ridge',command=clearce,cursor='arrow')
my_buttonc = Button(root,text='C',padx=25,pady=10,bg='#484848',fg='white',borderwidth=2,relief='ridge',command=clear,cursor='heart')

my_buttonplus = Button(root,text='+',padx=25,pady=10,bg='#484848',fg='white',borderwidth=2,relief='ridge',command=button_add)
my_buttonsubtract = Button(root,text='-',padx=26,pady=10,bg='#484848',fg='white',borderwidth=2,relief='ridge',command=button_subtract)
my_buttonmultiply = Button(root,text='X',padx=25,pady=10,bg='#484848',fg='white',borderwidth=2,relief='ridge',command=button_multiply)
my_buttondivide = Button(root,text='/',padx=25,pady=10,bg='#484848',fg='white',borderwidth=2,relief='ridge',command=button_divide)
my_buttonequal = Button(root,text='=',padx=25,pady=10,bg='#347A3C',fg='white',borderwidth=2,relief='ridge',command=button_equal)


my_buttonmodulo.grid(row=1,column=0)
my_buttonce.grid(row=1,column=1)
my_buttonc.grid(row=1,column=2)
my_buttondivide.grid(row=1,column=3)

my_button7.grid(row=2,column=0)
my_button8.grid(row=2,column=1)
my_button9.grid(row=2,column=2)
my_buttonmultiply.grid(row=2,column=3)

my_button4.grid(row=3,column=0)
my_button5.grid(row=3,column=1)
my_button6.grid(row=3,column=2)
my_buttonsubtract.grid(row=3,column=3)

my_button1.grid(row=4,column=0)
my_button2.grid(row=4,column=1)
my_button3.grid(row=4,column=2)
my_buttonplus.grid(row=4,column=3)

my_buttonplusminus.grid(row=5,column=0)
my_button0.grid(row=5,column=1)
my_buttondot.grid(row=5,column=2)
my_buttonequal.grid(row=5,column=3)






root.mainloop()