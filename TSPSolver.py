from utils import fitness, generateRandomPosition, generateRandomSwap
import random
from DiscreteDimension import Position, Velocity
from Particle import Particle

NUMBER_OF_ITERATIONS = 1000
NUMBER_OF_PARTICLES = 20

class TSPSolver:
    def __init__(self, numberOfCities):
        self.solution = None
        self.numberOfParticles = NUMBER_OF_PARTICLES
        self.swarm = [Particle(numberOfCities) for _ in range(self.numberOfParticles)]
        self.iteration = 0

    def solve(self):
        gBestPosition = Position()
        gBestPosition.values = self.swarm[0].position.values
        gbest = (gBestPosition, self.swarm[0].pbest[1])
        gbest = self.updateGBest(gbest)

        i = 0
        while i < NUMBER_OF_ITERATIONS:
            self.iteration += 1
            i += 1
            for p in self.swarm:
                p.update(gbest[0])
            gbest = self.updateGBest(gbest)
        
        self.solution = gbest[0].values
        print(gbest[1], self.iteration, self.solution)
    
    def updateGBest(self, gbestValue):
        gbest = gbestValue
        for p in self.swarm:
            if p.pbest[1] < gbest[1]:
                gbest = (p.pbest[0],p.pbest[1])
        
        return gbest

a = TSPSolver(5)
a.solve()

