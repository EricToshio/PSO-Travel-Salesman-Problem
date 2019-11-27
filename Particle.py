from utils import fitness, generateRandomPosition, generateRandomSwap

class Particle:
    def __init__(self, N):
        self.N = N
        self.position = Position()
        self.position.values = generateRandomPosition(N)
        self.velocity = Velocity()
        self.velocity.values = generateRandomSwap(N)
        self.pbest = (self.position, fitness(self.position.values))
        self.omega = 0.7
        self.alfa = 1.2
        self.beta = 2.3
    
    def update(self, gbest):
        self.r1 = random.uniform(0,1)
        self.r2 = random.uniform(0,1)
        
        inertiaFactor = self.omega*self.velocity
        cognitiveFactor = self.alfa*self.r1*(self.pbest[0] - self.position)
        socialFactor = self.beta*self.r2*(gbest - self.position)
        
        self.velocity = inertiaFactor + cognitiveFactor + socialFactor
        self.position = self.position + self.velocity

        if fitness(self.position.values) > self.pbest[1]:
            self.pbest = (self.position, fitness(self.position.values))