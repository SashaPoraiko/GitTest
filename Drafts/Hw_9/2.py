commands = ['end', 'write', 'read', 'calculate']


def write(file_name):
    with open(file_name, 'a') as countries:
        inc_client = input('Enter the Client: ')
        if not validate(inc_client.split('\t')):
            print('Wrong data!')
        else:
            countries.write(inc_client + '\n')


def listed_countries(file_name):
    with open(file_name, 'r') as items:
        return list(map(lambda row: row[:-1].split('\t'), items.readlines()))


def calculate_continent_countries(file_name, continent):
    country_list = listed_countries(file_name)
    smr = 0
    for cont in filter(lambda x: x[1] == continent, country_list):
        smr += 1
    return smr


def calculate_most_populated(file_name, continent):
    country_list = listed_countries(file_name)
    most_populated = country_list[0]
    for country in filter(lambda x: x[1] == continent and x[2] > most_populated[2], country_list):
        most_populated = country
    return country


def validate(data):
    return len(data) == 6


def read(file_name):
    with open(file_name, 'r') as countries:
        print('\n' + countries.read())


def run():
    file = 'countries.txt'
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
            continent = input('Enter the continent: ')
            print('This continent include {} countries'.format(calculate_continent_countries(file, continent)))
            print(
                'The most populated country in this continent is: {}'.format(calculate_most_populated(file, continent)[0]))


if __name__ == '__main__':
    run()
