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
        stadiums = list(map(lambda row: row[:-1].split('\t'), myFile.readlines()))

        oldestVal = None
        oldestStadium = None
        totalCapacity = 0
        for stadium in filter(lambda item: item[2] == country, stadiums):
            totalCapacity += int(stadium[3])
            if oldestStadium is None or int(stadium[4]) < oldestVal:
                oldestVal = int(stadium[4])
                oldestStadium = stadium
        if oldestStadium is None:
            print('not found')
        else:
            print('The total capacity of this country stadiums is: {0}'.format(totalCapacity))
            print(stadiums)
            print(
                'The oldest stadium of this country is {0}, its located in {1},'
                ' {2}, and was built in {4}'.format(*oldestStadium))
        myFile.close()
