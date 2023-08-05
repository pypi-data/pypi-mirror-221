from __future__ import annotations

import math
from enum import Enum
from functools import reduce

from uncertainty.utypes import ubool

class Domain(Enum): 
    NIL = 1; TRUE = 2; FALSE = 3; DOMAIN = 4

    def intersect(self, d: Domain) -> Domain:
        match self:
            case Domain.NIL: return Domain.NIL
            case Domain.TRUE:
                match d:
                    case Domain.FALSE: return Domain.NIL
                    case Domain.DOMAIN: return Domain.TRUE
                    case _: raise RuntimeError('unidentified domain')
            case Domain.FALSE:
                match d:
                    case Domain.TRUE: return Domain.NIL
                    case Domain.DOMAIN: return Domain.FALSE
                    case _: raise RuntimeError('unidentified domain')
            case Domain.DOMAIN: return d
            case _: raise RuntimeError('unidentified domain')
           
    def union(self, d: Domain) -> Domain:
        match self:
            case Domain.DOMAIN: return Domain.DOMAIN
            case Domain.TRUE:
                match d:
                    case Domain.NIL: return Domain.TRUE
                    case Domain.DOMAIN: return Domain.DOMAIN
                    case _: raise RuntimeError('unidentified domain')
            case Domain.FALSE:
                match d:
                    case Domain.NIL: return Domain.FALSE
                    case Domain.DOMAIN: return Domain.DOMAIN
                    case _: raise RuntimeError('unidentified domain')
            case Domain.NIL: return d
            case _: raise RuntimeError('unidentified domain')

