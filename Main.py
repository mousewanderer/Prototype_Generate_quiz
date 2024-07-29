import random,json, randfacts
from datetime import datetime


import factsgen
import multi
from storing import open_highscore, get_highscore


global change,score
change = False
score = 0


def Hardmode(q,a):
    points = 0
    for num in range(0,10):
        print(f"{q[num]}")
        
        write = input(":")
        if write == a[num]:
            print("Correct")
            points +=1
        else:
            print("Wrong")
            print(f"The answer is {a[num]}")

    if points == 1:
        print(f"you have {points} point")
    else:
        print(f"you have {points} points")


    if open_highscore() < points or open_highscore() == None:
        print("NEW HIGHSCORE")
        change = True
        get_highscore(points)
        score = points


def Easymode(q,a,b,c,d):
    
    k = [a,b,c,d]
    valid = ["a","b","c","d"]

    number = 1

    
    points = 0
    for num in range(0,10):
        print(f"{number}.  {q[num]}")
        value = random.shuffle(k)

        count = 0
        location = {"A": "", "B": "", "C":"","D":""}
        number+=1
        
        for run in k:
            print(f"{valid[count]}. {run[num]}")
            location[valid[count].upper()] = run[num]
            
            count +=1
            
            

        while True:
            try:
                write = input(":").upper()
                if write.lower() not in valid:
                    raise Exception
                elif location[write] == a[num]:
                    print("Correct")
                    points +=1
                    break
                else:
                    print("Wrong")
                    print(f"The answer is {a[num]}")
                    break
            except:
                print("invalid Value")
                
    if points == 1:
        print(f"you have {points} point")
    else:
        print(f"you have {points} points")

    if open_highscore() == None:
        get_highscore(0)
    elif open_highscore() < points:
        print("NEW HIGHSCORE")
        change = True
        get_highscore(points)
        score = points
        
#_____________________________________________________________________________________
def MainMenu():
    keys = ["A","B","C","X"]
    
    first = True
    while first:
        c = datetime.now().strftime('%H:%M:%S')
        print(f"Time now : {c}")
        print(""" Facts quiz
            A. Easy Mode
            B. Hard Mode
            C. View High score
            X. Exit

          """)
   
        try:
            y = input(":").upper()
            if y not in keys:
                raise ValueError
            elif y == "A":
                Easymode(factsgen.questions,factsgen.answers,multi.wrong1,multi.wrong2,multi.wrong3)
            elif y == "B":
                Hardmode(factsgen.questions,factsgen.answers)
            elif y == "C":
                if change == False:
                    print(open_highscore())
                elif change == True:
                    print(score)
                    
            elif y == "X":
                print("Good Bye")
                first = False

            
        except ValueError:
            print("Invalid Keys")


MainMenu()
            

            
