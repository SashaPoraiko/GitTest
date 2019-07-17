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
