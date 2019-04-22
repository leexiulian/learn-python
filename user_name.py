user_names = ['Admin','Jack','Tom','Lily','Frank']
#删除列表中的所有元素
del user_names[-len(user_names):]
#判断列表是否为空
if user_names:
	for user_name in user_names:
		if user_name.lower() == 'admin':
			print("Hello " + user_name.title() + ",would you like to see a status report?")
		else:
			print("Hello " + user_name.title() + ", thank you for logging in again.")
else:
	print("We need to find some users!")
