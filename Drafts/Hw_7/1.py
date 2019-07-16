buyers = {}
# name/item/count
while True:
    b = input('Enter the data: ').split()
    temp = {}

    if len(b) < 3:
        break

    temp[b[1]] = int(b[2])

    if b[0] not in buyers.keys():
        buyers[b[0]] = temp

    else:
        if buyers[b[0]].get(b[1]) is None:
            pair = {b[1]: int(b[2])}
            buyers[b[0]].update(pair)
        else:
            buyers[b[0]][b[1]] += int(b[2])

print(buyers)
#sorted