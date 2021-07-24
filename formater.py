# Very rough formater that spaces out the layers to a fixed width.
# It will mess up any other lines with the & character

output = open('output.txt', 'w') 
keypressWidth = 15


with open('config/corne.keymap') as file:
    for line in file:
        if line.__contains__('&'):
            for command in line.split('&')[1:]:
                
                command = command.strip()
                command = command.ljust(keypressWidth,' ')
                output.write('&' + command)
            output.write('\n')
        else:
            output.write(line)     
