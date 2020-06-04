###################################
#June2020
#Module JunePractice000
#Author: Merveille Koina Guidingar

def ChooseSign():
	print('\nMath Operations:\n')
	number = int(input('Enter First Number: '))
	number1 = int(input('Enter Second Number: '))
	character=input('Enter an Operation Sign: ')

	if(character == '+'):
		Result = (number + number1)
		print('The Result of Addition: '+str(Result))
	elif(character == '-'):
		Result = (number - number1)
		print('The Result of Subtraction: '+str(Result))
	elif(character == '*'):
		Result = (number * number1)
		print('The Result of Multiplication: '+str(Result))
	elif(character == '/'):
		Result = (number / number1)
		print('The Result of Division: '+str(Result))
	elif(character == '%'):
		Result = (number % number1)
		print('The Result of Modulo: '+str(Result))
	else:
		print('Wrong sign, try again later............')

def AssignmentOp():
	print('\nAssignment Operations:\n')
	numb = int(input('Enter a number: '))

	sign = input('Enter an assignment sign: ')

	if(sign =='+='):
		numb +=numb
		print(numb)
	elif(sign =='-='):
		numb -=numb
		print(numb)
	elif(sign =='*='):
		numb *=numb
		print(numb)
	elif(sign =='/='):
		numb /=numb
		print(numb)
	elif(sign =='**='):
		numb **=numb
		print(numb)
	elif(sign =='%='):
		numb %=numb
		print(numb)
	else:
		print('Wrong assignment Op, try again later....................')



