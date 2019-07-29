import file_modules

commands = ['end', 'write', 'read', 'calculate']


def calculate_things_semester(file_name):
    semester = input('Enter the semester number: ')
    disc_list = file_modules.listing(file_name)
    total_hours = 0
    for discipline in filter(lambda x: x[1] == semester, disc_list):
        total_hours += int(discipline[2])
    return total_hours


def calculate_unique_lecturers(file_name):
    disc_list = file_modules.listing(file_name)
    lecturers_list = []
    for discipline in filter(lambda x: x[4] not in lecturers_list, disc_list):
        lecturers_list.append(discipline[4])
    return lecturers_list


def read(file_name):
    print(file_modules.read(file_name))


def write(file_name):
    inc_thing = input('Enter the Thing: ')
    if not validate(inc_thing.split('\t')):
        print('Wrong data!')
        return
    file_modules.write(file_name, inc_thing)


def validate(data):
    return len(data) == 5


def run():
    file = 'Things.txt'
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
            print('The total hours for current semester is: {}'.format(calculate_things_semester(file)))
            print('The unique lecturers list is: {}'.format(calculate_unique_lecturers(file)))


if __name__ == '__main__':
    run()
