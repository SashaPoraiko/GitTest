commands = ['end', 'write', 'read', 'calculate']


def write(file_name):
    with open(file_name, 'a') as bank_clients:
        inc_client = input('Enter the Client: ')
        if not validate(inc_client.split('\t')):
            print('Wrong data!')
        else:
            bank_clients.write(inc_client + '\n')


def listed_clients(file_name):
    with open(file_name, 'r') as items:
        return list(map(lambda row: row[:-1].split('\t'), items.readlines()))


def calculate_credits(file_name):
    clients_list = listed_clients(file_name)
    smr = 0
    for client in clients_list:
        smr += int(client[4])
    return smr


def youngest_creditor(file_name):
    clients_list = listed_clients(file_name)


def validate(data):
    return len(data) == 6


def read(file_name):
    with open(file_name, 'r') as bank_clients:
        print('\n' + bank_clients.read())


def run():
    file = 'bank_clients.txt'
    while True:

        command = input('Enter the command: ')
        if command == 'end':
            break
        if command not in commands:
            print('Wrong command! ')
            continue

        if command == 'write':
            write(file)
        elif command == 'read':
            read(file)
        elif command == 'calculate':
            print('The total credits sum is: {}'.format(calculate_credits(file)))
            print('The youngest creditor is: {}')


if __name__ == '__main__':
    run()
