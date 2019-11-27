import random
from abc import ABC, abstractmethod 
import copy

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

class DiscreteDimension(ABC):
    def __init__(self):
        pass
        type = None
        values = None
    
    def __add__(self, other):
        if self.type == 'position' and other.type == 'velocity':
            returnObj = copy.deepcopy(self)
            for swap in other.values:
                i,j = swap
                returnObj.values[i], returnObj.values[j] = returnObj.values[j], returnObj.values[i]
            return returnObj
        
        if self.type == 'velocity' and other.type == 'position':
            returnObj = copy.deepcopy(other)
            for swap in self.values:
                i,j = swap
                returnObj.values[i], returnObj.values[j] = returnObj.values[j], returnObj.values[i]
            return returnObj
        
        if self.type == 'velocity' and other.type == 'velocity':
            returnObj = copy.deepcopy(self)
            returnObj.values.extend(other.values)
            return returnObj
        
        print("DiscreteDimension(Class): operation not specified")
        return 
    
    def __sub__(self, other):
        if self.type == 'position' and self.type == 'position':
            returnObj = copy.deepcopy(self)
            returnObj.values = []
            returnObj.type = 'velocity'
            auxObj = copy.deepcopy(other)
            for i in range(len(self.values)):
                if auxObj.values[i] != self.values[i]:
                    j = auxObj.values.index(self.values[i])
                    swap = (i,j)
                    returnObj.values.append(swap)
                    auxObj.values[i], auxObj.values[j] = auxObj.values[j], auxObj.values[i]
            return returnObj
    
    # def __mul__(self, other):
    #     same as rmul

    def __rmul__(self, other):
        if self.type == 'velocity':
            if other < 0:
                print("DiscreteDimension(Class): operation not specified: multiplication by negative number")
                return 
            if other > 1:
                returnObj = copy.deepcopy(self)
                integerPart = int(other)
                fracPart = int(other*10)%10
                returnObj.values = returnObj.values * integerPart
                returnObj.values.extend(self.values[:fracPart])
                return returnObj
            if other == 0:
                returnObj = copy.deepcopy(self)
                returnObj.values = []
                return returnObj
            
            fracPart = int(other*10)%10
            returnObj = copy.deepcopy(self)
            returnObj.values = returnObj.values[:fracPart]
            return returnObj
    
    def __str__(self):
        return f"{self.values}, type={self.type}"


class Position(DiscreteDimension):
    def __init__(self):
        DiscreteDimension.__init__(self)
        self.type = 'position'
        self.values = []

class Velocity(DiscreteDimension):
    def __init__(self):
        DiscreteDimension.__init__(self)
        self.type = 'velocity'
        self.values = []


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



