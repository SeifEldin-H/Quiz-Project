from Questions import Subject
#importing the random feature to randomize the questions
import random
import time
import copy
from inputimeout import inputimeout, TimeoutOccurred
import sys
def Intro()-> str:
    global Username
    """
    Username: -> str

    """
    print("Welcome To the Quiz")
    Username = input("please enter your username ")
    return Username
#Mainemenu() function prints the main menu of the quiz and asks user for an input
def MainMenu() -> str:
    """
        UserStart: -> int

    """
    global UserStart
    print("1. Start Quiz")
    print("2. Go through results")
    while True:
        try:
            UserStart = int(input("Please Choose (1 or 2) (to exit enter 0) "))   
        except ValueError:
            print("Invalid input, Correct values ar (1 or 2)")
            continue
        break
    if UserStart == 0:
       sys.exit()
                

def Topics():
    """
    
    """
    global Topic, Start, Elapsed, Limit, Count
    
    print("===============")
    print("1. Math")
    print("2. Physics")
    print("3. English")
    while True:    
        try:    
            Topic = int(input("Please choose a topic from the list above (1, 2, 3) "))
            while Topic !=1 and Topic !=2 and Topic !=3:
                print("Invalid Input")
                Topic = int(input("Please choose a topic from the list above (1, 2, 3) "))
        except ValueError:
            print("Invalid input please enter (1, 2 or 3)")
            continue
        break   
    Elapsed = 0
    Limit = 60
    Start = time.time()
    Count=0
    return Limit
    

def Display() -> str:
    """
        Question -> str
    """
    for x in Question: 
        print(str(*x[:-1])) #this converts the item in the array to str so that it can remove Curly brackets that appear when it outputs the question
    for Answers in Options:
        print(Answers)
#this goes through the Subject dictionary to randomize and pick a question from a specific subject 
def randomizer() -> dict:
    global Question, Options, Ans, Rq
    Question = []
    Options = []
    Ans = []
    if Topic == 1:
        Rq = random.choice(list(Subject["Math"].items()))
        Quiz = copy.deepcopy(Rq)
        Ans.append(Rq[1]["Answer"])
        Options.append(Rq[1]["A"])
        Options.append(Rq[1]["B"])
        Options.append(Rq[1]["C"])
        Options.append(Rq[1]["D"])
        Quiz[1].clear()
        Question.append(Quiz)
        Display()
    elif Topic == 2:
        Rq = random.choice(list(Subject["Physics"].items()))
        Quiz = copy.deepcopy(Rq)
        Ans.append(Rq[1]["Answer"])
        Options.append(Rq[1]["A"])
        Options.append(Rq[1]["B"])
        Options.append(Rq[1]["C"])
        Options.append(Rq[1]["D"])
        Quiz[1].clear()
        Question.append(Quiz)
        Display()
    elif Topic == 3:
        Rq = random.choice(list(Subject["English"].items()))
        Quiz = copy.deepcopy(Rq)
        Ans.append(Rq[1]["Answer"])
        Options.append(Rq[1]["A"])
        Options.append(Rq[1]["B"])
        Options.append(Rq[1]["C"])
        Options.append(Rq[1]["D"])
        Quiz[1].clear()
        Question.append(list(Quiz))
        Display()

        


def Guess():
    global Count
    """
        Guess: -> str
    """
    Timer = Limit - Elapsed.__round__(0)
    print(f"You have {Timer}s left")
    try: 
        Guess = inputimeout(prompt = "please enter a guess to the question (A, B, C, D) ", timeout = Timer)
        while Guess != "A" and Guess != "B" and Guess != "C" and Guess != "D":
            print("incorrect input, must be (A, B, C or D)")
            Guess = inputimeout(prompt = "please enter a guess to the question (A, B, C, D) ", timeout = Timer)
        for key in Rq:
            if Ans[0] == Guess:
                print("Correct")
                Count += 1
                break
            else:
                print("Incorrect")
                print("Correct answer was", Ans[0])
                break
    except TimeoutOccurred:
        print("Times Up")

def Viewing():
    global View
    View = open("Scores.txt", "r")
    for x in View:
        print(x)
    View.close()        
def Scores():
    Score = open("Scores.txt", "a")

    Score.write(f"{Username}, You got {Count} Questions correct. \n")
    
    Score.close()


