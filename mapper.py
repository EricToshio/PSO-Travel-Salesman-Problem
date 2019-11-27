from utils import fitness, generateRandomPosition, generateRandomSwap
from DiscreteDimension import Position, Velocity
import random

class Particle:
    def __init__(self, id, data):
        self.id = id
        self.N = data.nOfParticles
        self.position = Position()
        self.position.values = data.position
        self.velocity = Velocity()
        self.velocity.values = data.velocity
        self.pbest = (data.pbest, data.pbest_fitness)
        self.gbest = data.gbest
        self.gbest_fitness = data.gbest_fitness

        self.omega = 0.7
        self.alfa = 1.2
        self.beta = 2.3
    
    def update(self, gbest):
        self.r1 = random.uniform(0,1)
        self.r2 = random.uniform(0,1)
        
        inertiaFactor = self.omega*self.velocity
        cognitiveFactor = self.alfa*self.r1*(self.pbest[0] - self.position)
        socialFactor = self.beta*self.r2*(self.gbest_particle - self.position)
        
        self.velocity = inertiaFactor + cognitiveFactor + socialFactor
        self.position = self.position + self.velocity

        if fitness(self.position.values) < self.pbest[1]:
            self.pbest = (self.position, fitness(self.position.values))
    
    def make_message(self):
        a = str(-1)
        b = str(self.position)
        c = str(self.velocity)
        d = str(self.fitness)
        e = str(self.pbest_particle)
        f = str(self.pbest_fitness)
        g = str(self.gbest_particle)
        h = str(self.gbest_fitness)
        return ':'.join([a,b,c,d,e,f,g,h])
    
    def getParticleInfo(self):
        a = str(self.id)
        b = str(self.position)
        c = str(self.velocity)
        d = str(self.fitness)
        e = str(self.pbest_particle)
        f = str(self.pbest_fitness)
        g = str(self.gbest_particle)
        h = str(self.gbest_fitness)
        return ':'.join([a,b,c,d,e,f,g,h])
        

def parseData(data):
    nOfParticles, position, velocity, fitness, pbest_particle, pbest_fitness, gbest_particle, gbest_fitness = data.split(':')

    return {
        nOfParticles: int(nOfParticles),
        position: Position(position),
        velocity: Velocity(velocity),
        fitness: float(fitness),
        pbest: Position(pbest_particle),
        pbest_fitness: float(fitness),
        gbest: Position(gbest_particle),
        gbest_fitness: float(gbest_fitness),
    }


def mapper(mapperInput):
    # verificar se mapperInput eh string
    id, stringfiedData = eval(mapperInput)
    
    
    # parse data
    data = parseData(id, stringfiedData)

    # update particle velocity
    particleObj = Particle(data)
    particleObj.update()

    message = particle.make_message()
    emits = []
    for i in range(data.nOfParticles):
        if i != id:
            emits.append((i, message))
    
    newParticleInfo = particle.getParticleInfo()

    emits.append((id, newParticleInfo))
    return emits



