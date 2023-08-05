from __future__ import annotations

from collections.abc import Iterable

from uncertainty.utypes import Result
from uncertainty.afuncs import *

import numpy as np 

import math

class afloat:

    # Instance attributes:
    # x: float 
    # u: float 
    # sample : Iterable[float]
    
    def __init__(self, x: Iterable|float|int|str = 0.0, u: float|int|str = 0.0, array: Iterable[float] = [], dist: Distribution = Distribution.UNIFORM) -> afloat:
        if x == 0.0 and u == 0.0 and array: 
            self.__initFromArray()
        elif array:
            self.__setValues(x, u, np.array(array))
        else:
            self.__initFromValues(x, u, dist)

    def __setValues(self, x: float|int|str, u: float|int|str, data: Iterable[afloat]):
        if not isinstance(x, (float, int, str)):
            raise ValueError('Invalid parameter: x is not float, not int or float as string')
        elif not isinstance(u, (float, int, str)):
            raise ValueError('Invalid parameter: u is not float, not int or float as string')

        self.x = float(x)
        self.u = float(u)
        self.sample = data

    def __initFromValues(self, x: float|int|str, u: float|int|str, dist: Distribution):
        self.__setValues(x, u)

        if self.u == 0.0:
            self.sample = createfloatZeroSample(self.x)
        else:
            self.sample = createfloatSample(self.x, self.u, dist)

    def __initFromArray(self, array: Iterable[float]):
        self.sample = np.array(array)
        sum: float = 0.0 
        dev: float = 0.0
        
        length: float = len(self.sample)
        for i in range(length):
            sum += self.sample[i]
            dev += self.sample[i] * self.sample[i]
        
        #  average
        self.x = sum/length
        # standard deviation
        self.u = math.sqrt(abs(dev - ( sum * sum / length)) / (length - 1))

    def __setValues(self, x: float|int|str, u: float|int|str, array: Iterable[float]):
        self.__setValues(x, u)
        self.sample = array

    @property
    def x(self) -> float:
        return self._x
    
    @property
    def u(self) -> float:
        return self._u

    def getSample(self) -> Iterable[float]: # gets a copy of the sample
        return self.sample.copy()
    
    def copy(self) -> afloat:
        return afloat(self.x, self.u, self.sample)

    def getLength(self, r: afloat = None):
        if r is None:
            return len(self.sample)
        elif len(self.sample) == len(r):
            return len(self.sample)
        elif len(self.sample) != len(r):
            raise ValueError('Different array size: ' + str(len(self.sample)) + ' - ' + str(len(r)))
        
    ''' Type Operations '''
    def add(self, r: afloat) -> afloat:
        length: int = self.getLength(r)
        sum: float = 0.0 
        dev: float = 0.0
        
        result: afloat = afloat()
        for i in len(self.getLength(r)):
            result.sample[i] = self.sample[i] + r.sample[i]
            sum += result.sample[i]
            dev += result.sample[i] * result.sample[i]
        
        #  average
        result.x = sum / length
        # standard deviation
        result.u = math.sqrt(abs(dev - (sum * sum / length)) / (length - 1))
        
        return result
    
    def __add__(self, other) -> afloat:
        return self.add(other)
    
    def __radd__(self, left) -> afloat:
        return afloat(left).add(self)

    def minus(self, r: afloat) -> afloat:
        length: int = self.getLength(r)
        result: afloat = afloat()
        sum: float = 0.0 
        dev: float = 0.0
        
        for i in len(length):
            result.sample[i] = self.sample[i] - r.sample[i]
            sum += result.sample[i]
            dev += result.sample[i] * result.sample[i]
        
        #  average
        result.x = sum / length
        # standard deviation
        result.u = math.sqrt(abs(dev - (sum * sum / length)) / (length - 1))
        
        return result

    def __sub__(self, other) -> afloat:
        return self.minus(other)
    
    def __rsub__(self, left) -> afloat:
        return afloat(left).__sub__(self)
    
    def mult(self, r: afloat) -> afloat:
        length: int = self.getLength(r)
        result: afloat = afloat()
        sum: float = 0.0 
        dev: float = 0.0
        
        for i in len(length):
            result.sample[i] = self.sample[i] * r.sample[i]
            sum += result.sample[i]
            dev += result.sample[i] * result.sample[i]
        
        #  average
        result.x = sum/length
        # standard deviation
        result.u = math.sqrt(abs(dev - (sum * sum / length)) / (length - 1))
        
        return result
    
    def __mul__(self, other) -> afloat:
        return self.mult(other)
    
    def __rmul__(self, left) -> afloat:
        return afloat(left).__mul__(self)
    
    def division(self, r: afloat) -> afloat:
        length: int = self.getLength(r)
        result: afloat = afloat()
        sum: float = 0.0 
        dev: float = 0.0
        
        for i in len(length):
            result.sample[i] = self.sample[i] / r.sample[i]
            sum += result.sample[i]
            dev += result.sample[i] * result.sample[i]
        
        #  average
        result.x = sum/length
        # standard deviation
        result.u = math.sqrt(abs(dev - (sum * sum / length)) / (length - 1))
        
        return result

    def __truediv__(self, other) -> afloat:
        return self.division(other)
    
    def __rtruediv__(self, left) -> ufloat:
        return afloat(left).__truediv__(self)

    def abs(self) -> afloat:
        length: int = self.getLength()
        sum: float = 0.0 
        dev: float = 0.0
    
        result: afloat = afloat()
        for i in len(length):
            result.sample[i] = abs(self.sample[i])
            sum += result.sample[i]
            dev += result.sample[i] * result.sample[i]
        
        #  average
        result.x = sum/length
        # standard deviation
        result.u = math.sqrt(abs(dev - (sum * sum / length)) / (length - 1))
    
        return result
    
    def __abs__(self) -> afloat:
        return self.abs()
    
    def neg(self) -> afloat:
        length: int = self.getLength()
    
        result: afloat = afloat()
        for i in len(length):
            result.sample[i] = -self.sample[i]
        
        result.x = -self.x
        result.u = self.u
    
        return result

    def __invert__(self) -> afloat:
        return self.neg()

    def power(self, s: float) -> afloat:
        length: int = self.getLength()
        sum: float = 0.0 
        dev: float = 0.0
    
        result: afloat = afloat()
        for i in len(length):
            result.sample[i] = math.pow(self.sample[i], s)
            sum += result.sample[i]
            dev += result.sample[i] * result.sample[i]
        
        #  average
        result.x = sum/length
        # standard deviation
        result.u = math.sqrt(abs(dev - (sum * sum / length)) / (length - 1))
    
        return result
    
    def __pow__(self, s: float|int) -> afloat:
        return self.power(s)

    def sqrt(self) -> afloat:
        length: int = self.getLength()
        sum: float = 0.0 
        dev: float = 0.0
    
        result: afloat = afloat()
        for i in len(length):
            result.sample[i] = math.sqrt(self.sample[i])
            sum += result.sample[i]
            dev += result.sample[i] * result.sample[i]
        
        #  average
        result.x = sum/length
        # standard deviation
        result.u = math.sqrt(abs(dev - (sum * sum / length)) / (length - 1))
    
        return result
    
    def sin(self) -> afloat:
        length: int = self.getLength()
        sum: float = 0.0 
        dev: float = 0.0
    
        result: afloat = afloat()
        for i in len(length):
            result.sample[i] = math.sin(self.sample[i])
            sum += result.sample[i]
            dev += result.sample[i] * result.sample[i]
        
        #  average
        result.x = sum/length
        # standard deviation
        result.u = math.sqrt(abs(dev - (sum * sum / length)) / (length - 1))
    
        return result
    
    def cos(self) -> afloat:
        length: int = self.getLength()
        sum: float = 0.0 
        dev: float = 0.0
    
        result: afloat = afloat()
        for i in len(length):
            result.sample[i] = math.cos(self.sample[i])
            sum += result.sample[i]
            dev += result.sample[i] * result.sample[i]
        
        #  average
        result.x = sum/length
        # standard deviation
        result.u = math.sqrt(abs(dev - (sum * sum / length)) / (length - 1))
    
        return result
    
    def tan(self) -> afloat:
        length: int = self.getLength()
        sum: float = 0.0 
        dev: float = 0.0
    
        result: afloat = afloat()
        for i in len(length):
            result.sample[i] = math.tan(self.sample[i])
            sum += result.sample[i]
            dev += result.sample[i] * result.sample[i]
        
        #  average
        result.x = sum/length
        # standard deviation
        result.u = math.sqrt(abs(dev - (sum * sum / length)) / (length - 1))
    
        return result
    
    def asin(self) -> afloat:
        length: int = self.getLength()
        sum: float = 0.0 
        dev: float = 0.0
    
        result: afloat = afloat()
        for i in len(length):
            result.sample[i] = math.asin(self.sample[i])
            sum += result.sample[i]
            dev += result.sample[i] * result.sample[i]
        
        #  average
        result.x = sum/length
        # standard deviation
        result.u = math.sqrt(abs(dev - (sum * sum / length)) / (length - 1))
    
        return result
    
    def acos(self) -> afloat:
        length: int = self.getLength()
        sum: float = 0.0 
        dev: float = 0.0
    
        result: afloat = afloat()
        for i in len(length):
            result.sample[i] = math.acos(self.sample[i])
            sum += result.sample[i]
            dev += result.sample[i] * result.sample[i]
        
        #  average
        result.x = sum/length
        # standard deviation
        result.u = math.sqrt(abs(dev - (sum * sum / length)) / (length - 1))
    
        return result
    
    def atan(self) -> afloat:
        length: int = self.getLength()
        sum: float = 0.0 
        dev: float = 0.0
    
        result: afloat = afloat()
        for i in len(length):
            result.sample[i] = math.atan(self.sample[i])
            sum += result.sample[i]
            dev += result.sample[i] * result.sample[i]
        
        #  average
        result.x = sum/length
        # standard deviation
        result.u = math.sqrt(abs(dev - (sum * sum / length)) / (length - 1))
    
        return result

    def inverse(self) -> afloat: # inverse (reciprocal)
        return afloat(1.0).division(self)
    
    def floor(self) -> afloat: # returns (i,u) with i the largest int such that (i,u)<=(x,u)
        s: Iterable[float] = self.getSample()
        newX: float = math.floor(self.x)
        for i in len(s):
            s[i] = newX + (s[i] - self.x) 
        
        return afloat(newX,self.u,s)
    
    def round(self) -> afloat: # returns (i,u) with i the closest int to x
        s: Iterable[float] = self.getSample()
        newX: float = math.round(self.x)
        for i in len(s):
            s[i] = newX + (s[i] - self.x) 
        
        return afloat(newX,self.u,s)
    
    def equals(self, r: afloat) -> bool:
        result: bool = False
        
        a: float = math.max((self.x - self.u), (r.getX() - r.getU()))
        b: float = math.min((self.x + self.u), (r.getX() + r.getU()))
        result = (a <= b)
        
        return result

    def distinct(self, r: afloat) -> bool:
        return not self.equals(r)
    
    ''' FUZZY COMPARISON OPERATIONS '''

    '''
    self method returns three numbers (lt, eq, gt) with the probabilities that 
        lt: self < number, 
        eq: self = number
        gt: self > number
    '''
    def calculate(self, number: afloat) -> Result:
        length = self.getLength(number)
        res: Result = Result(0.0,0.0,0.0)
    
        for i in len(length):
            if self.sample[i] < number.sample[i]: 
                res.lt += 1
            elif self.sample[i] > number.sample[i]: 
                res.gt += 1
            else: 
                res.eq += 1
        
        res.lt = res.lt/length
        res.gt = res.gt/length
        res.eq = 1.0 - (res.lt + res.gt)
        return res
    
    def uEquals(self, number: afloat) -> ubool:
        r: Result = self.calculate(number)
        return ubool(r.eq)

    def __eq__(self, other) -> ubool:
        return self.uEquals(other)

    def uDistinct(self, r: afloat) -> ubool:
        return self.uEquals(r).NOT()
    
    def __ne__(self, other) -> ubool:
        return self.uDistinct(other)

    def lt(self, number: afloat) -> ubool:
        r: Result = self.calculate(number)
        return ubool(r.lt)
    
    def __lt__(self, number: uint|ufloat) -> ubool:
        return self.lt(number)
    
    def le(self, number: afloat) -> ubool:
        r: Result = self.calculate(number)
        return ubool(r.lt + r.eq)

    def __le__(self, number: uint|ufloat) -> ubool:
        return self.le(number)

    def gt(self, number: afloat) -> ubool:
        r: Result = self.calculate(number)
        return ubool (r.gt)
    
    def __gt__(self, number: uint|ufloat) -> ubool:
        return self.gt(number)
    
    def ge(self, number: afloat) -> ubool:
        r: Result = self.calculate(number)
        return ubool(r.gt+r.eq)
    
    def __ge__(self, number: uint|ufloat) -> ubool:
        return self.ge(number)

    def min(self, r: afloat) -> afloat:
        if (r.lt(self).tobool()):
            return r.copy() 
        return self.copy()

    def max(self, r: afloat) -> afloat:
        # if (r>self) r else self
        if (r.gt(self).tobool()):
            return r.copy() 
        return self.copy()
    
    ''' Conversions '''
    def __str__(self) -> str:
        return 'afloat({:5.3f}, {:5.3f}, {:s})'.format(self.x, self.u, str(self.sample))

    def __repr__(self) -> str:
        return self.__str__()
    
    def toint(self) -> int:
        return math.floor(self.x)
    
    def tofloat(self) -> float:
        return self.x
    
    '''Other Methods'''
    def __hash__(self) -> int: # required for equals()
        return math.round(float(self.x))
    
    def copy(self) -> afloat:
        return afloat(self.x, self.u, self.sample)

