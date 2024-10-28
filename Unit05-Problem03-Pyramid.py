# Problem 3
# Pyramid 1-15  (20 points)

# Ask for an input and require it to be between 1-15.
# First I have to initialize a variable. None = False.
# userNumber = None
userNumber = 0   # hard coding this to test until I get to 9 working.

# Next we run the loop for as long as the userNumber is None/False.
while userNumber < 1 or userNumber > 15:   # This will run UNTIL userNumber is True.
    userNumber = eval(input("Enter a number between 1 and 15: "))

spacer = "   "         # Using variables for the spaces
spacer2 = " "          # so they can be changed later.
if userNumber > 9:
    spacer = "    "    # When the number is double-digits
    spacer2 = "  "     # the spacing needs to be adjusted.
spacer3 = " "

print("The number entered is:", userNumber)
print()


for row in range(1, userNumber+1):
    if row == 1:  # The first row only has one number
        print(spacer * (userNumber - row), row)
    
    elif row >= 1:  # Any other row will add two loops to print
        print(spacer *  (userNumber - row), row, end='')
        for i in range(1, row):
            if (row-i) < 9:                        # Here we test to see if the number is double-digits
                print(spacer2, (row-i), end='')
            else:                                            # and we adjust the spacing if it is.
                print(spacer3, (row-i), end='')

        for i in range(row, 1, -1):
            if (row-i+2) < 9:                       # Here we test to see if the number is double-digits
                print(spacer2, (row - i)+2, end='')
            else:                                             # and we adjust the spacing if it is.
                print(spacer3, (row - i)+2, end='')
        
        print()
