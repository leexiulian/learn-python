filename = 'the_article.txt'

with open(filename,'r') as f_obj:
	contents = f_obj.read()
List = contents.split()
print(List)
print(len(List))