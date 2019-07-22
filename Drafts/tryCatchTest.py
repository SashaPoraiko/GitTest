numbers = open('Numbers.txt', 'r')
arr = []

try:
    for line in numbers:
        arr.append(int(line))
except ValueError:
    print('Error! its not int!')
except Exception:
    print('Some other error')
else:
    print('Its okay')
finally:
    numbers.close()
    print('The file is closed')
