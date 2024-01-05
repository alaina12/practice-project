# my_file = open('test.txt')
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# print(my_file.readline())
# print(my_file.readlines())
# my_file.close()


# with open ('test.txt', mode = 'a') as my_file:
# 	text = my_file.write(':)')
# 	print(text)

# with open('./app\sad.txt', mode = 'r+')as my_file:
# 	print(my_file.read())
try:
	with open('sad.txt', mode = 'x')as my_file:
 	print(my_file.read())
except FileNotFoundError as err:
	print("File not found")
	raise err 
except IOError as err:
	print("file does not exist")
	raise err

