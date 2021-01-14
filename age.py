driving = input ('Have you driven a car: ')
if driving !='yes' and driving !='no':
	print("you can only answer yes or no in this question")
	raise SystemExit

age = input('How old are you?')
age = int(age)

if driving =='yes':
	if age >= 18:
		print ('Pass')
	else:
		print('warning: your age is not qualified') 
elif driving == 'no':
	if age >= 18:
		print ('your age is qualified to get a driving license')
	else: 
		print('Your age is not qualified to get a driving license')
else:
	print ("you can only answer yes or no in Q1")