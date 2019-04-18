import sys
Number = input()
List =[]
x = 0
while x<len(Number):
	if Number[x] == '0':
		List.append('零')
	elif Number[x] == '1':
		List.append('一')
	elif Number[x] == '2':
		List.append('二')
	elif Number[x] == '3':
		List.append('三')
	elif Number[x] == '4':
		List.append('四')
	elif Number[x] == '5':
		List.append('五')
	elif Number[x] == '6':
		List.append('六')
	elif Number[x] == '7':
		List.append('七')
	elif Number[x] == '8':
		List.append('八')
	elif Number[x] == '9':
		List.append('九')
	else:
		print("输入格式错误")
		#如果条件不符合就结束程序
		sys.exit(0)
	x += 1
#将列表转化为字符串
print("".join(List))