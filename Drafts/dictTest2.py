bank = []
name = ''
while True:
    command = input('Enter the command: ')
    name = input('Enter the name: ')
    klient = {}
    if command == 'Deposit':
        if name not in bank:
            klient[name] = int(input('Enter the sum'))
        else:
            klient[name] += int(input('Enter the sum'))
        bank.append(klient)
    elif command == 'Withdraw':
        if name not in bank:
            klient[name] = int(input('Enter the sum'))
        else:
            klient[name] -= int(input('Enter the sum'))
    elif command == 'Balance':
        if name not in bank:
            klient[name] = int(input('U have no balance: '))
        else:
            print('Your current balance is: {0}'.format(klient[name]))
