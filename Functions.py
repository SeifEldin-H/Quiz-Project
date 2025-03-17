from Questions import Subject
#importing the random feature to randomize the questions
import random
import time
import copy
import inputimeout
from inputimeout import inputimeout, TimeoutOccurred
import sys
def Intro()-> str:
    """
    Username: -> str

    """
    global Username
    print("Welcome To the Quiz")
    Username = input("please enter your username ") 
#Mainemenu() function prints the main menu of the quiz and asks user for an input
def MainMenu() -> str:
    """
        UserStart: -> int

    """
    global UserStart
    print("1. Start Quiz")
    print("2. Go through results")
    try:
        UserStart = int(input("Please Choose (1 or 2) (to exit enter 0) "))
    except ValueError:
        print("Invalid input, Correct values ar (1 or 2)")
    if UserStart == 0:
        sys.exit()

def Topics():
    global Topic, Start, Elapsed, Limit
    print("===============")
    print("1. Math")
    print("2. Physics")
    print("3. English")
    try:    
        Topic = int(input("Please choose a topic from the list above (1, 2, 3) "))
    except ValueError:
        print("Invalid input please enter (1, 2 or 3)")
    Elapsed = 0
    Limit = 10
    Start = time.time()
    
    

def Display() -> str:
    for x in Question: 
        print(str(*x[:-1]))
    for Answers in Options:
        print(Answers)
#this goes through the Subject dictionary to randomize and pick a question from a specific subject 
def randomizer() -> dict:
    global Question, Options, Ans, Rq
    Question = []
    Options = []
    Ans = []
    try:
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
    except:
            print("Invalid input")

        

Count=0
def Guess():
    global Count
    """
        Guess: -> str
    """
    Timer = Limit - Elapsed.__round__(0)
    print(f"You have {Timer}s left")
    try:
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
    Viewing()
    Score = open("Scores.txt", "a")
    if View == Username:
        Score.write(f"{Username}, You got {Count} Questions correct. \n")
    
    Score.close()


