command = ''
bankClients = {}
commands = ['deposit', 'balance', 'withdraw', 'transfer', 'income']
while True:

    command = input('The possible commands: {0}, Enter the command: '.format(commands))
    if command == 'end':
        break

    if command not in commands:
        print('Wrong command, the possible commands are:{0}'.format(commands))
        continue

    # todo fix this
    name = None
    if command != 'income':
        name = input('Enter your name: ')

    if command == 'deposit':
        smr = int(input('Enter the sum: '))
        if smr > 0:
            bankClients[name] = bankClients.get(name, 0) + smr
            print('Congrats! Deposit was successfully! Your current balance is: {0}'.format(bankClients[name]))
        else:
            print('Wrong sum! sum should be more then 0!!')

    elif command == 'withdraw':

        smr = int(input('Enter the sum: '))
        if smr > 0:
            bankClients[name] = bankClients.get(name, 0) - smr
            print('Congrats! Withdraw was successfully! Your current balance is: {0}'.format(bankClients[name]))
        else:
            print('Wrong sum! sum should be more then 0!!')

    elif command == 'balance':
        if name in bankClients:
            print('Your current balance is: {0}'.format(bankClients[name]))
        else:
            print('Error!! U have no balance!!')

    elif command == 'transfer':
        bankClients[name] = bankClients.get(name, 0)
        secondClientName = input('Enter the receiver client name: ')
        summary = int(input('Enter the transfer sum : '))

        bankClients[secondClientName] = bankClients.get(secondClientName, 0)
        bankClients[name] = bankClients.get(name, 0) - summary
        bankClients[secondClientName] = bankClients.get(secondClientName, 0) + summary

        print('The transfer completed, transferred {0}'.format(summary))

    elif command == 'income':
        rate = int(input('Enter the rate: '))
        for key, balance in filter(lambda item: item[1] > 0, bankClients.items()):
            bankClients[key] += int(balance * rate / 100)
        print('Every client with positive balance has been improved!')
