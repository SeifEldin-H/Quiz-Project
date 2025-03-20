import time
import Functions

def main():
    """
    this function 


    """
    Functions.Intro()
    while True: #indefinite loop until user wants to exit 
        Functions.Main_Menu()
        if Functions.User_Start == 1:
            while True:
                Functions.Topics()
                if Functions.Topic == 4 or Functions.Topic == 5:
                    continue
                else:
                    break
            if Functions.Elapsed < Functions.Limit:
                for i in range(Functions.Numb_of_Q):
                    print("Question",i+1)
                    Functions.Randomizer() #this randomizes the questions
                    Functions.Guess()
                    Functions.Elapsed = time.time() - Functions.Start
                        
                    print("===============")
                Functions.Scores()
        elif Functions.User_Start == 2:
            time.sleep(1)
            Functions.Viewing()

       



if __name__ == '__main__':
    main()