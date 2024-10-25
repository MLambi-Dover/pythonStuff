# Problem 4
# The very first thing we do is import the random library
import random

# First ask the user if they want addition or subtraction
userChoice = input("Would you like [A]ddition or [S]ubtraction or [B]oth? ")

# if they choose subtraction or both ask if they want negative numbers
if userChoice == 'S' or userChoice == 's' or userChoice == 'B' or userChoice == 'b':
    negNums = input("Would you like to include negative numbers: y or Y ")

gameOn = True
rightAnswers = 0  #  Need to initialize a variable for the right answers.
wrongAnswers = 0

while gameOn:
    num1 = random.randint(1,9)
    num2 = random.randint(1,9)
    
    if userChoice == 'a' or userChoice == 'A':
        answer = eval(input(f"What is the sum of {num1} + {num2}?"))
        solution = num1 + num2                                                     # We need to capture this and pass it so we do not have to repeat code
        print(num1, " + ", num2, "=", (num1+num2), " is ", (answer == num1+num2))  # I originally did not have a 'solution' variable, and this works
    else:
        if negNums == 'y' or negNums == 'Y':
            answer = eval(input(f"What is the sum of {num1} - {num2}?"))
            solution = num1 - num2
            print(num1, " - ", num2, "=", solution, " is ", (answer == solution))
        else:
            while num1 < num2:
                num1 = random.randint(1,9)
                num2 = random.randint(1,9)
            answer = eval(input(f"What is the sum of {num1} - {num2}?"))
            solution = num1 - num2
            print(num1, " - ", num2, "=", solution, " is ", (answer == solution))

    if answer == solution:
        rightAnswers += 1
    else:
        wrongAnswers += 1
    if rightAnswers >= 5 or wrongAnswers >= 3:
        gameOn = False

print("You finished the game!")
print("You had", rightAnswers, "correct answers, and", wrongAnswers, "wrong answers.")
