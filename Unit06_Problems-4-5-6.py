# Unit 06 Problems 4, 5, 6
# Problem 4: Palindrome Number
def reverseInt(inp):              # Returns a reversed int of its inp parameter
    newNum = str()                # Create an empty variable that is a string
    for digit in str(inp):        # Iterate through the digits after casting the number as a string
        newNum = digit + newNum   # Concatenate the current digit berfore the previous digits
    return int(newNum)            # Return the new number after casting it as an integer

def isPalindrome(inp):
    return int(inp) == reverseInt(inp)  # Cast the input as an integer and compare to the returned int.
                                        # isPalindrome returs True or False
# userInput = input("Enter a number: ")     # Uncomment this and the next line to test problem 4.
# print(isPalindrome(userInput))            # Uncomment to test problem 4.

# Problem 5: Palindromic Prime
def isPrime(num):
    if num > 1:                              # We do not test 1 for primeness.
        for i in range(2, (num//2)+1):       # We divide by every number up to half plus one.
            if (num % i) == 0:               # If a number is evenly divisible it is NOT a prime,
                break                        # and we break out of the for loop.
        else:                                # We haven't seen much of a for/else loop.
            return True                      # If the for loop fails to find a divisible number
                                             # return True.
def palindromicPrime(NumOfPrimes):
    primeCount = 0     # Counts the number of prime numbers found.
    lineCount = 0      # Counts the number of numbers per line; break at 10.
    currentNumber = 2  # The number being tested for primeness.
    while primeCount < NumOfPrimes:                    # Contine until we have found the number of primes.
        if isPrime(currentNumber):                     # If the number is prime,
            if isPalindrome(currentNumber):            # and the number is a palindrom
                print(f'{currentNumber:5d}', end=' ')  # print the number formatted for 5 digits and no line end.
                primeCount += 1                        # Increment the number of primes found.
                lineCount += 1                         # Increment the line count.
                if lineCount ==10:                     # If 10 numbers have been printed
                    print()                            # print a new-line,
                    lineCount = 0                      # and reset the line counter.
        currentNumber += 1   # Finally, we increment to the next number to test.
    print("Done")


# palindromicPrime(100)  # Uncomment this line to test this portion of code.

# Problem 6: Emirp
primeCount = 0
lineCount = 0
currentNumber = 2
while primeCount < 101:    # Hard coded to test for 100; could be replaced with user input.
    if isPrime(currentNumber):
        if isPrime(reverseInt(currentNumber)):
            print(f"{currentNumber:5d}", end=' ')
            primeCount += 1
            lineCount += 1
            if lineCount == 10:
                print('')
                lineCount = 0
    currentNumber += 1
    print("Done")
