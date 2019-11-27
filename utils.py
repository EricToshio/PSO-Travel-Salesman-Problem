from itertools import combinations
import random

# Receive a state and return the number
# of non-attacking pairs of queens
# def fitness(state):
#     indexes = [c for c in range(len(state))]
#     pairs = list(combinations(indexes,2))
    
#     def isNonAttackingPair(pair):
#         i,j = pair
#         if state[i] == state[j]:
#             return False
#         dcol = abs(i-j)
#         drow = abs(state[i] - state[j])
#         if dcol == drow:
#             return False
#         return True
    
#     score = 0
#     for pair in pairs:
#         score = score + 1 if isNonAttackingPair(pair) else score

#     return score

from cidades import cities

def fitness(state):
    total = 0
    for i in range(len(state)-1):
        a = state[i+1] - 1
        b = state[i] - 1
        cityPosition1 = cities[a][1]
        cityPosition2 = cities[b][1]
        dist = (cityPosition1[0] - cityPosition2[0])**2 + (cityPosition1[1] - cityPosition2[1])**2
        total += dist 
    # dist = (positions[state[0]][0] - positions[state[-1]][0])**2 + (positions[state[0]][1] - positions[state[-1]][1])**2
    return total

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
    numOfSwaps = random.randint(1,N//2)
    swaps = []
    for _ in range(numOfSwaps):
        i = random.randint(0,N-1)
        j = random.randint(0,N-1)
        swaps.append((i,j))
    return swaps

