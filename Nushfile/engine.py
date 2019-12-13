from .prerequisites import *
from .retakes import *
from pyknow import *
from .models import Courses, Student
'''
Inference engine class for the Expert System AI
* creates Inference engine for prerequisite knowledge base
* gets the AI for course Suggestion
'''
class Engine():
    '''
    l --> list of suggested courses
    seps --> list of seps suggested courses
    cse --> list of cse suggested courses
    uni --> list of university core suggested courses
    facts --> list of facts

    '''


    l = []
    seps = []
    cse = []
    uni = []
    p = 11
    facts  = []

    '''
    CONSTRUCTOR
    Initiates the knowledge base

    head --> contains the list of facts

    '''
    def __init__(self):
        self.engine = Prereq()
        self.head = len(self.facts)

    '''
    resets the Inference engine
    '''

    def resetengine(self):
        self.engine.reset()

    '''

    Adds the facts into the facts list
    Updates the number of facts in head

    ARGS:
    List --> 2D list containing facts 
    
    '''

    def setfactdatalist(self, list):
        self.facts.append(list)
        self.head = len(self.facts)

    '''
    Return: list of facts

    '''

    def getfactdatalist(self):
        return self.facts

    '''
    return: Integer 
    number of facts
    '''

    def getfactnumber(self):
        return self.head
    '''
    defines facts into the Inference Engine

    '''

    def definefacts(self, numofcrdts):
        for f in self.facts:
            #print(f[0],f[1],f[2])
            self.engine.declare(Fact(f[1], grade=f[2]))
        self.engine.declare(Fact(credit= numofcrdts))

    '''
    Modifies the facts based on the situations

    ARGS:
    coursename --> String containing the course name
    grade --> String of grade

    RETURN: None
    '''




    def modifyfacts(self, coursename, grade):
        for h in self.facts:

            if h[1] == coursename:
                print(h[0],h[1],h[2])
                self.engine.retract(h[0])
                self.engine.declare(Fact(coursename, grade=grade))
                h[2] = grade
                h[0] = self.head
                self.head = self.head + 1
            self.facts = sorted(self.facts)

    '''
    returns a list of courses
    '''

    def getrunning(self):
        n =[]
        srt=[]
        mvp = []
        credit_limit =13 # A knowledge engine for students how much credits should they take on this semester
        this_session_credit =0

        self.engine.run()
        t = self.engine.listpass()
        '''search the courses and sort them by the priority -> credits '''
        #print('is it working?')
        for f in t:
            crs = Courses.objects.get(coursename= f)
            mvp.append([crs.priority,crs.credits,crs.coursename])
        t.clear()
        mvp = sorted(mvp)
        for m in mvp:
            if this_session_credit< credit_limit:
                srt.append(m)
                this_session_credit= this_session_credit + crs.credits

        #srt = sorted(srt)
        #print(srt)
        courselist =[]
        for s in srt:
            courselist.append(s[2])
        #p1,p2, courselist = zip(*srt)
        #print(courselist)
        return courselist
        #return sorted(srt)
        #print(t)
        '''
        for to in t:
            n.append(to)
        t.clear()
        if len(n) > 4:
            return n[-4:]
        else:
            return n
        '''


    def simulation(self):
        s = self.getrunning()

        print(s)
        while(len(s)!=0):
            for s1 in s:
                self.modifyfacts(s1,'S')
            s.clear()
            s = self.getrunning()
            #print(self.engine.facts)
            #print(s)

'''
Inference engine class for the Expert System AI
* creates Inference engine for prerequisite knowledge base
* gets the result for Full Graduation path
* Runs the Engine Inference Engine multiple times as a simulation to detect the full Graduation path of the particular student.

'''


class Gradepath():

    '''
    Constructor
    ARGS:
    f1 --> 2D list of course information that contains
        index 0 -> course name
        index 1 -> course credit
        index 2 -> course grade
    credit --> total credit completed
    
    
    LOCAL VARIABLE:
    pathlist--> list of semester prediction
    credit --> total credit completed






    '''


    def __init__(self, f1, credit):
        self.pathlist = []
        self.credit = credit
        i=0
        while (self.checker(f1) == True):
            # print(f1)
            i = i + 1
            #print(i)
            p = self.runningengine(f1)
            if(len(p)==0):
                break
            self.pathlist.append(p)
            f1 = self.changinglist(p, f1)

    '''
    Returns Pathlist
    '''
    def returncoursepath(self):
        return self.pathlist

    '''
    checker Checks if a course have been done or not, sequentially

    ARGS:
    d --> list of courses

    RETURN: boolean

    '''

    def checker(self,d):
        i = 0
        # print(d)
        for d1 in d:
            # print(d1[2])
            if d1[2] == 'N':
                # print(d1)

                # print(d1[2])
                return True
            else:
                pass
        return False

    '''

    Runs the Course Suggestion Inference Engine 

    ARGS:
    fprog --> 2D list of course information

    Return: list
    p --> list of suggested Course
    
    '''
    def runningengine(self,fprog):

        e = Engine()
        e.resetengine()
        for f2 in fprog:
            e.setfactdatalist(f2)
        e.definefacts(self.credit)
        # print(e.getfactnumber())
        # e.simulation()
        p = e.getrunning()

        print(p)
        return p

    '''
    changinglist

    for full graduation path we need to do a simulation of the course Suggestion 
    multiple times just changing the facts of previously suggested courses. so this
    function changes the course grade from 'N' to 'S' so that that course is no 
    longer looks like it hasnt been done.

    ARGS:
    prevcrs --> previously suggested course list
    List --> 2D list of course information

    RETURN: list

    '''
    def changinglist(self,prevcrs,list):
        print("in changing list")
        print(prevcrs)
        for p1 in prevcrs:
            crdt = Courses.objects.get(coursename= p1)
            self.credit = self.credit + crdt.credits
            for w1 in list:
                if w1[1] == p1:
                    w1[2] = 'S'
        return list




'''
if __name__ == '__main__':
    lst=[]
    i =1
    grdobj = Grades.objects.filter(Student_id=stdid)
    for grd in grdobj:
        lst.append([i, grd.Course_name, grd.grade])
        i=i+1
    obj = Gradepath(lst)
    d = obj.returncoursepath()
    print(d)
'''