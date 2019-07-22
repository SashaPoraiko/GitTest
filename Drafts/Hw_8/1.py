commands = ['write', 'read', 'end', 'search']

while True:

    command = input('Enter the command: ')
    if command == 'end':
        break

    if command == 'write':
        myFile = open('Stadiums.txt', 'a')
        inpStr = input('Enter the data: ')
        inpList = inpStr.split('\t')
        if len(inpList) != 5 or command not in commands:
            print('Wrong data!')
            myFile.close()
            continue
        else:
            myFile.write(inpStr + '\n')
            myFile.close()

    elif command == 'read':
        myFile = open('Stadiums.txt', 'r')
        print('\n' + myFile.read())
        myFile.close()

    elif command == 'search':
        country = input('Enter the country: ')
        myFile = open('Stadiums.txt', 'r')
        stadiums = myFile.readlines()
        oldestVal = int(stadiums[0].split('\t')[4])
        oldestStadium = ''
        totalCapacity = 0
        for stadium in stadiums:
            if stadium.split('\t')[2] == country:
                totalCapacity += int(stadium.split('\t')[3])
                if int(stadium.split('\t')[4]) <= oldestVal:
                    oldestVal = int(stadium.split('\t')[4])
                    oldestStadium = stadium

        print(
            'The oldest stadium of this country is: {0}, and the total capacity of this country stadiums is: {1}'.format(
                oldestStadium, totalCapacity))
        myFile.close()
