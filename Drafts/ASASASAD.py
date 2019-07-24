commands = ['end', 'write', 'read', 'calculate_semester', 'calculate_lecturers']


def calculate_things_semester(file_name):
    semester = input('Enter the semester number: ')
    with open(file_name, 'r') as items:
        disciplines_list = list(map(lambda row: row[:-1].split('\t'), items.readlines()))
        total_hours = 0
        for discipline in filter(lambda x: x[1] == semester, disciplines_list):
            total_hours += int(discipline[2])
    print('The total hours for current semester is: {}'.format(total_hours))


def calculate_unique_lecturers(file_name):
    with open(file_name, 'r') as items:
        disciplines_list = list(map(lambda row: row[:-1].split('\t'), items.readlines()))
        lecturers_list = []
        for discipline in filter(lambda x: x[4] not in lecturers_list, disciplines_list):
            lecturers_list.append(discipline[4])
        print('The unique lecturers list is: {}'.format(lecturers_list))


def read(file_name):
    with open(file_name, 'r') as thingList:
        print('\n' + thingList.read())


def write(file_name):
    with open(file_name, 'a') as thing_list:
        inc_thing = input('Enter the Thing: ')
        if not validate(inc_thing.split('\t')):
            print('Wrong data!')
        else:
            thing_list.write(inc_thing + '\n')


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
        elif command == 'calculate_semester':
            calculate_things_semester(file)
        elif command == 'calculate_lecturers':
            calculate_unique_lecturers(file)


if __name__ == '__main__':
    run()