class sbool:

    #b belief mass: degree of belief that self is True
    #d disbelief mass: degree of belief that self is False
    #u uncertainty mass: amount of uncommitted belief  
    #a base rate: prior probability of self being True
    #relativeWeight For fusion operations

    def __init__(self, b: bool|ubool|float|str = 1.0, d: float|str = 0.0, u: float|str = 0.0, 
                 a: float|str = 1.0, relativeWeight: float|str = 1.0) -> sbool:
        if isinstance(b, bool):
            self._createFromBool(b, relativeWeight)
        elif isinstance(b, ubool):
            self._createFromubool(b, relativeWeight)
        elif isinstance(b, sbool):
            self._createFromuopinion(b, relativeWeight)
        else:
            self._createFromFloats(b, d, u, a, relativeWeight)

    def adjust(self, value: float) -> float:
        return float(math.round(value * 1000000.0) / 1000000.0)

    def _createFromFloats(self, b: float|str = 1.0, d: float|str = 0.0, u: float|str = 0.0, 
                 a: float|str = 1.0, relativeWeight: float|str = 1.0) -> sbool:
        if abs(self.b+self.d+self.u-1.0)>0.001 or self.b<0.0 or \
            self.d<0.0 or self.u<0.0 or self.a<0.0 or self.b>1.0 or \
            self.d>1.0 or self.u>1.0 or self.a>1.0:
            raise ValueError('sbool constructor with relative weight: Invalid parameters. b:'+self.b+',d:'+self.d+',u:'+self.u+',a:'+self.a)

        self.b = self.adjust(float(b))
        self.d = self.adjust(float(d))
        self.u = self.adjust(float(u))
        self.a = self.adjust(float(a))
        self.relativeWeight = float(self.adjust(relativeWeight))

    def _createFromBool(self, b: bool, relativeWeight: float):
        if b: self.b = 1.0; self.d = 0.0; self.u = 0.0; self.a = 1.0 # Dogmatic True
        else: self.b = 0.0; self.d = 1.0; self.u = 0.0; self.a = 0.0 # Dogmatic False
        self.relativeWeight = relativeWeight

    def _createFromubool(self, b: ubool, relativeWeight: float): # type embedding -- without uncertainty
        self.b = self.adjust(b.c) 
        self.d = 1.0 - self.b 
        self.u = 0.0 
        self.a = self.b
        self.relativeWeight = relativeWeight

    def _createFromuopinion(self, b: sbool): # type embedding -- without uncertainty
        self.b = sbool.b
        self.d = sbool.d
        self.u = sbool.u
        self.a = sbool.a
        self.relativeWeight = sbool.relativeWeight

    ''' Dogmatic opinions are opinions with complete certainty (i.e., uncertainty = 0). '''
    def createDogmaticOpinion(projection: float, baseRate: float) -> sbool:
        if projection < 0.0 or projection > 1.0 or baseRate < 0.0 or baseRate > 1.0:
            raise ValueError('Create Dogmatic Opinion: Projections and baseRates should be between 0 and 1')
        
        return sbool(projection, 1.0 - projection, 0.0, baseRate)
	
    ''' Vacuous opinions have an uncertainty of 1. '''
    def createVacuousOpinion(projection: float) -> sbool:
        if projection < 0.0 or projection > 1.0:
            raise ValueError('CreateVacuousOpinion: Projection must be between 0 and 1. p=' + projection)
        return sbool(0.0, 0.0, 1.0, projection)	

    ''' getters (no def setters in order to respect well-formed rules) '''
    def belief(self) -> float:
        return self.b
    
    def disbelief(self) -> float:
        return self.d
    
    def uncertainty(self) -> float:
        return self.u
    
    def baseRate(self) -> float:
        return self.a
    
    @property
    def relativeWeight(self) -> float:
        return self._relativeWeight if self.isDogmatic() else 0.0
    
    @relativeWeight.setter
    def relativeWeight(self, relativeWeight: float):
        self._relativeWeight = self.adjust(relativeWeight)
    
    def getRelativeWeight(self, opinion: sbool) -> float:
           return self.adjust(self.relativeWeight / opinion.relativeWeight)

    '''  Auxiliary operationn '''
    def projection(self) -> float: # projected probability
        return self.adjust(self.b + self.a * self.u)
            
    def projectiveDistance(self, s: sbool) -> float: # projectiveDistance
        return self.adjust(abs(self.projection() - s.projection())) # /2

    def conjunctiveCertainty(self, s: sbool) -> float:
        return self.adjust((1.0 - self.u) * (1.0 - s.u))

    def degreeOfConflict(self, s: sbool) -> float:
        return self.adjust(self.projectiveDistance(s) * self.conjunctiveCertainty(s))
    
    def increasedUncertainty(self) -> sbool:
        if self.isVacuous():
            return self.clone()
        
        sqrt_u: float = math.sqrt(self.uncertainty())
        k: float = 1.0 - (sqrt_u - self.uncertainty()) / (self.belief() + self.disbelief())
        brBelief: float = self.belief() * k
        brUncertainty: float = sqrt_u
        brDisbelief: float = self.disbelief() * k
        return sbool(brBelief, brDisbelief, brUncertainty, self.baseRate())

    def isAbsolute(self) -> bool:
        return (self.belief() == 1.0) or (self.disbelief() == 1.0)

    def isVacuous(self) -> bool:
        return self.uncertainty() == 1.0

    def isCertain(self, threshold: float) -> bool:
        return not self.isUncertain(threshold)

    def isDogmatic(self) -> bool:
        return self.uncertainty() == 0.0

    def isMaximizedUncertainty(self) -> bool:
        return (self.disbelief() == 0.0) or (self.belief() == 0.0)

    def isUncertain(self, threshold: float) -> bool:
        return 1.0 - self.uncertainty() < threshold

    def uncertainOpinion(self) -> sbool:
        return self.uncertaintyMaximized()

    def certainty(self) -> float:
        if self.uncertainty() == 0.0:
            return 0.0
        return 1.0 - self.uncertainty()
    
    '''
	   Returns the subjective opinion that results from adjusting the base rate to be the one given in the
	   parameter. self operation is useful when we need to apply an opinion on a ubool value, whose
	   confidence will become the base rate of the resulting opinion. 
	   @param x ubool, whose confidence specifies the baseRate
	   @return A sbool value whose base rate is the one given in the parameter, the uncertainty is 
	   maintained, and the degree of belief is adjusted proportionally to the ratio (b/a) of the 
	   original sbool. If the base rate is the same, the sbool does not change. If the 
	   baseRate is 0 (False), the degree of belief of the sbool is 0 too, and the previous belief is 
	   transferred to the degree of disbelief.
    '''
    def applyOn(self, x: ubool) -> sbool:
        baseRate: float = x.c
        if baseRate < 0.0 or baseRate > 1.0:
            raise ValueError('applyOn(): baseRate must be between 0 and 1')
        
        if self.baseRate() == baseRate:
            return self.clone()
        
        uT: float = self.uncertainty()
        if uT==1.0:
            return sbool(0.0, 0.0, 1.0, baseRate) # we only change the base rate...
        
        bT: float = 0.0
        if self.baseRate() == 0.0: #then baseRate != 0.0
            bT  = self.belief() + self.disbelief() * baseRate #OK
        else:  #self.baseRate() != 0.0
            bT  = min(baseRate * self.belief() / self.baseRate(), (1.0 - uT))
        
        return sbool(bT, 1.0 - bT - uT, uT, baseRate)
		
    '''Type Operations '''
    def NOT(self) -> sbool:
        return sbool(self.d, self.b, self.u, 1.0-self.a, self.relativeWeight)
    
    def __invert__(self) -> sbool:
        return self.NOT()
    
    def AND(self, s: sbool) -> sbool: # assumes independent variables
        if self == s:
            return self.clone() # x and x = x
        
        b: float = self.b*s.b + (0.0 if self.a * s.a==1.0 else \
            ((1.0 - self.a) * s.a * self.b * s.u + self.a * (1.0 - s.a) * self.u * s.b) \
            / (1.0 - self.a * s.a))
        d: float = self.d + s.d - self.d * s.d
        return  sbool(b, 
                         d, 
                         1-d-b, 
                         self.a*s.a, 
                         self.getRelativeWeight() + s.getRelativeWeight()
        )

    def __and__(self, other) -> sbool:
        return self.AND(other)
    
    def __rand__(self, left) -> sbool:
        return sbool(left).AND(self)

    def OR(self, s: sbool) -> sbool:# assumes independent variables

        if self == s:
            return self.clone() # x or x
        
        b: float = self.b + s.b - self.b*s.b
        d: float = self.d*s.d + (0.0 if self.a + s.a == self.a*s.a else \
            (self.a*(1-s.a)*self.d*s.u+s.a*(1-self.a)*self.u*s.d)/(self.a + s.a - self.a*s.a))
        return sbool(
            b, 
            d, 
            1 - b - d, 
            self.a + s.a - self.a*s.a, 
            self.getRelativeWeight() + s.getRelativeWeight()
        )

    def __or__(self, other) -> sbool:
        return self.OR(other)

    def __ror__(self, left) -> sbool:
        return sbool(left).OR(self)
	
    def implies(self, s: sbool) -> sbool:
        return self.NOT().OR(s) # self is to be consistent with ubool, because in Subjective Logic self is not the case...
	
    def equivalent(self, s: sbool) -> sbool:
		# return self.implies(b).and(b.implies(self))
        return self.xor(s).NOT() 	
	
    def XOR(self, s: sbool) -> sbool:
        return sbool(
                abs(self.b - s.b), 
                1.0 - abs(self.b - s.b) - self.u*s.u,
                self.u*s.u,
                abs(self.a - s.a), 
                self.getRelativeWeight() + s.getRelativeWeight()
        )

    def __xor__(self, other) -> sbool:
        return self.XOR(other)
    
    def __rxor__(self, left) -> sbool:
        return sbool(left).XOR(self)
	
    def uncertaintyMaximized(self) -> sbool: # Returns the equivalent sbool with maximum uncertainty. 
            # The dual operation is toubool, which returns the equivalent sbool, with u==0
        #return self.increasedUncertainty()
        # Replaced by another version
        
        p: float = self.projection()
        # Extreme cases
        if self.a == 1.0 and p == 1.0:
            return sbool(0.0,0.0,1.0,self.a,self.getRelativeWeight())
        if self.a == 1.0 and self.u == 1.0:
            return sbool(0.0,0.0,1.0,self.a,self.getRelativeWeight())
        if self.a == 0.0 and self.b==0.0:
            return sbool(0.0,0.0,1.0,self.a,self.getRelativeWeight())
        # Normal cases
        if p < self.a:
            return sbool(0.0, 1.0 - (p/self.a), p/self.a, self.a,self.getRelativeWeight())
        return sbool((p - self.a) / (1.0 - self.a), 0.0, (1.0 - p)/ (1.0 - self.a), self.a,self.getRelativeWeight())	
		
    def deduceY(self, yGivenX: sbool, yGivenNotX: sbool) -> sbool: # DEDUCTION: returns Y, acting 'self' as X
        y: sbool = sbool()
        px: float = self.projection()
        K: float = 0.0
        y.a: float = yGivenX.a if yGivenX.u+yGivenNotX.u >= 2.0 else (self.a*yGivenX.b+(1.0-self.a)*yGivenNotX.b)/(1.0-self.a*yGivenX.u-(1.0-self.a)*yGivenNotX.u)
        pyxhat: float = yGivenX.b*self.a + yGivenNotX.b*(1-self.a)+ y.a*(yGivenX.u*self.a+yGivenNotX.u*(1-self.a))
        bIy: float = self.b*yGivenX.b+self.d*yGivenNotX.b+self.u*(yGivenX.b*self.a+yGivenNotX.b*(1.0-self.a))
        dIy: float = self.b*yGivenX.d+self.d*yGivenNotX.d+self.u*(yGivenX.d*self.a+yGivenNotX.d*(1.0-self.a))
        uIy: float = self.b*yGivenX.u+self.d*yGivenNotX.u+self.u*(yGivenX.u*self.a+yGivenNotX.u*(1.0-self.a))
        # case I
        #if (((yGivenX.b>yGivenNotX.b)and(yGivenX.d>yGivenNotX.d))or((yGivenX.b<=yGivenNotX.b)and(yGivenX.d<=yGivenNotX.d))) 
        K = 0.0

        # case II.A.1
        if (yGivenX.b>yGivenNotX.b)and(yGivenX.d<=yGivenNotX.d) and \
                (pyxhat <= (yGivenNotX.b+y.a*(1.0-yGivenNotX.b-yGivenX.d))) and \
                (px<=self.a):
            K=(self.a*self.u*(bIy-yGivenNotX.b))/((self.b+self.a*self.u)*y.a)
        # case II.A.2
        if (yGivenX.b>yGivenNotX.b)and(yGivenX.d<=yGivenNotX.d) and \
                (pyxhat <= (yGivenNotX.b+y.a*(1.0-yGivenNotX.b-yGivenX.d))) and \
                (px>self.a):
            K=(self.a*self.u*(dIy-yGivenX.d)*(yGivenX.b-yGivenNotX.b))/((self.d+(1.0-self.a)*self.u)*y.a*(yGivenNotX.d-yGivenX.d))
        # case II.B.1
        if (yGivenX.b>yGivenNotX.b)and(yGivenX.d<=yGivenNotX.d) and \
                (pyxhat > (yGivenNotX.b+y.a*(1.0-yGivenNotX.b-yGivenX.d))) and \
                (px<=self.a):
            K=((1.0-self.a)*self.u*(bIy-yGivenNotX.b)*(yGivenNotX.d-yGivenX.d))/((self.b+self.a*self.u)*(1.0-y.a)*(yGivenX.b-yGivenNotX.b))
        # case II.B.2
        if (yGivenX.b>yGivenNotX.b)and(yGivenX.d<=yGivenNotX.d) and \
                (pyxhat > (yGivenNotX.b+y.a*(1.0-yGivenNotX.b-yGivenX.d))) and \
                (px>self.a):
            K=((1.0-self.a)*self.u*(dIy-yGivenX.d))/((self.d+(1.0-self.a)*self.u)*(1.0-y.a))

        # case III.A.1
        if (yGivenX.b<=yGivenNotX.b)and(yGivenX.d>yGivenNotX.d) and \
                (pyxhat <= (yGivenX.b+y.a*(1.0-yGivenNotX.b-yGivenX.d))) and \
                (px<=self.a):
            K=((1.0-self.a)*self.u*(dIy-yGivenNotX.d)*(yGivenNotX.b-yGivenX.b))/((self.b+self.a*self.u)*y.a*(yGivenX.d-yGivenNotX.d))
        
        # case III.A.2
        if (yGivenX.b<=yGivenNotX.b)and(yGivenX.d>yGivenNotX.d) and \
                (pyxhat <= (yGivenX.b+y.a*(1.0-yGivenX.b-yGivenNotX.d))) and \
                (px>self.a):
            K=((1.0-self.a)*self.u*(bIy-yGivenX.d))/((self.d+(1.0-self.a)*self.u)*y.a)

        # case III.B.1
        if (yGivenX.b<=yGivenNotX.b)and(yGivenX.d>yGivenNotX.d) and \
                (pyxhat > (yGivenX.b+y.a*(1.0-yGivenX.b-yGivenNotX.d))) and \
                (px<=self.a):
            K=(self.a*self.u*(dIy-yGivenNotX.b))/((self.b+self.a*self.u)*(1.0-y.a))

        # case III.B.2
        if (yGivenX.b<=yGivenNotX.b)and(yGivenX.d>yGivenNotX.d) and \
                (pyxhat > (yGivenX.b+y.a*(1.0-yGivenX.b-yGivenNotX.d))) and \
                (px>self.a):
            K=(self.a*self.u*(bIy-yGivenX.b)*(yGivenX.d-yGivenNotX.d))/((self.d+(1.0-self.a)*self.u)*(1.0-y.a)*(yGivenNotX.b-yGivenX.b))
        
        y.b = self.adjust(bIy - y.a*K)
        y.d = self.adjust(dIy - (1.0-y.a)*K)
        y.u = self.adjust(uIy + K)
        y.setRelativeWeight(yGivenX.getRelativeWeight() + yGivenNotX.getRelativeWeight())

        return y
	

    ''' UNION AND WEIGHTED UNION OPERATIONS '''
    '''
        self method implements Union of two opinions, according to Josang's book (Section 6.1)
        return a sbool that represents the union of the two opinions (self + s).
    '''
    def union(self, s: sbool) -> sbool:
        if s == None or self.a + s.a >1.0 or self.b+s.b > 1.0:
            raise ValueError('union: invalid argument')

        return sbool(
            self.b + s.b, 
            (self.a * (self.d - s.b) + s.a * (s.d - self.b)) / (self.a + s.a),
            self.a * self.u + s.a * s.u,
            self.a + s.a, 
            self.getRelativeWeight() + s.getRelativeWeight()
		)
	
    '''
        self method implements the Weighted Union of a collection of opinions. 
        Note that the weighted union of two operations is different from their union. 
        return a sbool that represents the weigthed union, assuming the same weight for all opinions.
    '''    
    def weightedUnion(opinions: list[sbool]) -> sbool:
        if None in opinions or len(opinions) < 2:
            raise ValueError('weightedUnion: Cannot make the union of None opinions, or only one opinion was passed')
        b: float = 0.0
        a: float = 0.0
        u: float = 0.0
        n: int = len(opinions)
        for so in opinions:
            b+=so.b
            a+=so.a
            u+=so.a*so.u
        
        return sbool(b/n,1-b/n-u/a,u/a,a/n)
    
 
    ''' Binary ver ''' 
    def weightedUnion(self, opinion: sbool) -> sbool: #consensus and compromise fusion
       return self.consensusAndCompromiseFusion([self, opinion])

	
    '''
	    FUSION OPERATIONS 
	        These implementations are based in those given in https:#github.com/vs-uulm/subjective-logic-java
    '''
    '''
	    self method implements constraint belief fusion (CBF). It uses the binary operation and iterates 
	    over the collection of opinions. self operation is associative if the base rate is the same for all 
        opinions, otherwise the fused base rate distribution could be the confidence-weighted
	    average base rate (see Josang's book). The neutral element is the vacuous opinion.
        return a sbool that represents the fused evidence.
    '''
    def beliefConstraintFusion(opinions: list[sbool]) -> sbool:
        if None in opinions or opinions.size() < 2:
            raise ValueError('BCF: Cannot fuse None opinions, or only one opinion was passed')
        bcf: sbool = None
        
        for so in opinions:
            if bcf == None:
                bcf = so # first time
            else:
                bcf = bcf.bcFusion(so)
        
        return bcf
    
    '''
        self method implements MIN fusion. self takes the minimum, i.e., returns the opinion with 
        the lowest probability of being True, meaning the lowest projected probability P(X=x).
        return a sbool that represents the fused evidence.
    '''
    def minimumBeliefFusion(opinions: list[sbool]) -> sbool:
        if None in opinions or opinions.size() < 2:
            raise ValueError('MBF: Cannot fuse None opinions, or only one opinion was passed')

        min: sbool = None
        for so in opinions:
            if min == None:
                min = so
            min = min.min(so)
        
        return min.copy()

    '''
        self method implements MAJORITY fusion. self returns a dogmatic opinion that specifies the 
        decision of the majority.
        If the majority is tied, a vacuous opinion is returned.
        It is assumed that the base rates of all opinions are equal.
        For self operation, opinions that are undecided (projections equals base rate) are ignored.
        return a sbool that represents the fused evidence.
    '''

    def majorityBeliefFusion(opinions: list[sbool]) -> sbool:
        if None in opinions or opinions.size() < 2:
            raise ValueError('MajBF: Cannot fuse None opinions, or only one opinion was passed')
        pos: int = 0
        neg: int = 0

        for so in opinions:
            if so.projection() < so.a:
                neg+= 1
            elif so.projection() > so.a:
                pos+= 1
        
        if pos > neg: return sbool(1.0, 0, 0, 0.5) 		# True
        elif pos < neg: return sbool(0, 1.0, 0, 0.5) 	# False
        else: return sbool(0, 0, 1.0, 0.5) 				# uncertain
    
    
    ''' self method implements AVERAGE fusion.
        return a sbool that represents the fused evidence.
    '''
    def averageBeliefFusion(opinions: list[sbool]) -> sbool:
	   
        #implemented using equation (32) of https:#folk.uio.no/josang/papers/JWZ2017-FUSION.pdf 
        # because the Josang's book has a problem.

        if opinions == None or None in opinions or not opinions:
            raise ValueError('AVF: Cannot average None opinions')

        b: float = 0.0; u: float=0.0; a: float = 0.0
        PU: float = 1.0 #product of all uncertainties
        count: int = 0

        oBelief: float; oAtomicity: float; oUncertainty: float; oDisbelief: float

        for o in opinions:
            PU *= o.uncertainty() # product of all uncertainties

        # case I: all opinions with uncertainty > 0:
        if PU != 0.0:
            for o in opinions:
                u += PU/o.uncertainty()
                b += o.belief() * PU/o.uncertainty()
                a += o.baseRate()
            oBelief = b / u
            oAtomicity = a / opinions.size()
            oUncertainty = opinions.size() * PU / u
            oDisbelief = 1.0 - oBelief - oUncertainty
            return sbool(oBelief, oDisbelief, oUncertainty, oAtomicity)

        else: # there is at least one opinion with uncertainty = 0. Then we only consider these opinions
            for o in opinions:
                if o.uncertainty() == 0.0:
                    b += o.belief()
                    a += o.baseRate()
                    count+= 1  
            oBelief = b / count
            oAtomicity = a / count
            oUncertainty = 0.0
            oDisbelief = 1.0 - oBelief - oUncertainty
            return sbool(oBelief, oDisbelief, oUncertainty, oAtomicity)

    def productOfUncertainties(opinions: list[sbool]) -> float:
        return reduce(lambda acc, u : acc * u, map(lambda x : x.uncertainty(), opinions), 1.0)

    '''
     self method implements cumulative belief fusion (CBF) for multiple sources, as discussed in the corrected
     version of <a href='https:#folk.uio.no/josang/papers/JWZ2017-FUSION.pdf'>a FUSION 2017 paper by Josang et al.</a>
    
     As discussed in the book, cumulative fusion is useful in scenarios where opinions from multiple sources 
     are combined, where each source is relying on independent (in the statistical sense) evidence.
     
     
       return a sbool that represents the fused evidence based on evidence accumulation.
    '''
    def cumulativeBeliefFusion(opinions: list[sbool]) -> sbool:
        #handle edge cases
        if opinions == None or None in opinions or not opinions:
            raise ValueError('aCBF: Cannot average None opinions')

        if len(opinions) == 1:
            return opinions.iterator().next().clone()
        

        #fusion as defined by Josang
        resultBelief: float; resultDisbelief: float; resultUncertainty: float; resultRelativeWeight: float = 0.0; resultAtomicity: float = -1.0

        dogmatic: list[sbool]= []
        first: bool = True

        for o in opinions:
            if first:
                resultAtomicity = o.baseRate()
                first = False
            #dogmatic iff uncertainty is zero.
            elif o.uncertainty() == 0.0:
                dogmatic.append(o)

        if not dogmatic:
            #there are no dogmatic opinions -- case I/Eq16 of 10.23919/ICIF.2017.8009820
            productOfUncertainties: float = productOfUncertainties(opinions)
            numerator: float = 0.0
            beliefAccumulator: float = 0.0
            disbeliefAccumulator: float = 0.0

            #self computes the top and bottom sums in Eq16, but ignores the - (N-1) * productOfUncertainties in the numerator (see below)
            for o in opinions:
                #productWithoutO = product of uncertainties without o's uncertainty
                #self can be rewritten:
                #prod {C_j != C  u^{C_j = (u^C)^-1 * prod{C_j u^{C_j = 1/(u^C) * prod{C_j u^{C_j
                #so instead of n-1 multiplications, we only need a division
                productWithoutO: float = productOfUncertainties / o.uncertainty()
                beliefAccumulator = beliefAccumulator + productWithoutO * o.belief()
                disbeliefAccumulator = disbeliefAccumulator + productWithoutO * o.disbelief()
                numerator = numerator + productWithoutO

            #self completes the numerator:
            numerator = numerator - (opinions.size() - 1) * productOfUncertainties
            resultBelief = beliefAccumulator / numerator
            resultDisbelief = disbeliefAccumulator / numerator
            resultUncertainty = productOfUncertainties / numerator
            resultRelativeWeight = 0.0
        else:
            #at least 1 dogmatic opinion
            #note: self computation assumes that the relative weight represents how many opinions have been fused into that opinion.
            #for a normal multi-source fusion operation, self should be 1, in which case the gamma's in Eq17 are 1/N as noted in the text (i.e., all opinions count equally)
            #however, self formulation also allows partial fusion beforehand, by 'remembering' the amount of dogmatic (!) opinions in o.relativeWeight.
            totalWeight: float = math.fsum(map(lambda o : o.getRelativeWeight(), dogmatic))
            resultBelief: float =  math.fsum(map(lambda o : o.getRelativeWeight()/totalWeight * (o).belief(), dogmatic))
            resultDisbelief: float = math.fsum(map(lambda o : o.getRelativeWeight()/totalWeight * (o).disbelief(), dogmatic))
            resultUncertainty: float = 0.0
            resultRelativeWeight: float = totalWeight

        return sbool(resultBelief, resultDisbelief, resultUncertainty, resultAtomicity,resultRelativeWeight)

    '''
        self method implements epistemic cumulative belief fusion (eCBF) for multiple sources, 
        as discussed in the corrected
        version of <a href='https:#folk.uio.no/josang/papers/JWZ2017-FUSION.pdf'>a FUSION 2017 paper by Josang et al.</a>

        eCBF is useful when the opinions represent knowledge, and not observations, and therefore they are
        uncertainty maximized. As in the CBF, each source is supposed to be relying on independent 
        (in the statistical sense) evidence (in self case, knowledge).
        return a sbool that represents the fused evidence based on evidence accumulation.
    '''
    def epistemicCumulativeBeliefFusion(opinions: list[sbool]) -> sbool:
        #handle edge cases
        if opinions == None or None in opinions or not opinions:
            raise ValueError('eCBF: Cannot average None opinions')

        if opinions.size() == 1:
            return opinions.iterator().next().clone()

        #fusion as defined by Josang
        resultBelief: float; resultDisbelief: float; resultUncertainty: float; resultRelativeWeight: float = 0.0; resultAtomicity: float = -1.0

        dogmatic: list[sbool] = []
        first: bool = True
        for o in opinions:
            if first:
                resultAtomicity = o.baseRate()
                first = False
            
            #dogmatic iff uncertainty is zero.
            if o.uncertainty() == 0.0:
                dogmatic.append(o)
        
        if not dogmatic:
            #there are no dogmatic opinions -- case I/Eq16 of 10.23919/ICIF.2017.8009820
            uncertainties: float = map(lambda o : o.uncertainty(), opinions)
            productOfUncertainties: float = productOfUncertainties(opinions)
            numerator: float = 0.0
            beliefAccumulator: float = 0.0
            disbeliefAccumulator: float = 0.0

            #self computes the top and bottom sums in Eq16, but ignores the - (N-1) * productOfUncertainties in the numerator (see below)
            for o in opinions:
                #productWithoutO = product of uncertainties without o's uncertainty
                #self can be rewritten:
                #prod {C_j != C  u^{C_j = (u^C)^-1 * prod{C_j u^{C_j = 1/(u^C) * prod{C_j u^{C_j
                #so instead of n-1 multiplications, we only need a division
                productWithoutO: float = productOfUncertainties / o.uncertainty()
                beliefAccumulator = beliefAccumulator + productWithoutO * o.belief()
                disbeliefAccumulator = disbeliefAccumulator + productWithoutO * o.disbelief()
                numerator = numerator + productWithoutO
            
            #self completes the numerator:
            numerator = numerator - (opinions.size() - 1) * productOfUncertainties
            resultBelief = beliefAccumulator / numerator
            resultDisbelief = disbeliefAccumulator / numerator
            resultUncertainty = productOfUncertainties / numerator
            resultRelativeWeight = 0.0
        else:
            #at least 1 dogmatic opinion
            #note: self computation assumes that the relative weight represents how many opinions have been fused into that opinion.
            #for a normal multi-source fusion operation, self should be 1, in which case the gamma's in Eq17 are 1/N as noted in the text (i.e., all opinions count equally)
            #however, self formulation also allows partial fusion beforehand, by 'remembering' the amount of dogmatic (!) opinions in o.relativeWeight.
            totalWeight: float = math.fsum(map(lambda o : o.getRelativeWeight(), dogmatic))
            resultBelief: float =  math.fsum(map(lambda o : o.getRelativeWeight()/totalWeight * (o).belief(), dogmatic))
            resultDisbelief: float = math.fsum(map(lambda o : o.getRelativeWeight()/totalWeight * (o).disbelief(), dogmatic))
            resultUncertainty = 0.0
            resultRelativeWeight = totalWeight

        result: sbool = sbool(resultBelief, resultDisbelief, resultUncertainty, resultAtomicity,resultRelativeWeight)
        return result.uncertaintyMaximized()


    '''
        self method implements weighted belief fusion (WBF) for multiple sources, as discussed in a FUSION 2018 paper by van der Heijden et al.
        
        As discussed in the book, WBF is intended to represent the confidence-weighted averaging of evidence.
        Similar to AverageBF, it is useful when dependence between sources is assumed. However, WBF introduces 
        additional weights to increase the significance of sources that possess high certainty. 
        
        return a SubjectiveOpinion that represents the fused evidence based on confidence-weighted averaging of evidence.
    '''
    def weightedBeliefFusion(opinions: sbool) -> sbool:
        if opinions == None or None in opinions or not opinions:
            raise ValueError('WBF: Cannot average None opinions')

        if opinions.size() == 1:
            return opinions.iterator().next().clone()

        resultBelief: float = 0.0
        resultDisbelief: float = 0.0
        resultUncertainty: float = 0.0
        resultRelativeWeight: float = 0.0
        resultAtomicity: float = 0.0

        dogmatic: list[sbool] = []
        for o in opinions:
            #dogmatic iff uncertainty is zero.
            if o.uncertainty() == 0:
                dogmatic.append(o)

        if not dogmatic and any([o.certainty() > 0 for o in opinions]):
            #Case 1: no dogmatic opinions, at least one non-vacuous opinion
            productOfUncertainties: float = productOfUncertainties(opinions)
            sumOfUncertainties: float = math.fsum(map(lambda o : o.uncertainty(), opinions))

            numerator: float = 0.0
            beliefAccumulator: float = 0.0
            disbeliefAccumulator: float = 0.0
            atomicityAccumulator: float = 0.0

            for o in opinions:
                #prod = product of uncertainties without o's uncertainty
                prod: float = productOfUncertainties / o.uncertainty()

                #recall certainty = 1 - uncertainty
                beliefAccumulator = beliefAccumulator + prod * o.belief() * o.certainty()
                disbeliefAccumulator = disbeliefAccumulator + prod * o.disbelief() * o.certainty()
                atomicityAccumulator = atomicityAccumulator + o.baseRate() * o.certainty()
                numerator = numerator + prod
            

            numerator = numerator - opinions.size() * productOfUncertainties

            resultBelief = beliefAccumulator / numerator
            resultDisbelief = disbeliefAccumulator / numerator
            resultUncertainty = (opinions.size() - sumOfUncertainties) * productOfUncertainties / numerator
            resultAtomicity = atomicityAccumulator / (opinions.size() - sumOfUncertainties)
        elif all([o.uncertainty() == 1 for o in opinions]):
            #Case 3 -- everything is vacuous
            resultBelief = 0.0
            resultDisbelief = 0.0
            resultUncertainty = 1.0

            #all confidences are zero, so the weight for each opinion is the same -> use a plain average for the resultAtomicity
            resultAtomicity: float = 0.0
            first: bool = True
            for o in opinions:
                if first:
                    resultAtomicity = resultAtomicity + o.baseRate()
                    first = False
                
            resultAtomicity = resultAtomicity / float(len(opinions))

        else:
            #Case 2 -- dogmatic opinions are involved
            totalWeight: float = math.fsum(map(lambda o : o.getRelativeWeight(), dogmatic))
            resultBelief: float =  math.fsum(map(lambda o : o.getRelativeWeight()/totalWeight * (o).belief(), dogmatic))
            resultDisbelief: float = math.fsum(map(lambda o : o.getRelativeWeight()/totalWeight * (o).disbelief(), dogmatic))
            resultUncertainty = 0.0
            resultRelativeWeight = totalWeight

            #note: the for loop below will always set resultAtomicity correctly.
            resultAtomicity = -1
            first: bool = True
            for o in opinions:
                if first:
                    resultAtomicity = o.baseRate()
                    first = False

        return sbool(resultBelief, resultDisbelief, resultUncertainty, resultAtomicity,resultRelativeWeight)
   
    '''
        self method implements consensus & compromise fusion (CCF) for multiple sources, as discussed in a FUSION 2018 paper by van der Heijden et al.
        For more details, refer to Chapter 12 of the Subjective Logic book by Josang, specifically Section 12.6, which defines CC fusion for the case of two sources.
    
        return a sbool that represents the fused evidence.
    '''
    def consensusAndCompromiseFusion(opinions: list[sbool]) -> sbool:
        if opinions == None or None in opinions or len(opinions) < 2:
            raise ValueError('CCF: Cannot fuse None opinions, or only one opinion was passed')

        baseRate: float = -1
        first: bool = True
        for so in opinions:
            if first:
                baseRate = so.baseRate()
                first = False
            elif baseRate != so.baseRate():
                raise ValueError('CCF: Base rates for CC Fusion must be the same')
    
        #Step 1: consensus phase
        consensusBelief: float = float(min(map(lambda o : o.belief(), opinions)))
        consensusDisbelief: float = float(min(map(lambda o : o.disbelief(), opinions)))
        consensusMass: float = consensusBelief + consensusDisbelief

        residueBeliefs: list[float] = []
        residueDisbeliefs: list[float] = []
        uncertainties: list[float] = []
        for so in opinions:
            #note: self max should not be necessary..
            residueBeliefs.append(max(so.belief() - consensusBelief, 0))
            residueDisbeliefs.append(max(so.disbelief() - consensusDisbelief, 0))
            uncertainties.append(so.uncertainty())

        #Step 2: Compromise phase
        productOfUncertainties: float = productOfUncertainties(opinions)

        compromiseBeliefAccumulator: float = 0
        compromiseDisbeliefAccumulator: float = 0
        compromiseXAccumulator: float = 0 #self is what will later become uncertainty

        #self computation consists of 4 sub-sums that will be added independently.
        for i in range(len(opinions)):
            bResI: float = residueBeliefs[i]
            dResI: float = residueDisbeliefs[i]
            uI: float = uncertainties[i]
            # uWithoutI: float = productOfUncertainties / uI
            uWithoutI: float = productOfUncertainties / uI if uI != 0.0 else 0.0 

            #sub-sum 1:
            compromiseBeliefAccumulator = compromiseBeliefAccumulator + bResI * uWithoutI
            compromiseDisbeliefAccumulator = compromiseDisbeliefAccumulator + dResI * uWithoutI
            #note: compromiseXAccumulator is unchanged, since b^{ResI_X() of the entire domain is 0

        #sub-sums 2,3,4 are all related to different permutations of possible values
        for permutation in (len(opinions)):
            intersection: Domain = reduce(lambda acc, p : acc.intersect(p), permutation, Domain.DOMAIN)
            union: Domain = reduce(lambda acc, p : acc.union(p), permutation, Domain.NIL)

            #sub-sum 2: intersection of elements in permutation is x
            if intersection == Domain.TRUE:
                # --> add to belief
                prod: float = 1
                if Domain.DOMAIN in permutation:
                    prod = 0
                else:
                    for j in len(permutation):
                        match permutation[j]:
                            case Domain.DOMAIN:
                                prod = 0 # multiplication by 0
                            case True:
                                prod = prod * residueBeliefs[j] * 1
                compromiseBeliefAccumulator = compromiseBeliefAccumulator + prod
            elif intersection == Domain.FALSE:
                # --> add to disbelief
                prod: float = 1
                if Domain.DOMAIN in permutation:
                    prod = 0
                else:
                    for j in len(permutation):
                        match permutation[j]:
                            case Domain.DOMAIN:
                                prod = 0 # multiplication by 0
                            case False:
                                prod = prod * residueDisbeliefs[j] * 1
                        
                compromiseDisbeliefAccumulator = compromiseDisbeliefAccumulator + prod
            

            match union:
                case Domain.DOMAIN:
                    if not intersection == Domain.NIL:
                        pass
                        #sub-sum 3: union of elements in permutation is x, and intersection of elements in permutation is not NIL

                        #Note: self is always zero for binary domains, as explained by the following:
                        #prod: float = 1
                        #for (j: int=0 j<permutation.size() j++) {
                        #    switch (permutation[j]) {
                        #        case NIL:
                        #        case DOMAIN:
                        #            prod = 0 #because residue belief over NIL/DOMAIN is zero here
                        #        case True:
                        #        case False:
                        #            prod = 0 #because 1-a(y|x) is zero here, since a(y|x)=1 when x=y, and self must occur, since a(x|!x) occurring implies the intersection is NIL
                        #    
                        #            
                    else:
                        #sub-sum 4: union of elements in permutation is x, and intersection of elements in permutation is NIL
                        prod: float = 1
                        for j in len(permutation):
                            match permutation[j]:
                                case Domain.DOMAIN:
                                    prod = 0 #because residue belief over NIL/DOMAIN is zero here
                                case True:
                                    prod = prod * residueBeliefs[j]
                                case False:
                                    prod = prod * residueDisbeliefs[j]                          
                        compromiseXAccumulator = compromiseXAccumulator + prod
                case Domain.NIL:
                    #union of NIL means we have nothing to add
                    #sub-sum 3: union of elements in permutation is x, and intersection of elements in permutation is not NIL
                    #sub-sum 4: union of elements in permutation is x, and intersection of elements in permutation is NIL
                    pass
                case True:
                    #sub-sum 3: self is always zero for True and False, since 1-a(y_i|y_j)=0 in binary domains, where the relative base rate is either 1 if the union is x

                    #sub-sum 4: union of elements in permutation is x, and intersection of elements in permutation is NIL
                    if intersection == Domain.NIL:
                        #union is True, intersection is nil --> compute the product
                        prod: float = 1
                        for j in len(permutation):
                            match permutation[j]: #other cases will not occur
                                case True:
                                    prod = prod * residueBeliefs[j]
                                case False:
                                    prod = prod * residueDisbeliefs[j]
                                case Domain.NIL:
                                    prod = 0
                                case _:
                                    raise RuntimeError()
                            
                        
                        compromiseBeliefAccumulator = compromiseBeliefAccumulator + prod
                    
                    break
                case False:
                    #sub-sum 3: self is always zero for True and False, since 1-a(y_i|y_j)=0 in binary domains, where the relative base rate is either 1 if the union is x
                    #sub-sum 4: union of elements in permutation is x, and intersection of elements in permutation is NIL
                    if intersection.equals(Domain.NIL):
                        #union is True, intersection is nil --> compute the product
                        prod: float = 1
                        for j in len(permutation):
                            match permutation[j]: #other cases will not occur
                                case True:
                                    prod = prod * residueBeliefs[j]
                                case False:
                                    prod = prod * residueDisbeliefs[j]
                                case Domain.NIL:
                                    prod = 0
                                case _:
                                    raise RuntimeError()
                        compromiseDisbeliefAccumulator= compromiseDisbeliefAccumulator + prod

        compromiseBelief: float = compromiseBeliefAccumulator
        compromiseDisbelief: float = compromiseDisbeliefAccumulator
        compromiseUncertainty: float = compromiseXAccumulator
        preliminaryUncertainty: float = productOfUncertainties
        compromiseMass: float = compromiseBelief + compromiseDisbelief + compromiseUncertainty

        #Step 3: Normalization phase
        normalizationFactor: float = (1-consensusMass-preliminaryUncertainty)/(compromiseMass) if compromiseMass != 0.0 else 1.0
        fusedBelief: float = consensusBelief + normalizationFactor * compromiseBelief
        fusedDisbelief: float = consensusDisbelief + normalizationFactor * compromiseDisbelief
        fusedUncertainty: float = 1.0 - fusedBelief - fusedDisbelief

        return sbool(fusedBelief, fusedDisbelief, fusedUncertainty, baseRate)

    def tabulateOptions(size: int) -> list[Domain]:
        result = set()

        if size == 1:
            for item in Domain:
                result.append([item.value])
        else:
            for tuple in sbool.tabulateOptions(size - 1):
                for item in Domain:
                    result.append([item.value])

        return result
   
    ''' BINARY VERSIONS OF FUSING OPERATIONS '''

    def bcFusion(self, opinion: sbool) -> sbool: #belief constraint fusion
        #implemented using equation 12.2 of Josang's book
        harmony: float = self.belief() * opinion.uncertainty() + self.uncertainty() * opinion.belief() + self.belief() *opinion.belief()
        conflict: float = self.belief() * opinion.disbelief() + self.disbelief() * opinion.belief() #self.degreeOfConflict(opinion)# 0.0 # binomial opinions 
        if conflict == 1.0:
            raise ValueError('BCF: Cannot fuse totally conflicting opinions')
        
        b: float = harmony/(1.0-conflict)
        u: float = (self.uncertainty() * opinion.uncertainty()) / (1.0-conflict) 
        a: float = (self.baseRate() + opinion.baseRate()) / 2.0 if (self.uncertainty() + opinion.uncertainty() == 2.0) \
                    else (self.baseRate() * (1.0 - self.uncertainty()) + opinion.baseRate() * (1.0-opinion.uncertainty())) \
                        / (2-self.uncertainty()-opinion.uncertainty())
        return sbool(b, 1.0 - b - u, u, a)
        
    def ccFusion(self, opinion: sbool) -> sbool: #consensus and compromise fusion
        return self.consensusAndCompromiseFusion([self,opinion])

    def cumulativeFusion(self, opinion: sbool) -> sbool:
        return self.cumulativeBeliefFusion([self,opinion])

    def epistemicCumulativeFusion(self, opinion: sbool) -> sbool:
        return self.epistemicCumulativeBeliefFusion([self,opinion])

    def weightedFusion(self, opinion: sbool) -> sbool:
        return self.weightedBeliefFusion([self,opinion])

    def minimumFusion(self, opinion: sbool) -> sbool:
        return self.minimumBeliefFusion([self,opinion])

    def majorityFusion(self, opinion: sbool) -> sbool:
        return self.majorityBeliefFusion([self,opinion])

    def averageFusion(self, opinion: sbool) -> sbool:
        return self.averageBeliefFusion([self,opinion])
   
   
    ''' DISCOUNTING OPERATIONS '''
   
    ''' Binary versions '''
    '''
        self method implements the 'probability-sensitive trust discounting operator', 
        which causes the uncertainty in A's derived opinion about X to increase as a 
        function of the projected distrust in the source/advisor B. 
    
        For more details, refer to Chapter 14 of the Subjective Logic book by Josang, 
        specifically Section 14.3.2 that defines Trust Discounting with Two-Edge Paths.
    
        we assume that 'self' represents the opinion (functional trust) of an agent B 
        on statement X, i.e., [B:X]
        
        return a sbool that represents the opinion of A about X, [A:X]=[AB]x[B:X]
    '''
    def discount(self, atrustOnB: sbool) -> sbool:
        if atrustOnB == None:
            raise ValueError('Discountion operator parameter cannot be None')

        # self IS THE DISCOUNT OPERATOR DEFINED IN THE JOSANG 2016 BOOK 
        p: float = atrustOnB.projection()
        b: float = p * self.belief()
        d: float = p * self.disbelief()
        u: float = 1 - p * (self.disbelief() + self.belief())
        a: float = self.baseRate()
        return sbool(b,d,u,a)


    '''
        self method implements the discounting operator from the Trustyfeer 2018 
        paper bu Kurdi et al., which uses the belief() of the trust of A on B, instead of 
        the projection() of the trust of A on B, that was originally used by Josang. 
     
        Heba Kurdi, Bushra Alshayban, Lina Altoaimy, and Shada Alsalamah
        'TrustyFeer: A Subjective Logic Trust Model for Smart City Peer-to-Peer Federated Clouds'
        Wireless Communications and Mobile Computing, Volume 2018, Article ID 1073216, 13 pages
        https:#doi.org/10.1155/2018/1073216
     
        We assume that 'self' represents the opinion (functional trust) of an agent B 
        on statement X, i.e., [B:X]
    
        return a sbool that represents the opinion of A about X, [A:X]=[AB]x[B:X]
    '''
    def discountB(self, atrustOnB: sbool) -> sbool:
        if atrustOnB == None:
            raise ValueError('Discountion operator parameter cannot be None')

        p: float = atrustOnB.belief() # instead of atrustOnB.projection()
        b: float = p * self.belief()
        d: float = p * self.disbelief()
        u: float = 1 - b - d # = atrustOnB.disbelief() + atrustOnB.uncertainty() + atrustOnB.belief()*self.uncertainty()
        a: float = self.baseRate()

        return sbool(b,d,u,a)


    ''' Multi-edge path versions '''
    '''
        self method implements the discounting operator on multi-edge paths, 
        using the 'probability-sensitive trust discounting operator'
        which causes the uncertainty in A�s derived opinion about X to increase as a 
        function of the projected distrust in the source/advisor B. 
     
        For more details, refer to Chapter 14 of the Subjective Logic book by Josang, 
        specifically Section 14.3.4 that defines Trust Discounting with Multi-Edge Paths.
     
        we assume that 'self' represents the opinion (functional trust) of an agent An 
        on statement X, i.e., [An:X]
    
        @param agentsTrusts A collection of trust referrals that Agent (Ai) has on (Ai+1). [AiAi+1]
        return a sbool that represents the resulting opinion of A1 on X. 
        [A1:X]=[A1A2...An]x[An:X]
    '''
    
    def discount(self, agentsTrusts: sbool) -> sbool:
        if agentsTrusts == None:
            raise ValueError('Discountion operator parameter cannot be None')

        # self IS THE DISCOUNT OPERATOR DEFINED IN THE JOSANG 2016 BOOK 
        p: float = reduce(1.0,lambda acc,value : acc * value, map(lambda o : o.projection(), agentsTrusts))
        b: float = p * self.belief()
        d: float = p * self.disbelief()
        u: float = 1 - p * (self.disbelief() + self.belief())
        a: float = self.baseRate()

        return sbool(b,d,u,a)

    '''
        self method implements the discounting operator on multi-edge paths, 
        using the 'discounting operator' discountB() defined by Kurdi et al in 
        their 2018 paper 
         
        Heba Kurdi, Bushra Alshayban, Lina Altoaimy, and Shada Alsalamah
        'TrustyFeer: A Subjective Logic Trust Model for Smart City Peer-to-Peer Federated Clouds'
        Wireless Communications and Mobile Computing, Volume 2018, Article ID 1073216, 13 pages
        https:#doi.org/10.1155/2018/1073216
         
        we assume that 'self' represents the opinion (functional trust) of an agent An 
        on statement X, i.e., [An:X]
        
        return a sbool that represents the resulting opinion of A1 on X. 
        [A1:X]=[A1A2...An]x[An:X]
    '''
    def discountB(self, agentsTrusts: list[sbool]) -> sbool:
        if agentsTrusts == None:
            raise ValueError('Discountion operator parameter cannot be None')
        
        # self IS THE DISCOUNT OPERATOR DEFINED IN THE JOSANG 2016 BOOK 
        p: float = reduce(1.0,lambda acc,value : acc * value, map(lambda o : o.belief(), agentsTrusts))
        b: float = p * self.belief()
        d: float = p * self.disbelief()
        u: float = 1 - p * (self.disbelief() + self.belief())
        a: float = self.baseRate()

        return sbool(b,d,u,a)
    
    ''' comparison operations '''
    def equals(self, o: sbool) -> bool:
        if id(self) == id(o):
            return True
        if o == None or self.__class__ != o.__class__:
            return False

        return 	abs(self.belief()-sbool.belief()) < 0.001 and \
                abs(self.disbelief()-sbool.disbelief()) < 0.001 and \
                abs(self.uncertainty()-sbool.uncertainty()) < 0.001 and \
                abs(self.baseRate()-sbool.baseRate()) < 0.001

    def distinct(self, b: sbool) -> bool:
        return not self.equals(b)

    def min(self, opinion: sbool) -> sbool: # minimum based on projections
        return self if self.projection() <= opinion.projection() else opinion

    def max(self, opinion: sbool) -> sbool: # maximum based on projections
        return self if self.projection() >= opinion.projection() else opinion

    def hashCode(self) -> int:
        return round(float(self.b*100)) \
                + 10 * round(float(self.d * 100)) \
                + 100 * round(float(self.u*100)) \
                + 1000 * round(float(self.a*100))

    '''Conversions'''
    def __str__(self) -> str:
        return 'sbool({:5.3f}, {:5.3f}, {:5.3f}, {:%5.3f})'.format(self.b, self.d, self.u, self.a)
        
    def __repr__(self) -> str:
        return self.__str__()

    def toubool(self) -> ubool: # returns the projected probability
        return ubool(self.projection()) 

    ''' Other Methods '''
    def compareTo(self, other: sbool) -> int:
        x: float = abs(self.belief()-other.belief()) \
                    + abs(self.disbelief()-other.disbelief()) \
                    + abs(self.uncertainty()-other.uncertainty()) \
                    + abs(self.baseRate()-other.baseRate())
        if x < 0.001:
            return 0
        elif self.projection()-other.projection() < 0:
            return -1
        return 1

    def copy(self) -> sbool:
        return sbool(self.belief(),self.disbelief(),self.uncertainty(),self.baseRate(),self.relativeWeight)