sum = float(input())
if sum > 1000:
    print('U have 10% discount, your price will be: ', sum - ((sum / 100) * 10))
else:
    print('U have no discount,your price is: ', sum)

