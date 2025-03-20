import time
import Functions

def main():
    Functions.Intro()
    while True: #indefinite loop until user wants to exit 
        Functions.Main_Menu()
        if Functions.User_Start == 1:
            while True:
                Functions.Topics()
                if Functions.Topic == 4 or Functions.Topic == 5: # Checks if the settings for time change and number of question change to loop back to topics menu
                    continue
                else:
                    break
            if Functions.Elapsed < Functions.Limit: # Checks if time elapsed is below time limit
                for i in range(Functions.Numb_of_Q):
                    if Functions.Elapsed >= Functions.Limit: # Checks if time limit has been reached or not
                        time.sleep(1) # Delays the output of terminal by 1 sec
                    else:
                        print("Question",i+1)
                    
                        Functions.Randomizer()
                        Functions.Guess()
                        
                        Functions.Elapsed = time.time() - Functions.Start
                        
                    print("===============")
                Functions.Scores()
            else:
                break
        elif Functions.User_Start == 2:
            Functions.Viewing()

       



if __name__ == '__main__':
    main()