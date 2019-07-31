def read(file_name):
    with open(file_name, 'r') as file:
        return '\n' + file.read()


def write(file_name, inc_thing):
    with open(file_name, 'a') as file:
        file.write(repr(inc_thing) + '\n')


def listing(file_name):
    with open(file_name, 'r') as items:
        return list(map(lambda row: row[:-1].split('\t'), items.readlines()))
