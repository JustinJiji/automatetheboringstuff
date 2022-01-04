import random
numberOfStreaks = 0
coinFlip=[]
for experimentNumber in range(10000):

    # Code that creates a list of 100 'heads' or 'tails' values.
    for i in range(100):
        if random.randint(0,1)==0:
            coinFlip.append('H')
        else:
            coinFlip.append('T')

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for j in range(100):
        if coinFlip[j:j+6] == ['H','H','H','H','H','H']:
            numberOfStreaks += 1
        elif coinFlip[j:j+6] == ['T','T','T','T','T','T']:
            numberOfStreaks += 1
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
