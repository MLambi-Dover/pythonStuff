print("Problem 5: Guessing Game")
# Ask a user for a number.  Have the computer 'guess' the number, and have the user respond if it is (h)igh, (l)ow or (c)orrect.
# The computer should not be only making random guesses.
# Two variables will be used to keep track of the best high and low guesses, which should narrow.
# Uncomment the print statement near the bottom to watch the guesses narrow as you play.

# Import our libraries first
import random

# Ask the user for a number between 1-100
userNumber = int(input("Enter a number between 1 and 100: "))
computerGuess = random.randint(1,100)   # This is the computers first guess.
numGuesses = 0                          # We initialize our guess counter to 0, so we can add to it.
highGuess = None                        # We initialize the high and low guess variables to None
lowGuess = None                         # They will evaluate to False when set this way.
gameOn = True                           # This variable will control our game loop, and starts off True.

while gameOn:
    userAnswer = input(f"Is your number {computerGuess}? \n Enter 'h' for high, 'l' for low and 'c' for correct.") 
    if userAnswer == 'h':
        if not highGuess:  # highGuess starts out False/None so this captures the first round.
            highGuess = computerGuess  # The guess is assigned as the first high 
            if not lowGuess:           # If the low guess is not already set, set it to 0.
                lowGuess = 0           # We only have a high guess, so we set this to the bottom of the range.
        elif highGuess > computerGuess:   # If the current high guess is higher
            highGuess = computerGuess     # set it to the lower number.  This will bring the guess closer to the number.
        # An else is not needed here as the default operation is to do nothing.

    elif userAnswer == 'l':
        if not lowGuess:   # lowGuess starts out False. This can only trigger during the first round.
            lowGuess = computerGuess   # If lowGuess is not set, set it.
            if not highGuess:          # If highGuess is not set, set it.
                highGuess = 100        # We only have a low guess, so we set this to the top of the range.
        elif lowGuess < computerGuess:
            lowGuess = computerGuess

    elif userAnswer == 'c':
        print(f"Your last number was {computerGuess}.  It took {numGuesses} guesses.")
        gameOn = False  # This will end the game loop.
    
    # print(f"lowGuess: {lowGuess}, highGuess: {highGuess}")   # This will print the low and high guesses
    numGuesses += 1
    computerGuess = random.randint(lowGuess+1, highGuess-1)  # The last thing we do before going back to the top of the loop
                                                             # is generate a new guess, but within the bounds of our previous guesses
                                                             # plus an adjustment.
