testDict = {1: 'Hello', 2: 'NotHello', 3: 'AgainHello'}

searchedW = input('Enter the searched sinonim: ')

for key, value in testDict.items():
    if value == searchedW:
        print(key)
    if str(key) == searchedW:
        print(value)

