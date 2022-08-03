# tpetit@wpi.edu
# Homework 3 template

# 1

print('\n\nPart 1\n#####\n\n')
class Patient:
    # Add the constructor below
    def __init__(self, name, SSN):
        self.name = name
        self.SSN= SSN
    # Replace the return '' by your own code
    def __str__(self):
        st = ""
        st+= str(self.name) + "," + str(self.SSN)
        return st

class PatientQueue:
    # Add the constructor below
    def __init__(self):
        self.p1 = []
        self.p2 = []
        self.p3 = []

    # Replace the print('TODO') by your own code
    def add(self, patient, priority):
        if(priority==1):
            self.p1.append(patient.__str__())
        elif(priority==2):
            self.p2.append(patient.__str__())
        elif(priority==3):
            self.p3.append(patient.__str__())
        else:
            self.p3.append(patient.__str__())

    # Replace the print('TODO') by your own code
    #st....
    #more st's
    def nextPatient(self):
        #if statement checking if self.p1 is not empty? then pop and return
        #self.p1.pop()
        if self.p1:
            return self.p1.pop(0).__str__()
        elif self.p2:
            return self.p2.pop(0).__str__()
        elif self.p3:
            return self.p3.pop(0).__str__()
        else:
            return
        
    # Replace the return '' by your own code
    def __str__(self):
        st = ""
        stp1 = "\np1: " + self.p1.__str__()

        if(len(self.p1)>1):
            count=0
            for e in range(len(stp1)):
                #now e is the index at st
                if(stp1[e]==','):
                    if(count==1):
                        temp= list(stp1)
                        temp[e]=";"
                        stp1 = "".join(temp)
                        count=0
                    else:
                        count=1
    


        
        stp2 = "\np2: " + self.p2.__str__()

        if(len(self.p2)>1):
            count2=0
            for e in range(len(stp2)):
                #now e is the index at st
                if(stp2[e]==','):
                    if(count==1):
                        temp= list(stp2)
                        temp[e]=";"
                        stp2 = "".join(temp)
                        count2=0
                    else:
                        count2=1



        
        stp3 = "\np3: " + self.p3.__str__()


        if(len(self.p3)>1):
            count3=0
            for e in range(len(stp3)):
                #now e is the index at st
                if(stp3[e]==','):
                    if(count3==1):
                        temp= list(stp3)
                        temp[e]=";"
                        stp3 = "".join(temp)
                        count3=0
                    else:
                        count3=1

                    

        
        st +=  stp1 + stp2 + stp3
        st = st.replace("'","")

        
        return st

# Once you have finished to write the classes, uncomment the
# following tests. You must not have any error.

Paul = Patient("Allen",753265)
Marion = Patient("Raffi",435654)
Kalima = Patient("Aribi",873451)
Ann = Patient("Chang",771124)
Lee = Patient("Strong",113246)
p = PatientQueue()
print(p)
p.add(Paul,3)
p.add(Marion,2)
p.add(Kalima,1)
p.add(Ann,3)
p.add(Lee,1)
print(p)
for i in range(5):
    print("\nNext patient:", p.nextPatient())
    print("\nPatient list:", p)

# 2

print('\n\nPart 2\n#####\n\n')
# Write your code below (Counter and BCounter classes)

class Counter:
    def __init__(self, val=0):
        if(val<0):
            self.__val=0
        else:
            self.__val=val
    def increment(self):
        self.__val += 1
    def __str__(self):
        return str(self.__val)



def testCounter():
    counter1 = Counter()
    counter2 = Counter(350)
    print(counter1)
    print(counter2)
    counter1.increment()
    counter1.increment()
    counter2.increment()
    counter2.increment()
    print(counter1)
    print(counter2)

testCounter()

#-----------------------------------------------

#---2 BOUNDED COUNTER


class BCounter(Counter):
    def __init__(self,ub,val=0):
        if(ub<1):
            self.ub = 1
        else:
            self.ub = ub
        if(val<0):
            self.__val=0
        else:
            self.__val=val
        if(self.__val >= self.ub):
            print("WARNING, VAL >= UPPERBOUND")
            self.__val = 0
    def increment(self):
        test = self.__val + 1
        if(test < self.ub):
            self.__val += 1
        else:
            self.__val = 0
    def __str__(self):
        st = ""
        st += "Value: " + str(self.__val) + "\n"
        st += "Upperbound: " + str(self.ub) + "\n"
        return st


def testBCounter():
    b1 = BCounter(2)
    b2 = BCounter(2,350)
    print(b1)
    print(b2)
    b1.increment()
    b2.increment()
    print(b1)
    print(b2)
    b2.increment()
    print(b2)

testBCounter()



# 3
print('\n\nPart 3\n#####\n\n')

def robot_move(moves):
    x = 0
    y = 0
    for e in moves:
        if(e[0]=='N'): y=y+e[1]
        if(e[0]=='E'): x=x+e[1]
        if(e[0]=='S'): y=y-e[1]
        if(e[0]=='W'): x=x-e[1]
    return (x,y)

print(robot_move([('N',2), ('E',4), ('S',1), ('W',3)]))


