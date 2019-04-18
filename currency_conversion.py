# 1USD = 6.78RMB
currency = input("请输入带有符号的币值：")
if currency[0:3] == 'USD':
	RMB = eval(currency[3:]) * 6.78
	print("转换后的币值为{:.2f}RMB".format(RMB))
elif currency[0:3] == 'RMB':
	USD = eval(currency[3:])/6.78
	print("转换后的币值为{:.2f}USD".format(USD))
else:
	print("输入格式错误")
