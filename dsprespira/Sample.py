'''
Created on 22 nov. 2017

@author: Dimitri
'''
import math
from wheel.signatures.djbec import double
from warnings import catch_warnings
from _csv import Error
class Sample(object):
    '''
    classdocs
    '''
    def getNumSamples(self):
        return len(self.data)

    def __init__(self, sampleArray):
        '''
        Constructor
        '''
        self.data=sampleArray
          
    def getLocalEnergy(self):
        power=0.0
        length= len(self.data)
        for var in range(length):
            buffer=self.data[var]
            power+= (buffer*buffer)
        return power
    
    def linear2Decimal(self,dblValue):
        return 20.0 * math.log10(dblValue)
 
    def getdbSPL(self):
        try:
            value =math.pow(self.getLocalEnergy(), 0.5)
            value /= len(self.data) 
            return self.linear2Decimal(value)
        except ValueError:
            print(self.getLocalEnergy())
            print(math.pow(self.getLocalEnergy(), 0.5))
          
            return 0
            
    
    def showValues(self, indata):
        for floatje in indata:
            print(float(floatje))