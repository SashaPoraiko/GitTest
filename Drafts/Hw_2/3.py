firstW = input('Enter the first word: ')
secondW = input('Enter the second Word: ')
sentence = input('Enter the sentence: ').split()
result = []

for w in sentence:
    if w == firstW:
        result.append(secondW)
        continue
    result.append(w)

print(' '.join(result))
