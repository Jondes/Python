file_name = 'example.txt'

with open(file_name, 'w') as my_file:
    my_file.write(input('Your message: '))
    file_name.append(my_file)
