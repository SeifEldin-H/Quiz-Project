from Questions import Subject # Imports the nested dictionaty from the Questions file
import random # Importing the random feature to randomize the questions
import time # Imports time module to start the time
import copy # Imports copy module allowing use of deepcopy
from inputimeout import inputimeout, TimeoutOccurred # Imports input timeout feature from the inputimeout module for setting time limits for the user
import sys # Imports 


def Intro()-> str:
    global Username 
    """
    This function Introduces the user to the quiz program and prompts them to enter their user name

    Parameters
    -----------

    Username: str
        This lets the user input their chosen username

    Returns
    -----------

    Username
            Returns the username of the user
    """
    
    print("Welcome To the Quiz")
    while True: # Indefinite loop for error checking
        try: # try is error handling any incorrect input
            Username = input("please enter your username ")
            if len(Username) != 0 and not Username.isspace(): # This conditional statement check for empty spaces and empty inputs
                return Username
            else:
                print("invalid input, no spaces or empty characters") # This prints when the input is invalid
        except:
            pass
    
    

# This function prints the main menu of the quiz and asks user for an input
def Main_Menu() -> str:
    """
    This function displays a main menu for the user to go through the quiz or look at results of previous attempts

    Parameters
    -----------

    User_Start: int
        This lets the user input an integer from 0 to 2 to either exit the program
    
    Numb_of_Q: Literal[3]
        This is the number for the default amount of questions to appear

    Limit: Literal[60]
        This is the number for the limit that is set for completing the quiz

    """
    global User_Start, Numb_of_Q, Limit # Sets variables in this function to global so other functions can use variables
    print("===============")
    print("1. Start Quiz")
    print("2. Go through results")
    while True: # Indefinite loop
        try: # try is error handling any input that is not an integer
            User_Start = int(input("Please Choose (1 or 2) (to exit enter 0) ")) # Converts the input to integer so that it does not cause errors
            while User_Start != 0 and User_Start != 1 and User_Start != 2: # Checks if the input meets the requirements of the valid inputs
                print("Invalid input, Correct values ar (1 or 2)")
                return User_Start
        except ValueError:
            print("Invalid input, Correct values ar (1 or 2)")
            continue
        break
            
    if User_Start == 0: # Checks the users input for exiting the program
        sys.exit() # Command that exits the program
    Numb_of_Q = 3 # Initialises the number of questions
    Limit = 60 # Initialises the limit since 
    
                
# This function outputs the topic which the user can pick
def Topics() -> int: 
    """
    This functions prints the topic the user can choose and also allows the user to edit amount of questions and the length of the time limit
    
    Parameters
    ----------
    
    Topic: int
        allows the user to pick which topic to choose

    Elapsed: Literal[0]
        It is the time elapsed until time limit has been reached

    Count: Literal[0]
        This is the count for amount of question the user can get correct

    U_Answers: list
        This is to store what questions the user got correct, wrong or the timeout

    Start: float
        This to initialise the starting time of the quiz

    """
    global Topic, Start, Elapsed, Limit, Count, U_Answers, Numb_of_Q
    Elapsed = 0 # Initialises the elapsed time to 0 so that it resets when going back to the Topics menu
    Count=0 # Initialises the count to 0 so that it resets the count for amount of questions gotten correct to 0 so that 
    U_Answers = [] # This list is for
    # Prints the options for the user to choose for subjects or changing timing and number of questions
    print("===============")
    print("1. Math")
    print("2. Physics")
    print("3. English")
    print("4. to change number of questions")
    print("5. to change the limit of seconds to complete quiz")
    while True:    # Indefinite Loop
        try:    
            Topic = int(input("Please choose a topic from the list above (1, 2, 3) or to change amount of seconds or question (4,5) (To exit quiz enter 0) "))
            while Topic != 0 and Topic !=1 and Topic !=2 and Topic !=3 and Topic != 4 and Topic != 5 and Topic != 6: # Checks if the input is not the options shown to loop for a correct input
                print("Invalid Input please enter (1, 2 or 3)")
                Topic = int(input("Please choose a topic from the list above (1, 2, 3) or to change amount of seconds or question (4,5) (To exit quiz enter 0) "))
        except ValueError:
            print("Invalid input please enter (1, 2 or 3)")
            continue
        break
    if Topic == 0:
        sys.exit() #This exists the code
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
def Randomizer() -> dict:
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
    global  Rq, Numb_of_Q, Ans
    Question = [] # initialised the Question list for appending the question asked
    Options = [] # initialised the Options list for appending the options printed
    Ans = [] # initialised the Ans list for appending the answer 

    if Topic == 1: # This is the topic for math
        Rq = random.choice(list(Subject["Math"].items())) # This picks a random question from the math subject dictionary
        Quiz = copy.deepcopy(Rq) # This copies the Rq list to only have the question to appear
        Ans.append(Rq[1]["Answer"]) # This appends the answer to the Ans list
        
        # Here is where each option is appended to the Options list
        Options.append(Rq[1]["A"])
        Options.append(Rq[1]["B"])
        Options.append(Rq[1]["C"])
        Options.append(Rq[1]["D"])
        
        Quiz[1].clear() # Here I cleared the nested dictionary so that the question only remains
        Question.append(Quiz) # It is then appended to the question list
        print(str(*Question[0][:-1])) # This converts the item in the array to str so that it can remove Curly brackets that appear when it outputs the question
        for Answers in Options: # This for loop goes over each option to output it line by line
            print(Answers) 
    elif Topic == 2: # This is the topic for Physics
        Rq = random.choice(list(Subject["Physics"].items())) # This picks a random question from the physics subject dictionary
        Quiz = copy.deepcopy(Rq)
        Ans.append(Rq[1]["Answer"])
        # Here is where each option is appended to the Options list
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
        Rq = random.choice(list(Subject["English"].items())) # This picks a random question from the english subject dictionary
        Options.append(Rq[1]["A"])
        Quiz = copy.deepcopy(Rq)
        Ans.append(Rq[1]["Answer"]) 
        Options.append(Rq[1]["B"])
        Options.append(Rq[1]["C"])
        Options.append(Rq[1]["D"])
        Quiz[1].clear()
        Question.append(list(Quiz))
        for x in Question: 
            print(str(*x[:-1])) # This converts the item in the array to str so that it can remove Curly brackets that appear when it outputs the question
        for Answers in Options:
            print(Answers)
        

