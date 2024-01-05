file_name =input(str("File name: "))

if file_name.casefold().endswith('.gif'):
    print('image/gif')
elif file_name.casefold().endswith('.jpeg'):
    print('image/jpeg')
elif file_name.casefold().endswith('.jpg'):
    print('image/jpg')
elif file_name.casefold().endswith('.txt'):
    print('image/txt')
else:
    print('application/octet-stream')


