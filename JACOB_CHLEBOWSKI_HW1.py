# CS 5007 - Homework 1 template
# tpetit@wpi.edu

'''
 Please read the PDF for the questions.
 Once you completed a question, run the module to test.
'''

# ----------
# QUESTION 1
# ----------
# Do not modify the three following statements:
a = True
b = False
c = True

# Write your code below: 
#   be1: (write expression in place of the zero in the next line)
be1 = a and (b or (not c))

#   be2: (write expression in place of the zero in the next line)
be2 = not b or (a or c)

#   be3: (write expression in place of the zero in the next line)
be3 = (a and b) or (not c)

#   be4: (write expression in place of the zero in the next line)
be4 = not a or (not b or (not c))

print(be1,be2,be3,be4)


# ----------
# QUESTION 2
# ----------
# Do not modify the three following statements:
a = 4.0
b = 4.0
c = 2.0

# Write your code below:
#   e1: (write expression in place of the zero in the next line)
e1 = 4*a*b + b*c

#   e2: (write expression in place of the zero in the next line)
e2 = b**4

#   e3: (write expression in place of the zero in the next line)
e3 = ((a*b)**(1/2))

#   e4: (write expression in place of the zero in the next line)
e4 = ((a*c - b*a)/(b*c))

#   e5: (write expression in place of the zero in the next line)
e5 = (((a**2)-(c**3))+(2*(a*b)))

print(e1,e2,e3,e4,e5)

# ----------
# QUESTION 3
# ----------

# (A) # Write your code below: 

student1 = "Marie"
student2 = "James"
student3 = "Lee"
print(student1,student2,student3)



# (B) Write your code below:

print(student1 + "\n" + student2 + "\n" + student3)





# (C) Write your code below: 

x = 18
y = 3
z = x/y
t = x//y
u = x%y

print(z,t,u)



# (D) Write your code below:

import math
radius = 3.5
area = (math.pi)*(radius**2)
print(area)


# ----------
# QUESTION 4
# ----------



#  1)  Write here your windChill function


def WindChill(temp,velocity):
    wc = 13.13 + 0.628*temp - 12.1 * (velocity**0.15) + 0.3967 * temp * (velocity**0.155)
    print("At " + str(temp) + "C and " + str(velocity) + "kph winds it feels like " + str(wc) + "C")



#   Call here your function with arguments -20 for T and 30 for V 

WindChill(-20,30)



#   2) Write here your windChill2 function.

def WindChill2(temp,velocity):
    wc = 13.13 + 0.628*temp - 12.1 * (velocity**0.15) + 0.3967 * temp * (velocity**0.155)
    return wc





#   Call here your windChill2 function with arguments -20 for T and 30 for V.
#   Print the result of this call. 


print("Wind Chill of -20C and 30kph winds: " + str(WindChill2(-20,30)) + "C")


