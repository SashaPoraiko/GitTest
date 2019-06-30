firstText = input('Enter the first text: ').split()
secondText = 'TRIGGERED'

triggerWord = 'on'
i = 0

while i < len(firstText):
    if firstText[i] == triggerWord:
        firstText[i] += ' ' + secondText
    i += 1

print(' '.join(firstText))
