#Jacob Chlebowski
#Midterm
#6/27/22

#1
print('#1\n')

#p = int
#s = int
#c = string

class House:
    def __init__(self,p,s,c):
        self.price= p
        self.sqft = s
        self.city = c
    def __str__(self):
        st = ''
        st += str(self.price) + "\n"
        st += str(self.sqft) + "\n"
        st += self.city + "\n"
        return st
    def unitPrice(self):
        return (self.price//self.sqft)



        
h1 = House(240000,1400,'Philadelphia')
print(h1)
print(h1.unitPrice())

h2 = House(160000,1000,'New York')
print(h2)
print(h2.unitPrice())



# 2
print('\n#2\n')

def spreadisp(value):
    input = value
    y = ''
    strx = str(value)

    for i in range(len(strx)):
        if(strx[i]=="-"):
            print("")
        else:
            y+= strx[i] + "\n"

   
    if(input < 0):
        print("minus")
        print(y)
    elif(input > 0):
        print("plus")
        print(y)
    elif(input==0):
        print("0")
    else:
        print("")

spreadisp(567)
spreadisp(-67)
spreadisp(0)

# 3.1
print('\n#3.1\n')

numberOfWheels = { 'car':[3,4], 'truck':[4,6,8,10], 'bike':[1,2], 'wheelchair':[4,6] }

#TEST

if(4 in numberOfWheels['truck']):
    print('truck')
if(4 in numberOfWheels['car']):
    print('car')
if(4 in numberOfWheels['bike']):
    print('bike')
if(4 in numberOfWheels['wheelchair']):
    print('wheelchair')





# 3.2
print('\n#3.2\n')

def remo(aList):
    for e in aList:
        if(not(e%2==0)):
            aList.remove(e)
    for i in range(len(aList)):
        aList[i] += 1






