try:
    with open('newfile.txt', 'w') as file:
        file.write('This iss a new file created!')
        file.writelines([' This is another line to be added.', '\nAs well as this line.'])
except FileNotFoundError as e:
    print('Error', e)