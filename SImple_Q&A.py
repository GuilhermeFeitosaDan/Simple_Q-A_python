# Simple Q&A in Python by Guilherme Feitosa Dan
# The objective was just to create a game where the questions would be asked randomly and to use a function that would call a list with all the possible questions

import random

def questions(x):
    q_use = list()
    q_use = q[x-1]

    if q_use[3] == 0:
        
        q_use[3] = 1
        print(q_use[1])
        anw = input().lower()
        
        if anw == q_use[2]: 
            print("\nCORRECT!\n")
            flag = 1        
        
        else: 
            print("\nINCORRECT!!\n")
            print("The correct answer was: " + q_use[2].upper())
            flag = 0
        return flag, True

    elif  q1[3] == 1:
        flag = 0           
        return flag, False

# questions
q1 = [1, "What does PLC mean?", "programmable logic controller", 0 ]
q2 = [2, "What does PRG mean inside CODESYS?", "program", 0 ]
q3 = [3, "What does FB mean inside CODESYS?", "function block", 0 ]
q4 = [4, "What does FUN mean inside CODESYS?", "function", 0 ]
q5 = [5, "What's the biggest human body organ?", "skin", 0 ]
q6 = [6, "What does GPU stand for?", "graphics processing unit", 0 ]
q7 = [7, "What does RAM stand for?", "random access memory", 0 ]
q8 = [8, "What does PSU stand for?", "power suply", 0 ]
q9 = [9, "In a Lead compensator, who is the closest to the origin - pole or zero?", "zero", 0 ]
q10 = [10, "In a Lag compensator, who is the closest to the origin - pole or zero?", "pole", 0 ]
q11 = [11, "What does POU mean inside CODESYS?", "program organization unit", 0 ]

q = [q1, q2, q3,q4,q5,q6,q7,q8,q9,q10,q11]

print("Hello, welcome to the Q&A game!!!")
anw = input("Do you feel like playing it?  ('YES' or 'NO')")

# inicialization of variables
i = 0 
score = 0

if anw.lower() == "yes":
    print("Let's start then\n")
    
# defines how many questions will be asked
    while i < 5:
        a = questions(random.randint(1,11))
        if a[0] == 1:
            score += 1
        else: pass

        if a[1]:
            i += 1
        else: pass
    
    print("\nYOU HAVE SCORED:",str(score), "POINTS IN THIS GAME")
        
elif anw.lower() == "no":
    print("OK, see you later aligator!")

else: print("Try to type something acceptable")
