#Jacob Chlebowski HW4

############################################################################
#       1. TREES, APPLICATIONS


class Node:
    def __init__(self,left,right):
        self.left = left
        self.right = right
    def weight(self):
        weight=0
        if(self.left != None):
            weight += self.left.weight()
        if(self.right != None):
            weight += self.right.weight()
        return weight
    def isWellBalanced(self):
        balanced = ((abs(self.left.weight() - self.right.weight()))<3)
        if(not balanced):
            return False
        self.left().isWellBalanced()
        self.right().isWellBalanced()
        return balanced

    
    
    
    def __str__(self):
        res = "("
        res += self.left.__str__()
        res += ","
        res += self.right.__str__()
        res += ")"
        return res

    

class Toy:
    def __init__(self,root=None):
        self.root = root
    def weight(self):
        if(self.root != None):
            return self.root.weight()
        return 0
    def isWellBalanced(self):
        if(self.root != None):
            return self.root.isWellBalanced()
        return False
    def __str__(self):
        if(self.root != None):
            return self.root.__str__()
        return 'Empty tree'

        

class Animal(Node):
    def __init__(self,w):
        self.w=w
    def weight(self):
        return self.w
    def isWellBalanced(self):
        return True
    def __str__(self):
        return str(self.w)


    

animalGreen = Animal(23)   
animalPink = Animal(13)
animalBlue = Animal(12)
animalYellow = Animal(26)
animalRed = Animal(25)
lr = Node(animalPink,animalBlue)
l = Node(animalGreen,lr)
r = Node(animalYellow,animalRed)
root = Node(l,r)

toy = Toy(root)


print(toy.weight()) #MUST KEEP THIS PRINT STATEMENT
print(toy.isWellBalanced()) #MUST KEEP THIS PRINT STATEMENT
print(toy) #MUST KEEP THIS PRINT STATEMENT




##################################################################################
#       2. ALGORITHMS ON LISTS AND TIME COMPLEXITY


def q1(aList):
    for e in range(len(aList)):
        if(aList[e]%2 == 0):
            print("even")
        else:
            print("odd")

myList = [1,2,3,4,5]
q1(myList)



def q2(aList):
    for e in range(len(aList)):
        if(aList[e]%2 == 0):
            print("even", end="")
        else:
            print("odd",end="")
        if(e+1 < len(aList)):
            print(", ",end="")
  
q2(myList)
print("")


def q3(aList):
    st=""
    for e in range(len(aList)):
        if(aList[e]%2 == 0):
            st += "even"
        else:
            st += "odd"
        if(e+1 < len(aList)):
            st += ", "
    return st
    

#returns same result as q2
print(q3(myList))
    



    

def q4(aList):
    for e in range(len(aList)):
        if(aList[e]%2 == 0):
            aList[e]='even'
        else:
            aList[e]='odd'





#MUST PRINT FOR TESTING
myList = [1,2,3,4,5]
q4(myList)
print(myList)


####2.2 Maximum Successive Integers
def succint(aList):
    count = 1
    nextMax=0
    #time complexity must be linear ==  O(N), for loop (through N times)

    #time complexity must be linear ==  O(N), for loop (through N times)    
    for e in range(len(aList)-1):
        if(aList[e]==aList[e+1]):
            count = count + 1
        else:
            if(nextMax < count):
                nextMax=count
            count = 1
    return nextMax


l1 = [1,1,1,3,3,4,4,4,4,4,3,1,7,3,3,4,4]
l2 = []
l3 = [1,2,1,1,2,1,1]
print(succint(l1))
print(succint(l2))
print(succint(l3))




#This function is O(N) because the for loop goes through the range of 0 to N
#which makes it linear.


