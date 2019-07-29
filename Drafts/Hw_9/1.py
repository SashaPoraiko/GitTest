import file_modules
from functools import reduce

commands = ['end', 'write', 'read', 'calculate']


def write(file_name):
    inc_client = input('Enter the Client: ')
    if not validate(inc_client.split('\t')):
        print('Wrong data!')
        return
    file_modules.write(file_name, inc_client)


def calculate_credits(file_name):
    clients_list = file_modules.listing(file_name)
    return reduce(lambda l, r: l + int(r[4]), clients_list, 0)


def youngest_creditor(file_name):
    clients_list = file_modules.listing(file_name)


def validate(data):
    return len(data) == 6


def read(file_name):
    print(file_modules.read(file_name))


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
