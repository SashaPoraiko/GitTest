firstW = input('Enter the first word: ')
secondW = input('Enter the second Word: ')
sentence = input('Enter the sentence: ').split()
output = []

for w in sentence:
    if w == firstW:
        output.append(secondW)
        continue
    output.append(w)

print(' '.join(output))
