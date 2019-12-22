from pyknow import *

class Retakes(KnowledgeEngine):
    # Grade parameter gradeparam takes a string grade as number and converts it to grade alphabet
    gradeparam = {'D':1, 'D+':2, 'C-': 3,'C':4, 'C+':5, 'B-':6, 'B':7}

    #core parameter takes an integer and converts it to a category
    coreparam = {'CSE':1, 'SEPS': 2, 'UNI': 3, 'CAPS':4, 'TRAIL':5}

    #list wich saves all the retakeable courses
    retakes = []

    #corere --> list of core retakable courses 
    corere =[]

    #sepsre --> list of SEPS retakable courses 
    sepsre = []

    # unire --> list of university core retakable courses
    unire = []


    #@Rule(Fact(MATCH.coursename, grade= ~L('N')& ~L('F')& ~L('A')& ~L('A-')& ~L('B+')))
    #def take(self, coursename):
     #   pass



    '''basic retaking list
    3 types of instances have 3 rules
    1.name --> Course name
    2.grade --> grade for the corresponding course
    3.category --> which category the course falls under
    '''



    @Rule(AS.courses << Fact(name=W(), grade= ~L('N')& ~L('F')& ~L('A')& ~L('A-')& ~L('B+'), category="CSE"))
    def take2(self, courses):
        f = courses.as_dict()
        self.retakes.append([self.gradeparam[f['grade']],self.coreparam[f['category']],f['name']])
        self.corere.append([self.gradeparam[f['grade']], f['name']])

    @Rule(AS.courses << Fact(name=W(), grade=~L('N') & ~L('F') & ~L('A') & ~L('A-') & ~L('B+'), category="SEPS"))
    def takeseps(self, courses):
        f = courses.as_dict()
        self.retakes.append([self.gradeparam[f['grade']], self.coreparam[f['category']], f['name']])
        self.sepsre.append([self.gradeparam[f['grade']], f['name']])

    @Rule(AS.courses << Fact(name=W(), grade=~L('N') & ~L('F') & ~L('A') & ~L('A-') & ~L('B+'), category="UNI"))
    def takeuni(self, courses):
        f = courses.as_dict()
        self.retakes.append([self.gradeparam[f['grade']], self.coreparam[f['category']], f['name']])
        self.unire.append([self.gradeparam[f['grade']], f['name']])

    


    '''
    returning the list of retakable courses
    '''

    
    def listpass(self):
        return self.retakes