command = ''
bankClients = {}

while True:

    command = input('Enter the command: ')
    if command == 'end':
        break

    name = input('Enter your name: ')

    if name not in bankClients:
        bankClients[name] = 0

    if command == 'deposit':
        bankClients[name] += int(input('Enter the sum: '))

    elif command == 'withdraw':
        bankClients[name] -= int(input('Enter the sum: '))

    elif command == 'balance':
        print('Your current balance is: {0}'.format(bankClients[name]))

    elif command == 'transfer':
        firstClientName = input('Enter the sender client name: ')
        secondClientName = input('Enter the receiver client name: ')
        summary = int(input('Enter the transfer sum : '))

        if firstClientName not in bankClients:
            bankClients[firstClientName] = 0
        if secondClientName not in bankClients:
            bankClients[secondClientName] = 0
        if summary > bankClients[firstClientName]:
            print('There are not enough funds on your account to transfer')
        else:
            bankClients[firstClientName] -= summary
            bankClients[secondClientName] += summary
            print('The transfer completed, transferred {0}'.format(summary))

    elif command == 'income':
        rate = int(input('Enter the rate: '))
        for key, funds in bankClients.items():
            if funds > 0:
                funds += int(funds / 100 * rate)
