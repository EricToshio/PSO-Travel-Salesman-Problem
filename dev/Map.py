import random
import math

class Map:
    def __init__(self, num_nodes):
        self.MIN_POS = 1
        self.MAX_POS = 100

        self.nodes = []
        for _ in range(num_nodes):
            self.nodes.append(self.generateNode()) 

    def generateNode(self):
        x = random.randint(self.MIN_POS, self.MAX_POS)
        y = random.randint(self.MIN_POS, self.MAX_POS)
        return (x,y)

    @staticmethod
    def distance(node1, node2):
        return math.sqrt((node1[0]-node2[0])**2+(node1[1]-node2[1])**2)


if __name__ == "__main__":
    map = Map(10)
    print(map.nodes)
    print(Map.distance(map.nodes[0],map.nodes[1]))

