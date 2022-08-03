
# Final assignment 7/21/2022
# TEMPLATE
# CS5007
# tpetit@wpi.edu

# Section 1

print('\n\nSection 1:')
class Node:
    def __init__(self,left,value,right):
        # left and right are of class Node
        self.left = left
        self.value = value # we assume that all the values are integers
        self.right = right
        
    def __str__(self):
        res = '['
        if(self.left != None):
            res += 'left:' + self.left.__str__()
        else:
            res += 'None'
        res += ','+str(self.value)+','
        if(self.right != None):
            res += 'right:' + self.right.__str__()
        else:
            res += 'None'
        return res+']'
    
    def invert(self):
        self.value = 0-self.value
        if(self.left != None):
            self.left.invert()
        if(self.right != None):
            self.right.invert()
        
    def toList(self, current):
        current.append(self.value)
        if(self.left != None):
            self.left.toList(current)
        if(self.right != None):
            self.right.toList(current)
        return current

    

class BinTree:
    def __init__(self,root=None):
        self.root = root
        
    def __str__(self):
        if self.root != None:
            return self.root.__str__()
        return 'Empty tree'
    
    def invert(self):
        if(self.root != None):
            return self.root.invert()
        
    def toList(self):
        current = []
        if(self.root != None):
            return self.root.toList(current)
        

x1 = Node(None, 5, None)
x2 = Node(None, 6, None)
x3 = Node(x1, 4, None)
x4 = Node(x2, 9, x3)
x5 = Node(None, 7, None)
x6 = Node(x4, 15, x5)
tree = BinTree(x6)

# Write the additional tests below
tree.invert()
print(tree.toList())
tree.invert()
print(tree.toList())

# Write the class ColorNode below
class ColorNode(Node):
    def __init__(self,left,value,right,color):
        Node.__init__(self,left,value,right)
        self.color = 'blue'
    def toList(self):
        print( str(self.value) + ":" + self.color)
        if(self.left != None):
            self.left.toList()
        if(self.right != None):
            self.right.toList()

# Once ColorNode is written, uncomment the following tests:

x1 = ColorNode(None, 5, None, 'green')
x2 = Node(None, 6, None)
x3 = ColorNode(x1, 4, None,'blue')
x4 = ColorNode(x2, 9, x3, 'purple')
x5 = ColorNode(None, 7, None,'red')
x6 = Node(x4, 15, x5)
tree = BinTree(x6)
#print(tree.toList())





# Section 2

print('\n\nSection 2:')

class DNA:
    def __init__(self, aString):
        self.seq = []
        for e in aString:
            self.seq.append(e)
    def __str__(self):
        s = ''
        for e in self.seq:
            s += e
        return s
    def getList(self):
        newList = []
        for e in self.seq:
            newList.append(e)
        return newList
    def glue(self, dnaObject):
        #return NEW DNA object that represents the concat. of the list of
        #letters of dnaObject and self.seq
        dnaObjectList = dnaObject.getList()
        string = ''
        for e in dnaObjectList:
            string+=e
        return DNA(string)
    def countSeq(self, aString):
        count = 0
        newString = ''.join(self.seq)
        count = newString.count(aString)
        return count
            
    def countSet(self, aList):
        dictionary = {}
        for e in aList:
            dictionary[e] = None
        for key in dictionary:
            val = self.countSeq(key)
            dictionary[key]=val
        print(dictionary)

       
x = DNA('AAAECGTAECGTCEC')
y = DNA('GGCTGTA')
z = x.glue(y)
t = y.glue(x)
print(x)
print(y)
print(z)
print(t)
print(x.countSeq('A'))
print(x.countSeq('EC'))
print(x.countSeq('AGCT'))
print(x.countSet(['A','EC','CGT','ACGT','GTC','A','EC']))

        











