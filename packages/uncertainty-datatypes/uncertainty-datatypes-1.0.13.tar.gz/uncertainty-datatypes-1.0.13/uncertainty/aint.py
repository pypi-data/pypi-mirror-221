from __future__ import annotations

from collections.abc import Iterable

from uncertainty.afuncs import *

import math

class aint:

    # Instance attributes:
    # x: int 
    # u: float 
    # sample : Iterable[int]
    
    def __init__(self, x: Iterable|int|str = 0.0, u: float|int|str = 0.0, array: Iterable[int] = [], dist: Distribution = Distribution.UNIFORM) -> aint:
        if x == 0 and u == 0.0 and array: 
            self.__initFromArray()
        elif array:
            self.__setValues(x, u, np.array(array))
        else:
            self.__initFromValues(x, u, dist)

    def __setValues(self, x: int|str, u: float|int|str):
        if not isinstance(x, (int, str)):
            raise ValueError('Invalid parameter: x is not int or float as string')
        elif not isinstance(u, (float, int, str)):
            raise ValueError('Invalid parameter: u is not float, not int or float as string')

        self.x = int(x)
        self.u = float(u)

    def __initFromValues(self, x: int|str, u: float|int|str, dist: Distribution):
        self.__setValues(x, u)

        if self.u == 0.0:
            self.sample = createintZeroSample(self.x)
        else:
            self.sample = createintSample(self.x, self.u, dist)

    def __initFromArray(self, array: Iterable[int]):
        self.sample = np.array(array)
        sum: int = 0.0 
        dev: float = 0.0
        
        length: float = len(self.sample)
        for i in range(length):
            sum += self.sample[i]
            dev += self.sample[i] * self.sample[i]
        
        #  average
        self.x = sum/length
        # standard deviation
        self.u = math.sqrt(abs(dev - ( sum * sum / length)) / (length - 1))

    def __setValues(self, x: int|str, u: float|int|str, array: Iterable[float]):
        self.__setValues(x, u)
        self.sample = array

    @property
    def x(self) -> int:
        return self._x
    
    @property
    def u(self) -> float:
        return self._u
    
    def getSample(self) -> Iterable[int]: #gets a copy of the sample
        return self.sample.copy()
    
    def getLength(self, r: aint = None):
        if r is None:
            return len(self.sample)
        elif len(self.sample) == len(r):
            return len(self.sample)
        elif len(self.sample) != len(r):
            raise ValueError('Different array size: ' + str(len(self.sample)) + ' - ' + str(len(r)))
    
    ''' Type Operations '''
    def add(self, r: aint) -> aint:
        length: int = self.getLength(r)
        sum: int =  0 
        dev: float =  0.0

        result: aint =  aint()
        for i in range(length):
            result.sample[i] = self.sample[i] + r.sample[i]
            sum += result.sample[i]
            dev += result.sample[i] * result.sample[i]

        # average
        result.setX(sum/length)
        #standard deviation
        result.setU(math.sqrt(abs(dev - (sum * sum / length)) / (length - 1)))
        return result
    
    def __add__(self, r) -> aint:
        return self.add(r)
    
    def __radd__(self, left) -> aint:
        return aint(left).__add__(self)

    def minus(self, r: aint) -> aint:
        length: int = self.getLength(r)
        sum: int =  0 
        dev: float =  0.0

        result: aint =  aint()
        for i in range(length):
            result.sample[i] = self.sample[i] - r.sample[i]
            sum += result.sample[i]
            dev += result.sample[i] * result.sample[i]

        # average
        result.setX(sum/length)
        #standard deviation
        result.setU(math.sqrt(abs(dev - (sum * sum / length)) / (length - 1)))
        return result

    def __sub__(self, r: aint):
        return self.minus(r)
    
    def __rsub__(self, left) -> aint:
        return aint(left).__sub__(self)
    
    def mult(self, r: aint) -> aint:
        length: int = self.getLength(r)
        sum: int =  0 
        dev: float =  0.0

        result: aint =  aint()
        for i in range(length):
            result.sample[i] = self.sample[i] * r.sample[i]
            sum += result.sample[i]
            dev += result.sample[i] * result.sample[i]

        # average
        result.setX(sum/length)
        #standard deviation
        result.setU(math.sqrt(abs(dev - (sum * sum / length)) / (length - 1)))
        return result
    
    def __mul__(self, r) -> aint:
        return self.mult(r)
    
    def __rmul__(self, left) -> aint:
        return uint(left).__mul__(self)

    def division(self, r: aint) -> aint:
        length: int = self.getLength(r)
        sum: int =  0 
        dev: float =  0.0

        result: aint =  aint()
        for i in range(length):
            result.sample[i] = self.sample[i] / r.sample[i]
            sum += result.sample[i]
            dev += result.sample[i] * result.sample[i]

        # average
        result.setX(sum/length)
        #standard deviation
        result.setU(math.sqrt(abs(dev - (sum * sum / length)) / (length - 1)))
        return result
    
    def __truediv__(self, r):
        return self.division(r)
    
    def __rtruediv__(self, left) -> aint:
        return aint(left).__truediv__(self)

    ''' self operation returns a ufloat '''
    def divisionR(self, r: aint) -> ufloat:
        length: int = self.getLength()
        sum: int =  0 
        dev: float =  0.0
        x: float = 0.0
        
        for i in range(length):
            x = self.sample[i] / r.sample[i]
            sum += x
            dev += x*x

        result: ufloat =  ufloat()
        # average
        result.setX(sum/length)
        #standard deviation
        result.setU(math.sqrt(abs(dev - (sum * sum / length)) / (length - 1)))
        return result

    def abs(self) -> aint:
        length: int = self.getLength()
        sum: int = 0 
        dev: float = 0.0

        result: aint =  aint()
        for i in range(length):
            result.sample[i] = abs(self.sample[i])
            sum += result.sample[i]
            dev += result.sample[i] * result.sample[i]

        # average
        result.setX(sum/length)
        #standard deviation
        result.setU(math.sqrt(abs(dev - (sum * sum / length)) / (length - 1)))
        return result
    
    def __abs__(self) -> aint:
        return self.abs()
    
    def neg(self) -> aint:
        length: int = self.getLength()
        for i in range(length):
            result.sample[i] = - (self.sample[i])

        result: aint =  aint()
        # average
        result.setX(-self.x)
        #standard deviation
        result.setU(self.u)
        return result
    
    def __neg__(self) -> aint:
        return self.neg()
    
    def power(self, s: float) -> aint:
        length: int = self.getLength()
        sum: int =  0 
        dev: float =  0.0

        result: aint =  aint()
        for i in range(length):
            result.sample[i] = int(math.pow(self.sample[i], s))
            sum += result.sample[i]
            dev += result.sample[i] * result.sample[i]

        # average
        result.setX(sum/length)
        #standard deviation
        result.setU(math.sqrt(abs(dev - (sum * sum / length)) / (length - 1)))
        return result
    
    def sqrt(self) -> aint:
        length: int = self.getLength()
        sum: int =  0 
        dev: float =  0.0

        result: aint =  aint()
        for i in range(length):
            result.sample[i] = int(math.sqrt(self.sample[i]))
            sum += result.sample[i]
            dev += result.sample[i] * result.sample[i]

        # average
        result.setX(sum/length)
        #standard deviation
        result.setU(math.sqrt(abs(dev - (sum * sum / length)) / (length - 1)))
        return result
    
    def __pow__(self, s: float|int) -> aint:
        return self.power(s)

    def inverse(self) -> aint: #inverse (reciprocal)
        return aint(1,0.0).division(self)

    ''' 
       FUZZY COMPARISON OPERATIONS
       using 1-to-1 comparisons is not fair, due to possible reorderings
    '''
    def equals(self, number: aint) -> ubool:
        return self.toufloat().uEquals(number.toufloat())
    
    def __eq__(self, r: uint|ufloat) -> ubool:
        return self.uEquals(r)

    def distinct(self, r: aint) -> ubool:
        return self.equals(r).NOT()
    
    def __eq__(self, r: uint|ufloat) -> ubool:
        return self.uEquals(r)

    def lt(self, number: aint) -> ubool:
        return self.toufloat().lt(number.toufloat())
    
    def __lt__(self, r: uint|ufloat) -> ubool:
        return self.lt(r)
    
    def le(self, number: aint) -> ubool:
        return self.toufloat().le(number.toufloat())

    def __le__(self, r: uint|ufloat) -> ubool:
        return self.le(r)

    def gt(self, number: aint) -> ubool:
        return self.toufloat().gt(number.toufloat())
    
    def __gt__(self, r: uint|ufloat) -> ubool:
        return self.gt(r)

    def ge(self, number: aint) -> ubool:
        return self.toufloat().ge(number.toufloat())
    
    def __ge__(self, r: uint|ufloat) -> ubool:
        return self.ge(r)
   
    '''END OF FUZZY COMPARISON OPERATIONS'''

    def min(self, r: aint) -> aint:
        if r < self:
            return r.copy() 
        return self.copy()
        
    def max(self, r: aint) -> aint:
        if r > self:
            return r.copy()
        return self.copy()

    ''' Conversions '''
    def __str__(self) -> str:
        return 'aint({:5.3f}, {:5.3f}, {:s})'.format(self.x, self.u, str(self.sample))

    def __repr__(self) -> str:
        return self.__str__()
    
    def toint(self) -> int: #
        return int(self.x)
        
    def toint(self) -> ufloat:
        return uint(self.x, self.u)
    
    def tofloat(self) -> ufloat:
        return float(self.x)
    
    def toufloat(self) -> ufloat:
        return ufloat(self.x, self.u)
    
    ''' Other Methods '''
    def __hash__(self):
        return math.round(self.x)

    def copy(self) -> aint:
        return aint(self.x, self.u, self.sample)