while True:

    command = input('Enter the command: ')
    if command == 'end':
        break

    if command == 'write':
        myFile = open('Stadiums.txt', 'a')
        inpStr = input('Enter the data: ')
        inpList = inpStr.split('\t')
        if len(inpList) != 7:
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
        oldestVal = int(myFile.readlines()[0][4])
        oldestStadium = ''
        totalCapacity = 0
        for stadium in myFile.readlines():
            if stadium[2] == country and int(stadium[4]) < oldestVal:
                oldestVal = int(stadium[4])
                oldestStadium = stadium
            totalCapacity += int(stadium[3])
        print(
            'The oldest stadium of this country is: {0}, and the total capacity of this country stadiums is: {1}'.format(
                oldestStadium, totalCapacity))
        myFile.close()
