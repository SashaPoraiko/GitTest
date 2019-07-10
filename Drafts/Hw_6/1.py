firstState = {'Obama': 3, 'Trump': 2, 'Linkoln': 4}
secondState = {'Obama': 4, 'Trump': 12, 'Linkoln': 42}
thirdState = {'Obama': 13, 'Trump': 12, 'Linkoln': 8}

statesLst = [firstState, secondState, thirdState]

obamaSum = 0
trumpSum = 0
linkolnSum = 0

for state in statesLst:
    for key, value in state.items():
        if key == 'Obama':
            obamaSum += state['Obama']
        elif key == 'Trump':
            trumpSum += state['Trump']
        else:
            linkolnSum += state['Linkoln']



print(obamaSum, trumpSum, linkolnSum)

