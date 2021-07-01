import random
import sys

global words
global wrongs
global toGuess
global lineDraw
global state

state = 0
wrongs = 0
words = ["apple", "banana", "lamp", "hello"]
lineDraw= []

def gameloop():
    global toGuess
    which = random.randint(0, int(len(words)-1))
    toGuess = list(words[which])
    for i in toGuess:
        lineDraw.append("_")
    print(lineDraw)
    guessing()

def restart():
        choice = input("Wanna Restart?(ye/no) ")
        if choice == "ye":
            global words
            global wrongs
            global toGuess
            global lineDraw
            global state

            state = 0
            wrongs = 0
            words = ["apple", "banana", "lamp", "hello"]
            lineDraw = []
            print("Nice! Then let's give it another try!")
            gameloop()
        elif choice == "no":
            print("Then not, Loser!")
            exit()
        else:
            restart()

def double_check():         #überprüft ob das "guess" nochmal irgendwo im Wort vorkommt. 
    if guess in toGuess:      #Ausgelagert, damit "no" nicht danach geprintet wird
        place = toGuess.index(guess)
        lineDraw[place] = guess
        toGuess[place] = "_"
        print(lineDraw)
        check_win()
        double_check()
    else:
        guessing()

def checker(): 
    global state     #checkt ob der guess in der Liste vom Word2 ist
    if guess in toGuess:
        double_check()
    else:
        state += 1
        drawHangman(state)
        guessing()

def guessing():
    global place
    global guess
    guess = input("Guess a letter: ")
    checker()

def check_win():
    so = 0
    for i in toGuess:
        if i == "_":
            so += 1
    if so == len(toGuess):
        print("\nYou won!")
        restart()
    else:
        double_check()

def set_word():
    print("word")


def drawHangman(state):
    if state == 1:
        print("\nYou've got "+str(10-state)+" trys left!")
        print("""
    
    	    
    	    
         
         
    
    #####
        """)

    if state == 2:
        print("\nYou've got "+str(10-state)+" trys left!")
        print("""
    __
    |>
    ||    
    ||	    
    ||     
    ||     
    ||
    #####
        """)
    
    if state == 3:
        print("\nYou've got "+str(10-state)+" trys left!")
        print("""
    __
    |>---------
    ||    
    ||	    
    ||     
    ||     
    ||
    #####
        """)
    
    if state == 4:
        print("\nYou've got "+str(10-state)+" trys left!")
        print("""
    __
    |>---------
    ||      |
    ||	    
    ||     
    ||     
    ||
    #####
        """)

    if state == 5:
        print("\nYou've got "+str(10-state)+" trys left!")
        print("""
    __
    |>---------
    ||      |
    ||	    o
    ||      
    ||     
    ||
    #####
        """)

    if state == 6:
        print("\nYou've got "+str(10-state)+" trys left!")
        print("""
    __
    |>---------
    ||      |
    ||	    o
    ||      |
    ||     
    ||
    #####
        """)

    if state == 7:
        print("\nYou've got "+str(10-state)+" trys left!")
        print("""
    __
    |>---------
    ||      |
    ||	    o
    ||     -|
    ||     
    ||
    #####
        """)

    if state == 8:
        print("\nYou've got "+str(10-state)+" trys left!")
        print("""
    __
    |>---------
    ||      |
    ||	    o
    ||     -|-
    ||     
    ||
    #####
        """)

    if state == 9:
        print("\nYou've got just "+str(10-state)+" try left, choose wisely!")
        print("""
    __
    |>---------
    ||      |
    ||	    o
    ||     -|-
    ||     /
    ||
    #####
        """)

    if state == 10:
        print("\nLoser! You L O S T")
        print("""
    __
    |>---------
    ||      |
    ||	    o
    ||     -|-
    ||     //
    ||
    #####
        """)
        restart()
    print(lineDraw)
    guessing()


gameloop()
