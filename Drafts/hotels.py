commands = ['write', 'read', 'end', 'info']

while True:

    command = input('Enter the command: ')
    if command == 'end':
        break
    if command not in commands:
        print('Wrong command! ')
        continue

    if command == 'write':
        with open('Hotels.txt', 'a') as hotelsList:
            incHotel = input('Enter the hotel: ')
            if len(incHotel.split()) != 6:
                print('Wrong data!')
                continue
            hotelsList.write(incHotel + '\n')

    elif command == 'read':
        with open('Hotels.txt', 'r') as hotelsList:
            print('\n' + hotelsList.read())

    elif command == 'info':
        country = input('Enter the country: ')

        with open('Hotels.txt', 'r') as hotels:
            hotelsList = list(map(lambda row: row[:-1].split('\t'), open('Hotels.txt', 'r').readlines()))
            count = 0
            smr = 0
            topCapacity = 0
            topHotel = ''
            for hotel in filter(lambda item: item[2] == country, hotelsList):
                smr += int(hotel[4])
                count += 1
                if int(hotel[5]) > topCapacity:
                    topCapacity = int(hotel[5])
                    topHotel = hotel
            try:
                averageStars = int(smr / count)
            except ZeroDivisionError:
                print('No hotels in this country!!')
            else:
                print('The average hotel stars count in this country is {}'.format(averageStars))
                print(
                    'The biggest hotel in this country is {0}, its located in {1},{2}, and contains {5} peoples'.format(
                        *topHotel))
