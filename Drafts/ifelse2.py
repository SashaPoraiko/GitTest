sum = float(input())
if sum > 1000:
    print('U have 5% discount, your price will be: {0}'.format(sum - ((sum / 100) * 5)))
elif sum > 500:
    print('U have 3%  discount,your price is: {0}'.format(sum - ((sum / 100) * 3)))
else:
    print('U have no discount,your price is {0}'.format(sum))
