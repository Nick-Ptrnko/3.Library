while True:
	try:
		first = int(input())
		second = int(input())
		print(first / second)
	except TypeError as e:
		print("Both values must be numbers ", e)
	except ZeroDivisionError as e:
		print("You are trying to divide by zero ", e)
	except KeyboardInterrupt as e:
		print("The program is completed ", e)

