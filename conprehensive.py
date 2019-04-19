#创建一个列表
Lists = ["country","city","language","hello","custom","music","book","computer","mountain","sub"]
#在列表末尾添加一个元素
Lists.append("add")
#在指定位置插入一个元素
Lists.insert(0,"river")
#del 删除一个元素
del Lists[-2]
#pop弹出一个最后元素
Lists.pop()
#pop弹出第五个元素
Lists.pop(4)
#删除列表中的元素computer
Lists.remove("computer")
#打印列表
print(Lists)
#获取列表的长度并打印
print(len(Lists))
#按字母顺序进行并打印
print(sorted(Lists))
#将列表进行永久性排序
Lists.sort()
#逆向排序
Lists.reverse()
#将列表输出
print(Lists)




