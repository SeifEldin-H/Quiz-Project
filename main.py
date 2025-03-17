import time
import Functions

def main():
    Functions.Intro()
    while True: #indefinite loop until user wants to exit 
        Functions.MainMenu()
        if Functions.UserStart == 1:
            Functions.Topics()
            if Functions.Elapsed < Functions.Limit:
                for i in range(3):
                    if Functions.Elapsed >= Functions.Limit :
                        print("Times up returning to main menu")
                        time.sleep(1)
                    else:
                        print("Question",i+1)
                        Functions.randomizer() #this randomizes the questions
                        Functions.Guess()
                        Functions.Question.pop()
                        Functions.Options.pop()
                        Functions.Elapsed = time.time() - Functions.Start
                        
                    print("===============")
                Functions.Scores()
        elif Functions.UserStart == 2:
            Functions.Viewing()



if __name__ == '__main__':
    main()