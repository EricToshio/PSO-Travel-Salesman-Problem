from TSPSolver import TSPSolver
from cidades import cities

a = TSPSolver(6)
a.solve()
sol = a.getSolution()

for ind in sol:
    print(cities[ind-1])