# Project Euler Problem 54
# by Connor Halleck-Dube

import time
t0 = time.clock()

## Solution 1: Elaborate numerical system

Ranks = {'highcard':0, 'pair':1, 'twopair':2, 'threekind':3, 'straight':4, 'flush':5, 'fullhouse':6, 'fourkind':7, 'sflush':8, 'rflush':9}

# returns a list, the first element of which is the hand's rank, 
# the second is the sum of the hand's values, 
# the third-seventh are the cards ordered from highest to lowest
convert = {'2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9': 8, 'T':9, 'J':10, 'Q':11, 'K':12, 'A':13}
def evaluate(hand):
    # This list will be returned
    worth = []
    
    # Hold numerical card values and suit chars, respectively
    values = []
    suits = []
    for card in hand:
        values.append(convert[card[0]])
        suits.append(card[1])
    
    # Evaluate properties of the hand
    counts = cardCount(values)
    onesuit = isSameSuit(suits)
    straight = isStraight(values)
    
    # Evaluates the hand
    if onesuit and sum(values) == 55: # Royal Flush
        worth.append(Ranks['rflush'])
    elif onesuit and straight: # Straight Flush
        worth.append(Ranks['sflush'])
    elif (counts[0][0] == 4): # etc
        worth.append(Ranks['fourkind'])
        worth.append(counts[0][1])
        worth.append(counts[1][1])
    elif (counts[0][0] == 3) and (counts[1][0] == 2):
        worth.append(Ranks['fullhouse'])
        worth.append(counts[0][1])
        worth.append(counts[1][1])
    elif onesuit:
        worth.append(Ranks['flush'])
    elif straight:
        worth.append(Ranks['straight'])
    elif (counts[0][0] == 3):
        worth.append(Ranks['threekind'])
        worth.append(counts[0][1])
    elif (counts[0][0] == 2) and (counts[1][0] == 2):
        worth.append(Ranks['twopair'])
        worth.append(counts[0][1])
        worth.append(counts[1][1])
    elif (counts[0][0] == 2):
        worth.append(Ranks['pair'])
        worth.append(counts[0][1])
    else:
        worth.append(Ranks['highcard'])
    
    # Adds the cards from highest to lowest into worth
    values.sort()
    values.reverse()
    for value in values:
        worth.append(value)
    return worth
    
def isSameSuit(suits):
    return len(set(suits)) == 1
    
# Returns a pair of two-item lists
# maxcount is (highest appearance count, card value)
# secondcount is (second highest appearance count, card value)
def cardCount(values):
    # calculate the top two appearance counts
    maxcount = [0, 0] 
    secondcount = [0, 0]
    for i in set(values):
        count = (values.count(i), i)
        if (count[0] > maxcount[0]):
            secondcount = maxcount
            maxcount = count
        elif (count[0] > secondcount[0]):
            secondcount = count
    return (maxcount, secondcount)

def isStraight(values):
    for i in range(13):
        if sorted([(v+i)%13 for v in values]) == [0, 1, 2, 3, 4]:
            return True
    return False

# Compare two evaluate lists first by rank, then by values, then by high cards
def oneWinner(v1, v2):
    i = 0
    while v1[i] == v2[i]:
        i += 1
    return v1[i] > v2[i]
    

f = open('poker.txt')
onewins = 0
for line in f:
    list = line[:len(line)-1].split(' ')
    v1 = evaluate(list[:5])
    v2 = evaluate(list[5:])
    
    # Compare first by rank, then by values, then by high cards until something is unequal
    if oneWinner(v1, v2):
        onewins += 1
print(onewins)

## End Solution 1

t1 = time.clock()
print("Solution 1 took:", round(t1-t0, 4), "seconds.")
