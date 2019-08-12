import shelve


def save_into_shelve(file, key, instances):
    with shelve.open(file, flag='n') as f:
        for item in instances:
            f[getattr(item, key, '')] = item


def read_from_shelve(file):
    with shelve.open(file, flag='r') as f:
        return list(f.values())


def add_single(file, key, thing):
    with shelve.open(file) as f:
        f[getattr(thing, key, '')] = thing


def find_single(file, key):
    with shelve.open(file, flag='r') as f:
        return filter(lambda x: x == key, f.keys())
