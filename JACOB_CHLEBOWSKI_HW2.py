# CS 5007 HW2 template

# ---
# Day number
# Write below the dayNumber function & tests

#1 for Monday, 2 for Tuesday etc...
#if it's not a day return -1
#NOT case sensitive - st.lower()
def dayNumber(st):
    st = st.lower()
    if(st=="monday"):
        return 1
    elif(st=="tuesday"):
        return 2
    elif(st=="wednesday"):
        return 3
    elif(st=="thursday"):
        return 4
    elif(st=="friday"):
        return 5
    elif(st=="saturday"):
        return 6
    elif(st=="sunday"):
        return 7
    else:
        return -1
    

day1 = dayNumber('Thursday')
day2 = dayNumber('thursday')
day3 = dayNumber('FRIDAY')
day4 = dayNumber('not a day')
print(day1,day2,day3,day4)



# ---
# Iterating function
# Write below the repeatSt function & tests

#Print n times st, each on new line
#if n<=0 do nothing
def repeatSt(st,n):
    i=0
    if(n<=0):
        return
    else:
        while(i<n):
            print(st+'\n')
            i+=1

repeatSt('Hello',4)
repeatSt('grrr',-1)


# ---
# Taylor Sinus
# Write your code below

#approximates sin(x) in radians
import math
def taylor(x,n):
    current=0
    for i in range(n):
        current = current + (((-1)**(i))*(x**(2*i+1))/(math.factorial(2*i+1)))
    return current
        

x = math.pi/2
print(math.sin(x))
print(taylor(x,7))
    

# ---
# Input

def helloProgram():
    st = input('Please enter your name\n')
    print('Hello '+ st + '!')

# uncomment the following line to test this function    
helloProgram()

# Write your code below

#assign local variable grade with value of st casted as an integer, that is, int(st)
#print value of the grade variable
def enterAGrade():
    st = input('Please enter a grade in [0,100]\n')
    grade = int(st)
    print(grade)

enterAGrade()



def enterSomeGrades():
    aList = []
    st = input('Please enter a grade in [0,100]\n')
    aList.append(int(st))
    st = input('continue y or n?')
    while(st=='y'):
        st = input('Please enter a grade in [0,100]\n')
        aList.append(int(st))
        st = input('continue y or n?')
    print(aList)

enterSomeGrades()
        

# ---
# Extra-credit


#strictly positive n
#prints out triangle of height n using the symbol '*' without spaces
def triangle(n):
    for i in range(n):
        for j in range(i+2):
            if(j==1):
                print("*",end ="")
            if(j>1):
                print("**",end ="")
        print("\n")
    
   
        
        
    

triangle(6)

