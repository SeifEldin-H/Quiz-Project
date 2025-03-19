import time
import Functions

def main():
    """
    this function 


    """
    Functions.Intro()
    while True: #indefinite loop until user wants to exit 
        Functions.MainMenu()
        if Functions.UserStart == 1:
            while True:
                Functions.Topics()
                if Functions.Topic == 4 or Functions.Topic == 5:
                    continue
                else:
                    break
            if Functions.Elapsed < Functions.Limit:
                for i in range(Functions.NumbofQ):
                    print("Question",i+1)
                    Functions.randomizer() #this randomizes the questions
                    Functions.Guess()
                    
                    Functions.Elapsed = time.time() - Functions.Start
                        
                    print("===============")
                Functions.Scores()
        elif Functions.UserStart == 2:
            Functions.Viewing()



if __name__ == '__main__':
    main()