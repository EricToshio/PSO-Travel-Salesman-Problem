from abc import ABC, abstractmethod 
import copy

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
