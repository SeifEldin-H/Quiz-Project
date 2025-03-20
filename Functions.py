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
    This function Introduces the user to the quiz program and prompts them to enter their user name

    Parameters
    -----------

    Username: str
        This lets the user input their chosen username

    """
    print("Welcome To the Quiz")
    Username = input("please enter your username ")

# This function prints the main menu of the quiz and asks user for an input
def Main_Menu() -> str:
    """
    This function displays a main menu for the user to go through the quiz or look at results of previous attempts

    Parameters
    -----------

    User_Start: int
        This lets the user input an integer from 0 to 2 to either exit the program 


    """
    global User_Start, Numb_of_Q, Limit
    print("===============")
    print("1. Start Quiz")
    print("2. Go through results")
    while True:
        try:
            User_Start = int(input("Please Choose (1 or 2) (to exit enter 0) "))   
        except ValueError:
            print("Invalid input, Correct values ar (1 or 2)")
            continue
        break
    if User_Start == 0:
       sys.exit()
    Numb_of_Q = 3
    Limit = 60
    
                
# This function outputs the topic which the user can pick
def Topics() -> int: 
    """
    This functions prints the topic the user can choose and also allows the user to edit amount of questions and the length of the time limit
    
    Parameters
    ----------
    
    Topic: int

    Elapsed: Literal

    Count: Literal

    U_Answers: list

    """
    global Topic, Start, Elapsed, Limit, Count, U_Answers, Numb_of_Q
    Elapsed = 0
    Count=0
    
    U_Answers = []
    print("===============")
    print("1. Math")
    print("2. Physics")
    print("3. English")
    print("Enter 4 to change number of questions")
    print("Enter 5 to change the limit of seconds to complete quiz")
    while True:    
        try:    
            Topic = int(input("Please choose a topic from the list above (1, 2, 3) (To exit quiz enter 0) "))
            while Topic != 0 and Topic !=1 and Topic !=2 and Topic !=3 and Topic != 4 and Topic != 5 and Topic != 6:
                print("Invalid Input")
                Topic = int(input("Please choose a topic from the list above (1, 2, 3) (To exit quiz enter 0) "))
        except ValueError:
            print("Invalid input please enter (1, 2 or 3)")
            continue
        break
    if Topic == 0:
        sys.exit()
    elif Topic == 4:
        try:
            Numb_of_Q = int(input("Enter the number of questions you would like to answer (Max 10) (Default is 3 questions) "))
            while Numb_of_Q > 10 and Numb_of_Q < 0:
                print("Max number of questions is 10 please enter a number between 1 and 10")
                Numb_of_Q = int(input("Enter the number of questions you would like to answer (Max 10) (Default is 3 questions) "))
        except ValueError:
            print("Incorrect input please enter a valid integer")
    elif Topic == 5:
        try: # try is error handling any input that is not an integer
            Limit = int(input("Enter the number of seconds (Default is 60s) "))
        except ValueError:
            print("Incorrect input please enter a valid integer")

    print("===============")
    Start = time.time() # Declaring start here so it does not reset when going through questions using for loops in the main functions


    
    


# This goes through the Subject dictionary to randomize and pick a question from a specific subject 
def randomizer() -> dict:
    """
    This function picks a random question from the dictionary in Question.py and appends the options, question and answer.
    
    Parameters
    ----------

    Question: list
        This holds the question to display

    Options: list
        This holds the options the user can use 

    Ans: list
        This holds the correct option for the question

    Rq: tuple[str, dict[str, str]]
        The random question that is picked
    """
    global Question, Options, Ans, Rq, Numb_of_Q
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
        for x in Question: 
            print(str(*x[:-1])) # This converts the item in the array to str so that it can remove Curly brackets that appear when it outputs the question
        for Answers in Options:
            print(Answers)
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
        for x in Question: 
            print(str(*x[:-1])) # This converts the item in the array to str so that it can remove Curly brackets that appear when it outputs the question
        for Answers in Options:
            print(Answers)
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
        for x in Question: 
            print(str(*x[:-1])) # This converts the item in the array to str so that it can remove Curly brackets that appear when it outputs the question
        for Answers in Options:
            print(Answers)
        

#function that allows user input and validates input also has a timeout feature for when the timeout ends 
def Guess():
    """
    The guess function allows the user to input an answer to the question it also prints the timer and reduces the time left
    
    Parameters
    ---------

    Guess: LiteralString | str

    Timer: int

    UAnswer: list
    """
    global Count
    Timer = Limit - Elapsed.__round__(0)
    print(f"You have {Timer}s left")
    try: 
        Guess = inputimeout(prompt = "please enter a guess to the question (A, B, C, D) ", timeout = Timer).upper()
        while Guess != "A" and Guess != "B" and Guess != "C" and Guess != "D": #loop to validate user input
            print("incorrect input, must be (A, B, C or D)")
            Guess = inputimeout(prompt = "please enter a guess to the question (A, B, C, D) ", timeout = Timer).upper()
        for key in Rq: #loop that goes through the answer for each question and checks users input
            if Ans[0] == Guess:
                print("Correct")
                Count += 1
                U_Answers.append("Correct")
                break
            else:
                print("Incorrect")
                print("Correct answer was", Ans[0])
                U_Answers.append("Wrong")
                break
    except TimeoutOccurred:
        print("Times Up, returning to the main menu")
        time.sleep(1)
        U_Answers.append("Timeout")
#this functions allows the user to review their past results

def Scores():
    Score = open("Scores.txt", "a")
    if Topic == 1:
        Score.write(f"{Username}, You got {Count} Questions correct in math. {U_Answers} \n")
    elif Topic == 2:
        Score.write(f"{Username}, You got {Count} Questions correct in physics. {U_Answers} \n")
    elif Topic == 3:
        Score.write(f"{Username}, You got {Count} Questions correct in english. {U_Answers} \n")
    Score.close()


def Viewing():
    """
    This function views the results of the quiz and only prints specific usernames scores

    Parameter
    ----------

    View: TextIOWrapper[_WrappedBuffer]
        This opens the file to read the content

    Saved_User: list[str]
        This variable helps locate the username of the user to output their score 


    """
    View = open("Scores.txt", "r")
    Saved_User = View.readlines()
    for x in range(len(Saved_User)):
        if Username in Saved_User[x]:
            print(Saved_User[x])
    if Username not in Saved_User[x]:
        print("===============")
        print("user not found")
        
    View.close()
        