# This function that allows user input and validates input also has a timeout feature for when the timeout ends 
def Guess():
    """
    The guess function allows the user to input an answer to the question it also prints the timer and reduces the time left
    
    Parameters
    ---------

    Guess: LiteralString | str
        This is how the user enters their guess

    timeout: float
        The time limit until the user can input an answer

    Timer: int
        This is the timer prompting the user to finish
    
    U_Answer: list
        This list is used to append what the user got wrong, correct and timeout

    Example
    ---------

        Timer: You have 60s left    
    
    """
    global Count
    Timer = Limit - Elapsed.__round__(0) # Here is how the Time limit is calculated
    print(f"You have {Timer}s left") # Displays the time limit to the user
    try: 
        Guess = inputimeout(prompt = "please enter a guess to the question (A, B, C, D) ", timeout = Timer).upper() # This variable helps exit the input when user has reached the time limit
        while Guess != "A" and Guess != "B" and Guess != "C" and Guess != "D": #loop to validate user input
            print("incorrect input, must be (A, B, C or D)")
            Guess = inputimeout(prompt = "please enter a guess to the question (A, B, C, D) ", timeout = Timer).upper()
        for key in Rq: #loop that goes through the answer for each question and checks users input
            if Ans[0] == Guess: # This conditional statement compares the correct answer withe the users guess
                print("Correct") 
                Count += 1 # Here is the count for the amount of questions the user got correct
                U_Answers.append("Correct") # This appends to a list that is later saved to the scores file when the user got something correct
                break
            else:
                print("Incorrect")
                print("Correct answer was", Ans[0])
                U_Answers.append("Wrong") # This appends to a list that is later saved to the scores file when the user got something wrong
                break
    except TimeoutOccurred: # This returns the user to the main menu when the time limit has been reached
        print("Times Up, returning to the main menu")
        U_Answers.append("Timeout") # This appends to a list that is later saved to the scores file when the user ran out of time
        time.sleep(1)
        
#this functions allows the user to review their past results

def Scores():
    """
    This function saves the users' score to the specific subject chosen

    Parameters
    -----------
    
    Score: TextIOWrapper[_WrappedBuffer]
        Saves the user score

    Example
    -----------
    
    {Username}, You got {Count} questions correct in (Subject). ['Correct', 'Wrong', 'Timeout']
    
    """
    Score = open("Scores.txt", "a") 
    if Topic == 1: # This checks if the topic chosen is math
        Score.write(f"{Username}, You got {Count} Questions correct in math. {U_Answers} \n") # Stores the username and count of questions the user got correct math
    elif Topic == 2: # This checks if the topic chosen is physics
        Score.write(f"{Username}, You got {Count} Questions correct in physics. {U_Answers} \n") # Stores the username and count of questions the user got correct for physics
    elif Topic == 3: # This checks if the topic chosen is english
        Score.write(f"{Username}, You got {Count} Questions correct in english. {U_Answers} \n") # Stores the username and count of questions the user got correct for english
    Score.close() # this closes the file


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
    Saved_User = View.readlines() # This reads lines of the scores file
    for x in range(len(Saved_User)): # This loops over line by line the Scores file
        if Username in Saved_User[x]: # This checks if the username exists in the file
            print(Saved_User[x])
    if Username not in Saved_User[x]:
        print("===============")
        print("user not found")
        
    View.close()
        