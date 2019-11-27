from itertools import combinations
import random

# Receive a state and return the number
# of non-attacking pairs of queens
def fitness(state):
    indexes = [c for c in range(len(state))]
    pairs = list(combinations(indexes,2))
    
    def isNonAttackingPair(pair):
        i,j = pair
        if state[i] == state[j]:
            return False
        dcol = abs(i-j)
        drow = abs(state[i] - state[j])
        if dcol == drow:
            return False
        return True
    
    score = 0
    for pair in pairs:
        score = score + 1 if isNonAttackingPair(pair) else score

    return score

# Return a list with random numbers
# between 1 and 8 inclusive representing
# a particle on PSO algorithm
def generateRandomParticle(N):
    particle = []
    for i in range(N):
        randomPosition = random.randint(1,8)
        particle.append(randomPosition)
    
    return particle

def generateRandomPosition(N):
    l = [c+1 for c in range(N)]
    position = []
    for j in range(N):
        indexChosen = random.randint(0,len(l)-1)
        position.append(l[indexChosen])
        del l[indexChosen]
    return position

def generateRandomSwap(N):
    numOfSwaps = random.randint(1,5)
    swaps = []
    for _ in range(numOfSwaps):
        i = random.randint(0,N-1)
        j = random.randint(0,N-1)
        swaps.append((i,j))
    return swaps

