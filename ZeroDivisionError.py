print("Give me two number,and I'll devide them.")
print("Enter 'q' to quit.")
while True:
	first_number = input("\nFirst Number:")
	if first_number == 'q':
		break
	second_number = input("Second Number:")
	if second_number == 'q':
		break
	try:
		answer = int(first_number)/int(second_number)
	except ZeroDivisionError:
		print("You can't divide by zero.")
	else:
		print(answer)