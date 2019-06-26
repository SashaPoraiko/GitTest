data = input('Enter the sentence: ').split()
result = []
i = 0

while i < len(data):
    if not data[i] in result:
        result.append(data[i])
    i += 1

print(' '.join(result))
