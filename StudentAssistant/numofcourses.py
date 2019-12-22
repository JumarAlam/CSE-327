from pyknow import *

'''
Knowledge base for selecting how many courses a student can take.
'''
class Numofcrs(KnowledgeEngine):
    i=0
    maxcourse=15
    
    @Rule(Fact(cgpa= P(lambda x: x>=3.5)))
    def allowedcrdtup35(self):
        self.maxcourse = 17

    @Rule(Fact(cgpa=P(lambda x: x < 3.5)),Fact(credits= P(lambda x:x<100)))
    def allowedcrdtup35(self):
        self.maxcourse = 15
    @Rule(Fact(credits= P(lambda x:x>100)))
    def allowed100(self):
        self.maxcourse= 17



    #Returns number of maximum credits
    def numbcrs(self):
        return self.maxcourse



'''
Driver file 
if __name__ == '__main__':
    engine = Numofcrs()
    engine.reset()
    engine.declare(Fact(cgpa=2.90))
    engine.declare(Fact(credits=90))
    engine.declare(Fact(semnum=12))

    engine.run()
    print(engine.numbcrs())
'''