###
res = {}
while True:
    country = input('Enter the country:')
    if country == '':
        break
    cities = input('Enter the cities: ').split()

    res[country] = cities

searchedCity = input('Enter the searched city: ')

for key, value in res.items():
    if searchedCity in res[key]:
        print('the country is{0}'.format(key))
