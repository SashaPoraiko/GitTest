commands = ['write', 'read', 'end', 'search']

while True:

    command = input('Enter the command: ')
    if command == 'end':
        break
    if command not in commands:
        print('Wrong command! ')
        continue

    if command == 'write':
        with open('Hotels.txt', 'w') as hotels:
            incHotel = input('Enter the hotel: ')
            if len(incHotel.split()) != 6:
                print('Wrong data!')
                continue
            hotels.write(incHotel + '\n')
    elif command == 'read':
        with open('Hotels.txt', 'r') as hotels:
            print('\n' + hotels.read())
    elif command == 'calculate':
        print(1)
