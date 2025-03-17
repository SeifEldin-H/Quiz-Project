import time
import Functions
def main():
    Functions.Intro()
    while True:
        Functions.MainMenu()
        try:
            if Functions.UserStart == 1:
                Functions.Topics()
                if Functions.Elapsed < Functions.Limit:
                    for i in range(3):
                        if Functions.Elapsed >= 10 :
                            print("Times up returning to main menu")
                            time.sleep(1)
                        else:
                            print("Question",i+1)
                            Functions.randomizer()
                            Functions.Guess()
                            Functions.Question.pop()
                            Functions.Options.pop()
                            Functions.Elapsed = time.time() - Functions.Start
                            print(Functions.Elapsed.__round__(0))
                            
                        print("===============")
                    Functions.Scores()
            elif Functions.UserStart == 2:
                Functions.Viewing()
        except ValueError:
            print("Invalid input please enter the correct values are ")
        else:
            False



if __name__ == '__main__':
    main()