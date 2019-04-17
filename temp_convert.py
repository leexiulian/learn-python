TempStr = input("请输入带有符号的温度值: ")
#摄氏温度转换为华氏温度
if TempStr[-1] in ['C','c']:
	F = eval(TempStr[0:-1])*1.8 + 32
	print("转换后的温度是{:.2f}F".format(F))
#华氏温度转换为摄氏温度
elif TempStr[-1] in ['F','f']:
	C = (eval(TempStr[0:-1]) - 32)/1.8
	print("转换后的温度是{:.2f}C".format(C))
else:
	print("输入格式错误")