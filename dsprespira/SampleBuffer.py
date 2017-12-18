'''
Created on 21 nov. 2017

@author: Dimitri
'''
import statistics

class SampleBuffer(object):

        
    def __init__(self):
        self.dataWave= []

    def __append__(self,dbspl):
        self.dataWave.append(dbspl)
 
    def getMedian(self):
        return statistics.median(self.dataWave)
        
    
    def getSyllables(self):    
        numSyll=0
        for value in range(0,len(self.dataWave)):
                #print("teller:"+ str(value+1))
                #print("waarde:"+ str(self.dataWave[value]))
                if value>5:
                    if self.dataWave[value-4]<self.dataWave[value-3]<self.dataWave[value-2]>self.dataWave[value-1]>self.dataWave[value]:
                        if self.getMedian()<self.dataWave[value-2]:
                            if self.dataWave[value-2]-self.dataWave[value-2]<2 and self.dataWave[value-2]-self.dataWave[value-1]<2:
                                numSyll+=1
                 
        return numSyll