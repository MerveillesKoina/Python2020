###################################
#June2020
#Module JunePractice000
#Author: Merveille Koina Guidingar

def FizzBuzzExample():

	for fzzb in range (35):
		if(fzzb %15 ==0):
			print(str(fzzb)+'.FizzBuzz')
		elif(fzzb % 3==0):
			print(str(fzzb)+'.Fizz')
		elif(fzzb % 5 ==0):
			print(str(fzzb)+'.Buzz')
		else: 
			print(fzzb)

