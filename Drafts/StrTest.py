text1 = 'myte txtt asdal dasd'.split()
text2 = input('txtx').split()
res = []
for w in text1:
    if w not in text2:
        res.append(w)
print(res)
print(' '.join(res))
