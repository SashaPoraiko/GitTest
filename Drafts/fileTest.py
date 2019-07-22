while True:

    command = input('Enter the command: ')
    if command == 'end':
        break

    if command == 'write':
        myFile = open('Db.txt', 'a')
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
        myFile = open('Db.txt', 'r')
        print('\n' + myFile.read())
        myFile.close()

    elif command == 'search':
        searchedWord = input('Enter searched word: ')
        myFile = open('Db.txt', 'r')
        for line in myFile.readlines():
            for word in line.split():
                if searchedWord in word:
                    print(line)
                    break
        myFile.close()

    elif command == 'topcar':
        topValCar = 0
        topCar = ''
        searchedYear = input('Enter the year: ')
        myFile = open('Db.txt', 'r')
        for car in myFile.readlines():
            if car.split('\t')[3] == searchedYear and int(car.split('\t')[4]) > topValCar:
                topValCar = int(car.split('\t')[4])
                topCar = car
        print('The most expensive car of {0} year is {1}'.format(searchedYear, topCar))
        myFile.close()

    elif command == 'totalsum':
        myFile = open('Db.txt', 'r')
        total = 0
        cars = myFile.readlines()
        for car in cars:
            total += int(car.split('\t')[4])
        print('The total sum of all cars is: {0}'.format(total))
        myFile.close()
