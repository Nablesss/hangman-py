import random
import sys

state = 0
wrongs = 0
words = ["apple", "banana", "peach", "cherrys", "grapes", "lamp", "bed", "desk", "computer", "headset"]
lineDraw= []

def gameloop():     #filles the reference list "toGuess" with "_"'s according to the length of the word which needs to be guessed
    global toGuess
    which = random.randint(0, int(len(words)-1))
    toGuess = list(words[which])
    for i in toGuess:
        lineDraw.append("_")
    print(lineDraw)
    guessing()

def restart():              #resets the important game variables or quits the console when"choice" equals "no"
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

def double_check():         #checks if the "guess" appears another time in the word
    if guess in toGuess:      #in an own function so that the "no" is not printed after the filled in letters
        place = toGuess.index(guess)
        lineDraw[place] = guess
        toGuess[place] = "_"
        print(lineDraw)
        check_win()
        double_check()
    else:
        guessing()

def checker(): 
    global state     #checks if guess is in the list of Word2
    if guess in toGuess:
        double_check()
    else:
        state += 1
        drawHangman(state)
        guessing()

def guessing():     #gets the input from the letter and saves it inside "guess"
    global place
    global guess
    guess = input("Guess a letter: ")
    checker()

def check_win():     #if the reference list is completely filled with "_" the game is won
    so = 0
    for i in toGuess:
        if i == "_":
            so += 1
    if so == len(toGuess):
        print("\nYou won!")
        restart()
    else:
        double_check()

def drawHangman(state):                                     #visualisations of the hangman for printing in the console
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
