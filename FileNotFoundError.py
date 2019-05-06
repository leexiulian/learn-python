filename = 'alice.txt'
try:
	with open(filename,'r') as file_object:
		contents = file_object.read()
except FileNotFoundError:
	message = "Sorry,the file " + filename + " does not exist."
	print(message)