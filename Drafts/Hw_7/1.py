buyers = {}

# name/item/count
while True:
    command = input('Enter the command: ')

    if command == 'end':
        break
    if command == 'write':
        temp = {}

        name, product, count = input('Enter the data: ').split()
        count = int(count)

        buyers[name][product] = buyers.setdefault(name, {}).get(product, 0) + count
        print(buyers)
    if command == 'read':
        for name in sorted(buyers.keys()):
            print(name + ':')
            for product in sorted(buyers[name].keys()):
                print('\t', product, buyers[name][product])
