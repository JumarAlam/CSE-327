from .retakes import *
from pyknow import *
from .models import Courses, Student



class Retakecrs:
    '''
    CONSTRUCTOR
    Initiates the knowledge base
    '''
    def __init__(self):
        self.engine = Retakes()
        self.facts = []
    '''
    RESETS THE INFERENCE ENGINE
    ''' 
    def resetengine(self):
        self.engine.reset()

    '''
    Adds the facts into the facts list
    Updates the number of facts in head
    '''    


    def setfactdatalist(self, list):
        self.facts.append(list)
    '''
    returns list of lists '''

    def getfactdatalist(self):
        return self.facts
        ''' decalre facts 
        '''

    def definefacts(self):
        for f in self.facts:
            #print(f[0],f[1],f[2])
            self.engine.declare(Fact(name=f[0], grade=f[1], category=f[2]))
        '''
        returns retake list

        '''
    def runes(self):
        self.engine.run()
        return self.engine.listpass()

